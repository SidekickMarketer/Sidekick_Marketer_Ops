from fastapi import FastAPI, Request, Depends, HTTPException, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from datetime import datetime
import secrets
import os
import shutil
from pathlib import Path

from .database import engine, get_db, Base
from .models import Client, Strategy, Post, PreviousPost, Photo, Comment, Batch, PostStatus, ProfileAudit, AUDIT_CHECKLISTS, StrategyFile, OnboardingStatus
from .services import caption_generator, metricool, strategy_parser

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Caption Management App")

# Setup static files and templates
BASE_DIR = Path(__file__).resolve().parent.parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Ensure upload directory exists
UPLOAD_DIR = BASE_DIR / "static" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# AGENCY DASHBOARD ROUTES
# ============================================================================

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    """Main agency dashboard"""
    clients = db.query(Client).filter(Client.is_active == True).all()
    recent_posts = db.query(Post).order_by(Post.created_at.desc()).limit(10).all()

    return templates.TemplateResponse("agency/dashboard.html", {
        "request": request,
        "clients": clients,
        "recent_posts": recent_posts,
        "metricool_status": metricool.validate_metricool_config()
    })


# ============================================================================
# CLIENT MANAGEMENT
# ============================================================================

@app.get("/clients", response_class=HTMLResponse)
async def list_clients(request: Request, db: Session = Depends(get_db)):
    """List all clients"""
    clients = db.query(Client).all()
    return templates.TemplateResponse("agency/clients.html", {
        "request": request,
        "clients": clients
    })


@app.get("/clients/new", response_class=HTMLResponse)
async def new_client_form(request: Request):
    """Form to create new client"""
    return templates.TemplateResponse("agency/client_form.html", {
        "request": request,
        "client": None
    })


@app.post("/clients")
async def create_client(
    request: Request,
    name: str = Form(...),
    db: Session = Depends(get_db)
):
    """Create a new client"""
    # Generate slug and review token
    slug = name.lower().replace(" ", "-").replace("'", "")
    review_token = secrets.token_urlsafe(32)

    client = Client(
        name=name,
        slug=slug,
        review_token=review_token,
        onboarding_status=OnboardingStatus.IN_PROGRESS,
        onboarding_step=1
    )
    db.add(client)
    db.commit()
    db.refresh(client)

    # Create empty strategy
    strategy = Strategy(client_id=client.id)
    db.add(strategy)
    db.commit()

    # Redirect to onboarding wizard
    return RedirectResponse(f"/clients/{client.id}/onboarding", status_code=303)


@app.get("/clients/{client_id}", response_class=HTMLResponse)
async def view_client(request: Request, client_id: int, db: Session = Depends(get_db)):
    """View client details and manage"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    posts = db.query(Post).filter(Post.client_id == client_id).order_by(Post.created_at.desc()).all()
    photos = db.query(Photo).filter(Photo.client_id == client_id).all()

    return templates.TemplateResponse("agency/client_detail.html", {
        "request": request,
        "client": client,
        "posts": posts,
        "photos": photos
    })


@app.get("/clients/{client_id}/strategy", response_class=HTMLResponse)
async def edit_strategy(request: Request, client_id: int, db: Session = Depends(get_db)):
    """Edit client strategy"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    return templates.TemplateResponse("agency/strategy_form.html", {
        "request": request,
        "client": client,
        "strategy": client.strategy
    })


@app.post("/clients/{client_id}/strategy")
async def save_strategy(
    request: Request,
    client_id: int,
    db: Session = Depends(get_db)
):
    """Save client strategy"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    form_data = await request.form()

    strategy = client.strategy
    if not strategy:
        strategy = Strategy(client_id=client_id)
        db.add(strategy)

    # Update strategy fields
    strategy.brand_voice = form_data.get("brand_voice", "")
    strategy.tone_keywords = [k.strip() for k in form_data.get("tone_keywords", "").split(",") if k.strip()]
    strategy.content_pillars = [p.strip() for p in form_data.get("content_pillars", "").split(",") if p.strip()]
    strategy.target_audience = form_data.get("target_audience", "")
    strategy.audience_pain_points = [p.strip() for p in form_data.get("audience_pain_points", "").split(",") if p.strip()]
    strategy.platforms = [p.strip() for p in form_data.getlist("platforms")]
    strategy.industry = form_data.get("industry", "")
    strategy.unique_selling_points = [u.strip() for u in form_data.get("unique_selling_points", "").split(",") if u.strip()]
    strategy.key_messages = [m.strip() for m in form_data.get("key_messages", "").split("\n") if m.strip()]
    strategy.topics_to_avoid = [t.strip() for t in form_data.get("topics_to_avoid", "").split(",") if t.strip()]
    strategy.additional_notes = form_data.get("additional_notes", "")

    # Parse hashtag sets
    primary_hashtags = [h.strip().replace("#", "") for h in form_data.get("primary_hashtags", "").split(",") if h.strip()]
    secondary_hashtags = [h.strip().replace("#", "") for h in form_data.get("secondary_hashtags", "").split(",") if h.strip()]
    strategy.hashtag_sets = {"primary": primary_hashtags, "secondary": secondary_hashtags}

    db.commit()

    return RedirectResponse(f"/clients/{client_id}", status_code=303)


# ============================================================================
# CAPTION GENERATION
# ============================================================================

@app.get("/clients/{client_id}/generate", response_class=HTMLResponse)
async def generate_captions_form(request: Request, client_id: int, db: Session = Depends(get_db)):
    """Form to generate new captions"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    return templates.TemplateResponse("agency/generate_form.html", {
        "request": request,
        "client": client
    })


@app.post("/clients/{client_id}/generate")
async def generate_captions(
    request: Request,
    client_id: int,
    db: Session = Depends(get_db)
):
    """Generate captions using AI"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client or not client.strategy:
        raise HTTPException(status_code=404, detail="Client or strategy not found")

    form_data = await request.form()

    # Get previous posts for deduplication
    previous = db.query(PreviousPost).filter(PreviousPost.client_id == client_id).all()
    previous_captions = [p.caption for p in previous]

    # Also include posts we've already created
    existing_posts = db.query(Post).filter(Post.client_id == client_id).all()
    previous_captions.extend([p.caption for p in existing_posts])

    # Build strategy dict
    strategy_dict = {
        "brand_voice": client.strategy.brand_voice,
        "tone_keywords": client.strategy.tone_keywords or [],
        "content_pillars": client.strategy.content_pillars or [],
        "target_audience": client.strategy.target_audience,
        "audience_pain_points": client.strategy.audience_pain_points or [],
        "industry": client.strategy.industry,
        "unique_selling_points": client.strategy.unique_selling_points or [],
        "key_messages": client.strategy.key_messages or [],
        "topics_to_avoid": client.strategy.topics_to_avoid or [],
        "hashtag_sets": client.strategy.hashtag_sets or {}
    }

    # Generate captions
    num_captions = int(form_data.get("num_captions", 5))
    platform = form_data.get("platform", "instagram")
    content_theme = form_data.get("content_theme", None)
    specific_topic = form_data.get("specific_topic", None)
    batch_name = form_data.get("batch_name", f"Batch {datetime.now().strftime('%Y-%m-%d')}")

    captions = caption_generator.generate_captions(
        strategy=strategy_dict,
        previous_posts=previous_captions,
        num_captions=num_captions,
        platform=platform,
        content_theme=content_theme if content_theme else None,
        specific_topic=specific_topic if specific_topic else None
    )

    # Save generated captions as posts
    for cap in captions:
        if "error" not in cap:
            hashtags = " ".join([f"#{h}" for h in cap.get("hashtags", [])])
            post = Post(
                client_id=client_id,
                caption=cap.get("caption", ""),
                hashtags=hashtags,
                platform=platform,
                batch_name=batch_name,
                status=PostStatus.DRAFT
            )
            db.add(post)

    db.commit()

    return RedirectResponse(f"/clients/{client_id}", status_code=303)


# ============================================================================
# POST MANAGEMENT
# ============================================================================

@app.get("/posts/{post_id}", response_class=HTMLResponse)
async def view_post(request: Request, post_id: int, db: Session = Depends(get_db)):
    """View and edit a single post"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    photos = db.query(Photo).filter(Photo.client_id == post.client_id).all()

    return templates.TemplateResponse("agency/post_detail.html", {
        "request": request,
        "post": post,
        "photos": photos
    })


@app.post("/posts/{post_id}")
async def update_post(
    request: Request,
    post_id: int,
    db: Session = Depends(get_db)
):
    """Update a post"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    form_data = await request.form()

    post.caption = form_data.get("caption", post.caption)
    post.hashtags = form_data.get("hashtags", post.hashtags)
    post.platform = form_data.get("platform", post.platform)

    photo_id = form_data.get("photo_id")
    if photo_id:
        post.photo_id = int(photo_id)

    scheduled = form_data.get("scheduled_date")
    if scheduled:
        post.scheduled_date = datetime.fromisoformat(scheduled)

    db.commit()

    return RedirectResponse(f"/posts/{post_id}", status_code=303)


@app.post("/posts/{post_id}/status")
async def update_post_status(
    post_id: int,
    status: str = Form(...),
    db: Session = Depends(get_db)
):
    """Update post status"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.status = status
    if status == PostStatus.APPROVED:
        post.approved_at = datetime.utcnow()

    db.commit()

    return JSONResponse({"success": True, "status": status})


@app.post("/posts/{post_id}/schedule")
async def schedule_post_to_metricool(
    post_id: int,
    db: Session = Depends(get_db)
):
    """Push approved post to Metricool for scheduling"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.status != PostStatus.APPROVED:
        return JSONResponse({"error": "Post must be approved before scheduling"}, status_code=400)

    client = post.client
    if not client.metricool_blog_id:
        return JSONResponse({"error": "Client not linked to Metricool"}, status_code=400)

    if not post.scheduled_date:
        return JSONResponse({"error": "No scheduled date set"}, status_code=400)

    # Build full caption with hashtags
    full_caption = post.caption
    if post.hashtags:
        full_caption += f"\n\n{post.hashtags}"

    # Schedule in Metricool
    result = await metricool.schedule_post(
        blog_id=client.metricool_blog_id,
        caption=full_caption,
        platform=post.platform,
        scheduled_datetime=post.scheduled_date
    )

    if "error" in result:
        return JSONResponse({"error": result["error"]}, status_code=400)

    post.status = PostStatus.SCHEDULED
    post.metricool_post_id = result.get("id")
    db.commit()

    return JSONResponse({"success": True, "metricool_id": result.get("id")})


# ============================================================================
# PHOTO MANAGEMENT
# ============================================================================

@app.get("/clients/{client_id}/photos", response_class=HTMLResponse)
async def view_photos(request: Request, client_id: int, db: Session = Depends(get_db)):
    """View client photo library"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    photos = db.query(Photo).filter(Photo.client_id == client_id).all()

    return templates.TemplateResponse("agency/photos.html", {
        "request": request,
        "client": client,
        "photos": photos
    })


@app.post("/clients/{client_id}/photos")
async def upload_photo(
    client_id: int,
    file: UploadFile = File(...),
    description: str = Form(""),
    tags: str = Form(""),
    db: Session = Depends(get_db)
):
    """Upload a photo for a client"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    # Create client folder
    client_folder = UPLOAD_DIR / client.slug
    client_folder.mkdir(exist_ok=True)

    # Save file with unique name
    ext = Path(file.filename).suffix
    filename = f"{secrets.token_hex(8)}{ext}"
    file_path = client_folder / filename

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Parse tags
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]

    photo = Photo(
        client_id=client_id,
        filename=filename,
        original_filename=file.filename,
        file_path=f"/static/uploads/{client.slug}/{filename}",
        description=description,
        tags=tag_list
    )
    db.add(photo)
    db.commit()

    return RedirectResponse(f"/clients/{client_id}/photos", status_code=303)


# ============================================================================
# CLIENT REVIEW PORTAL (Public-facing)
# ============================================================================

@app.get("/review/{review_token}", response_class=HTMLResponse)
async def client_review_portal(request: Request, review_token: str, db: Session = Depends(get_db)):
    """Client-facing review portal"""
    client = db.query(Client).filter(Client.review_token == review_token).first()
    if not client:
        raise HTTPException(status_code=404, detail="Invalid review link")

    # Get posts pending client review
    posts = db.query(Post).filter(
        Post.client_id == client.id,
        Post.status == PostStatus.CLIENT_REVIEW
    ).order_by(Post.scheduled_date).all()

    return templates.TemplateResponse("client/review.html", {
        "request": request,
        "client": client,
        "posts": posts
    })


@app.post("/review/{review_token}/posts/{post_id}/approve")
async def client_approve_post(
    review_token: str,
    post_id: int,
    db: Session = Depends(get_db)
):
    """Client approves a post"""
    client = db.query(Client).filter(Client.review_token == review_token).first()
    if not client:
        raise HTTPException(status_code=404, detail="Invalid review link")

    post = db.query(Post).filter(Post.id == post_id, Post.client_id == client.id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.status = PostStatus.APPROVED
    post.approved_at = datetime.utcnow()
    db.commit()

    return JSONResponse({"success": True})


@app.post("/review/{review_token}/posts/{post_id}/request-changes")
async def client_request_changes(
    request: Request,
    review_token: str,
    post_id: int,
    db: Session = Depends(get_db)
):
    """Client requests changes to a post"""
    client = db.query(Client).filter(Client.review_token == review_token).first()
    if not client:
        raise HTTPException(status_code=404, detail="Invalid review link")

    post = db.query(Post).filter(Post.id == post_id, Post.client_id == client.id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    form_data = await request.form()
    comment_text = form_data.get("comment", "")

    # Add comment
    comment = Comment(
        post_id=post_id,
        author_type="client",
        author_name=client.name,
        content=comment_text
    )
    db.add(comment)

    post.status = PostStatus.REVISION_REQUESTED
    post.client_comment = comment_text
    db.commit()

    return JSONResponse({"success": True})


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.get("/api/clients/{client_id}/posts")
async def api_get_posts(client_id: int, status: str = None, db: Session = Depends(get_db)):
    """API to get posts for a client"""
    query = db.query(Post).filter(Post.client_id == client_id)
    if status:
        query = query.filter(Post.status == status)

    posts = query.order_by(Post.created_at.desc()).all()

    return [{
        "id": p.id,
        "caption": p.caption,
        "hashtags": p.hashtags,
        "platform": p.platform,
        "status": p.status,
        "scheduled_date": p.scheduled_date.isoformat() if p.scheduled_date else None,
        "photo_url": p.photo.file_path if p.photo else None
    } for p in posts]


@app.get("/api/metricool/brands")
async def api_get_metricool_brands():
    """Get all Metricool brands for linking"""
    brands = await metricool.get_brands()
    return brands


@app.post("/api/clients/{client_id}/link-metricool")
async def link_metricool(
    client_id: int,
    blog_id: str = Form(...),
    db: Session = Depends(get_db)
):
    """Link a client to their Metricool brand"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    client.metricool_blog_id = blog_id
    db.commit()

    return JSONResponse({"success": True})


# ============================================================================
# PREVIOUS POSTS (for deduplication)
# ============================================================================

@app.post("/clients/{client_id}/import-previous")
async def import_previous_posts(
    client_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Import previous posts from CSV for deduplication"""
    import csv
    import io

    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    content = await file.read()
    decoded = content.decode("utf-8")
    reader = csv.DictReader(io.StringIO(decoded))

    count = 0
    for row in reader:
        caption = row.get("caption") or row.get("Caption") or row.get("text") or row.get("Text")
        if caption:
            prev = PreviousPost(
                client_id=client_id,
                caption=caption,
                platform=row.get("platform", "unknown"),
                posted_date=datetime.now()  # Could parse from row if available
            )
            db.add(prev)
            count += 1

    db.commit()

    return JSONResponse({"success": True, "imported": count})


# ============================================================================
# PROFILE AUDITS
# ============================================================================

@app.get("/clients/{client_id}/audits", response_class=HTMLResponse)
async def view_audits(request: Request, client_id: int, db: Session = Depends(get_db)):
    """View all profile audits for a client"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    # Get existing audits
    audits = db.query(ProfileAudit).filter(ProfileAudit.client_id == client_id).all()
    audits_by_platform = {a.platform: a for a in audits}

    # Get platforms from client strategy, or default to common ones
    platforms = []
    if client.strategy and client.strategy.platforms:
        platforms = client.strategy.platforms
    else:
        platforms = ["facebook", "instagram", "gbp"]

    # Build audit summary for each platform
    audit_summary = []
    for platform in platforms:
        if platform in AUDIT_CHECKLISTS:
            existing = audits_by_platform.get(platform)
            audit_summary.append({
                "platform": platform,
                "name": AUDIT_CHECKLISTS[platform]["name"],
                "score": existing.score if existing else 0,
                "last_audited": existing.last_audited_at if existing else None,
                "total_items": len(AUDIT_CHECKLISTS[platform]["items"]),
                "critical_items": len([i for i in AUDIT_CHECKLISTS[platform]["items"] if i["critical"]])
            })

    return templates.TemplateResponse("agency/audits.html", {
        "request": request,
        "client": client,
        "audit_summary": audit_summary,
        "available_platforms": list(AUDIT_CHECKLISTS.keys())
    })


@app.get("/clients/{client_id}/audits/{platform}", response_class=HTMLResponse)
async def edit_audit(request: Request, client_id: int, platform: str, db: Session = Depends(get_db)):
    """Edit a specific platform audit"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    if platform not in AUDIT_CHECKLISTS:
        raise HTTPException(status_code=404, detail="Invalid platform")

    # Get or create audit
    audit = db.query(ProfileAudit).filter(
        ProfileAudit.client_id == client_id,
        ProfileAudit.platform == platform
    ).first()

    checklist_data = audit.checklist_data if audit else {}

    # Build checklist with current state
    checklist = AUDIT_CHECKLISTS[platform]
    items_with_state = []
    for item in checklist["items"]:
        item_data = checklist_data.get(item["key"], {})
        items_with_state.append({
            **item,
            "checked": item_data.get("checked", False),
            "notes": item_data.get("notes", "")
        })

    return templates.TemplateResponse("agency/audit_detail.html", {
        "request": request,
        "client": client,
        "platform": platform,
        "platform_name": checklist["name"],
        "items": items_with_state,
        "score": audit.score if audit else 0,
        "last_audited": audit.last_audited_at if audit else None
    })


@app.post("/clients/{client_id}/audits/{platform}")
async def save_audit(
    request: Request,
    client_id: int,
    platform: str,
    db: Session = Depends(get_db)
):
    """Save audit checklist"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    if platform not in AUDIT_CHECKLISTS:
        raise HTTPException(status_code=404, detail="Invalid platform")

    form_data = await request.form()

    # Get or create audit
    audit = db.query(ProfileAudit).filter(
        ProfileAudit.client_id == client_id,
        ProfileAudit.platform == platform
    ).first()

    if not audit:
        audit = ProfileAudit(client_id=client_id, platform=platform)
        db.add(audit)

    # Process form data
    checklist_data = {}
    checklist = AUDIT_CHECKLISTS[platform]

    checked_count = 0
    for item in checklist["items"]:
        key = item["key"]
        is_checked = form_data.get(f"check_{key}") == "on"
        notes = form_data.get(f"notes_{key}", "")

        checklist_data[key] = {
            "checked": is_checked,
            "notes": notes
        }

        if is_checked:
            checked_count += 1

    # Calculate score
    total_items = len(checklist["items"])
    score = int((checked_count / total_items) * 100) if total_items > 0 else 0

    audit.checklist_data = checklist_data
    audit.score = score
    audit.last_audited_at = datetime.utcnow()

    db.commit()

    return RedirectResponse(f"/clients/{client_id}/audits", status_code=303)


# ============================================================================
# CLIENT ONBOARDING
# ============================================================================

STRATEGY_UPLOAD_DIR = BASE_DIR / "static" / "uploads" / "strategies"
STRATEGY_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/clients/{client_id}/onboarding", response_class=HTMLResponse)
async def onboarding_wizard(request: Request, client_id: int, db: Session = Depends(get_db)):
    """Client onboarding wizard - upload strategy files"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    # Get any previously uploaded strategy files
    strategy_files = db.query(StrategyFile).filter(StrategyFile.client_id == client_id).all()

    # Get extracted strategy data from session or strategy
    extracted_data = {}
    if client.strategy:
        extracted_data = {
            "brand_voice": client.strategy.brand_voice,
            "tone_keywords": client.strategy.tone_keywords or [],
            "content_pillars": client.strategy.content_pillars or [],
            "target_audience": client.strategy.target_audience,
            "audience_pain_points": client.strategy.audience_pain_points or [],
            "industry": client.strategy.industry,
            "unique_selling_points": client.strategy.unique_selling_points or [],
            "key_messages": client.strategy.key_messages or [],
            "topics_to_avoid": client.strategy.topics_to_avoid or [],
            "hashtag_sets": client.strategy.hashtag_sets or {},
            "platforms": client.strategy.platforms or [],
        }

    return templates.TemplateResponse("agency/onboarding.html", {
        "request": request,
        "client": client,
        "strategy_files": strategy_files,
        "extracted_data": extracted_data,
        "step": client.onboarding_step or 1
    })


@app.post("/clients/{client_id}/onboarding/upload-strategy")
async def upload_strategy_file(
    client_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload and parse a strategy document"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    # Create client strategy folder
    client_folder = STRATEGY_UPLOAD_DIR / client.slug
    client_folder.mkdir(exist_ok=True)

    # Save file
    ext = Path(file.filename).suffix.lower()
    filename = f"{secrets.token_hex(8)}{ext}"
    file_path = client_folder / filename

    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    # Parse the document
    extracted = strategy_parser.parse_strategy_document(content, file.filename, client.name)

    # Save strategy file record
    strategy_file = StrategyFile(
        client_id=client_id,
        filename=filename,
        original_filename=file.filename,
        file_path=f"/static/uploads/strategies/{client.slug}/{filename}",
        file_type=ext.replace(".", ""),
        extracted_summary=extracted.get("summary", ""),
        processed=True
    )
    db.add(strategy_file)

    # Update strategy with extracted data
    if client.strategy and "error" not in extracted:
        strategy = client.strategy

        # Merge extracted data with existing (don't overwrite existing values)
        if extracted.get("brand_voice") and not strategy.brand_voice:
            strategy.brand_voice = extracted["brand_voice"]

        if extracted.get("tone_keywords"):
            existing = strategy.tone_keywords or []
            strategy.tone_keywords = list(dict.fromkeys(existing + extracted["tone_keywords"]))

        if extracted.get("content_pillars"):
            existing = strategy.content_pillars or []
            strategy.content_pillars = list(dict.fromkeys(existing + extracted["content_pillars"]))

        if extracted.get("target_audience") and not strategy.target_audience:
            strategy.target_audience = extracted["target_audience"]

        if extracted.get("audience_pain_points"):
            existing = strategy.audience_pain_points or []
            strategy.audience_pain_points = list(dict.fromkeys(existing + extracted["audience_pain_points"]))

        if extracted.get("industry") and extracted["industry"] != "default" and not strategy.industry:
            strategy.industry = extracted["industry"]

        if extracted.get("unique_selling_points"):
            existing = strategy.unique_selling_points or []
            strategy.unique_selling_points = list(dict.fromkeys(existing + extracted["unique_selling_points"]))

        if extracted.get("key_messages"):
            existing = strategy.key_messages or []
            strategy.key_messages = list(dict.fromkeys(existing + extracted["key_messages"]))

        if extracted.get("topics_to_avoid"):
            existing = strategy.topics_to_avoid or []
            strategy.topics_to_avoid = list(dict.fromkeys(existing + extracted["topics_to_avoid"]))

        if extracted.get("platforms"):
            existing = strategy.platforms or []
            strategy.platforms = list(dict.fromkeys(existing + extracted["platforms"]))

        # Handle hashtags
        if extracted.get("hashtags_primary") or extracted.get("hashtags_secondary"):
            existing_sets = strategy.hashtag_sets or {"primary": [], "secondary": []}
            if extracted.get("hashtags_primary"):
                existing_sets["primary"] = list(dict.fromkeys(
                    existing_sets.get("primary", []) + extracted["hashtags_primary"]
                ))
            if extracted.get("hashtags_secondary"):
                existing_sets["secondary"] = list(dict.fromkeys(
                    existing_sets.get("secondary", []) + extracted["hashtags_secondary"]
                ))
            strategy.hashtag_sets = existing_sets

        if extracted.get("additional_notes"):
            if strategy.additional_notes:
                strategy.additional_notes += "\n\n" + extracted["additional_notes"]
            else:
                strategy.additional_notes = extracted["additional_notes"]

    db.commit()

    return JSONResponse({
        "success": True,
        "file_id": strategy_file.id,
        "filename": file.filename,
        "extracted": extracted
    })


@app.post("/clients/{client_id}/onboarding/save-strategy")
async def save_onboarding_strategy(
    request: Request,
    client_id: int,
    db: Session = Depends(get_db)
):
    """Save strategy during onboarding"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    form_data = await request.form()

    strategy = client.strategy
    if not strategy:
        strategy = Strategy(client_id=client_id)
        db.add(strategy)

    # Update strategy fields
    strategy.brand_voice = form_data.get("brand_voice", "")
    strategy.tone_keywords = [k.strip() for k in form_data.get("tone_keywords", "").split(",") if k.strip()]
    strategy.content_pillars = [p.strip() for p in form_data.get("content_pillars", "").split(",") if p.strip()]
    strategy.target_audience = form_data.get("target_audience", "")
    strategy.audience_pain_points = [p.strip() for p in form_data.get("audience_pain_points", "").split(",") if p.strip()]
    strategy.platforms = [p.strip() for p in form_data.getlist("platforms")]
    strategy.industry = form_data.get("industry", "")
    strategy.unique_selling_points = [u.strip() for u in form_data.get("unique_selling_points", "").split(",") if u.strip()]
    strategy.key_messages = [m.strip() for m in form_data.get("key_messages", "").split("\n") if m.strip()]
    strategy.topics_to_avoid = [t.strip() for t in form_data.get("topics_to_avoid", "").split(",") if t.strip()]
    strategy.additional_notes = form_data.get("additional_notes", "")

    # Parse hashtag sets
    primary_hashtags = [h.strip().replace("#", "") for h in form_data.get("primary_hashtags", "").split(",") if h.strip()]
    secondary_hashtags = [h.strip().replace("#", "") for h in form_data.get("secondary_hashtags", "").split(",") if h.strip()]
    strategy.hashtag_sets = {"primary": primary_hashtags, "secondary": secondary_hashtags}

    # Update onboarding step
    client.onboarding_step = 2

    db.commit()

    return RedirectResponse(f"/clients/{client_id}/onboarding", status_code=303)


@app.post("/clients/{client_id}/onboarding/complete")
async def complete_onboarding(
    client_id: int,
    db: Session = Depends(get_db)
):
    """Mark onboarding as complete"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    client.onboarding_status = OnboardingStatus.COMPLETED
    db.commit()

    return RedirectResponse(f"/clients/{client_id}", status_code=303)


@app.post("/clients/{client_id}/onboarding/skip")
async def skip_onboarding(
    client_id: int,
    db: Session = Depends(get_db)
):
    """Skip onboarding and go directly to client page"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    client.onboarding_status = OnboardingStatus.COMPLETED
    db.commit()

    return RedirectResponse(f"/clients/{client_id}", status_code=303)


@app.delete("/clients/{client_id}/onboarding/files/{file_id}")
async def delete_strategy_file(
    client_id: int,
    file_id: int,
    db: Session = Depends(get_db)
):
    """Delete an uploaded strategy file"""
    strategy_file = db.query(StrategyFile).filter(
        StrategyFile.id == file_id,
        StrategyFile.client_id == client_id
    ).first()

    if not strategy_file:
        raise HTTPException(status_code=404, detail="File not found")

    # Delete physical file
    file_path = BASE_DIR / strategy_file.file_path.lstrip("/")
    if file_path.exists():
        file_path.unlink()

    db.delete(strategy_file)
    db.commit()

    return JSONResponse({"success": True})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
