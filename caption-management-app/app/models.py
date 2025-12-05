from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, JSON, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
import uuid

from .database import Base


class PostStatus(str, enum.Enum):
    DRAFT = "draft"
    INTERNAL_REVIEW = "internal_review"
    CLIENT_REVIEW = "client_review"
    REVISION_REQUESTED = "revision_requested"
    APPROVED = "approved"
    SCHEDULED = "scheduled"
    POSTED = "posted"


class Platform(str, enum.Enum):
    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"
    LINKEDIN = "linkedin"
    TIKTOK = "tiktok"
    TWITTER = "twitter"
    GBP = "gbp"  # Google Business Profile


class OnboardingStatus(str, enum.Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True)  # URL-friendly name
    review_token = Column(String(64), unique=True, index=True)  # For client portal access

    # Metricool integration
    metricool_blog_id = Column(String(50), nullable=True)

    # Onboarding tracking
    onboarding_status = Column(String(50), default=OnboardingStatus.NOT_STARTED)
    onboarding_step = Column(Integer, default=1)  # Current step in onboarding

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    # Relationships
    strategy = relationship("Strategy", back_populates="client", uselist=False, cascade="all, delete-orphan")
    posts = relationship("Post", back_populates="client", cascade="all, delete-orphan")
    previous_posts = relationship("PreviousPost", back_populates="client", cascade="all, delete-orphan")
    photos = relationship("Photo", back_populates="client", cascade="all, delete-orphan")
    profile_audits = relationship("ProfileAudit", back_populates="client", cascade="all, delete-orphan")
    strategy_files = relationship("StrategyFile", back_populates="client", cascade="all, delete-orphan")


class Strategy(Base):
    __tablename__ = "strategies"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), unique=True)

    # Brand voice
    brand_voice = Column(Text)  # e.g., "Professional but approachable, uses humor sparingly"
    tone_keywords = Column(JSON)  # e.g., ["friendly", "expert", "conversational"]

    # Content pillars
    content_pillars = Column(JSON)  # e.g., ["education", "behind-the-scenes", "testimonials", "tips"]

    # Audience
    target_audience = Column(Text)  # Description of ideal customer
    audience_pain_points = Column(JSON)  # What problems they solve

    # Platform-specific
    platforms = Column(JSON)  # Which platforms this client uses
    hashtag_sets = Column(JSON)  # e.g., {"primary": ["#marketing", "#business"], "secondary": [...]}

    # Content guidelines
    topics_to_avoid = Column(JSON)  # Things not to talk about
    competitors_to_avoid = Column(JSON)  # Don't mention these
    key_messages = Column(JSON)  # Core messages to reinforce
    cta_preferences = Column(JSON)  # Preferred calls-to-action

    # Additional context
    industry = Column(String(100))
    unique_selling_points = Column(JSON)
    additional_notes = Column(Text)

    # Timestamps
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship
    client = relationship("Client", back_populates="strategy")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))

    # Content
    caption = Column(Text, nullable=False)
    hashtags = Column(Text)
    platform = Column(String(50))  # instagram, facebook, etc.

    # Media
    photo_id = Column(Integer, ForeignKey("photos.id"), nullable=True)

    # Scheduling
    scheduled_date = Column(DateTime, nullable=True)
    batch_name = Column(String(100))  # e.g., "Week of Dec 9" or "December 2024"

    # Status tracking
    status = Column(String(50), default=PostStatus.DRAFT)

    # Client feedback
    client_comment = Column(Text, nullable=True)
    revision_notes = Column(Text, nullable=True)

    # Metricool integration
    metricool_post_id = Column(String(100), nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    approved_at = Column(DateTime, nullable=True)
    posted_at = Column(DateTime, nullable=True)

    # Relationships
    client = relationship("Client", back_populates="posts")
    photo = relationship("Photo", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class PreviousPost(Base):
    """Historical posts to avoid duplication"""
    __tablename__ = "previous_posts"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))

    caption = Column(Text)
    platform = Column(String(50))
    posted_date = Column(DateTime)

    # For similarity checking
    caption_embedding = Column(JSON, nullable=True)  # Store embedding for similarity search

    client = relationship("Client", back_populates="previous_posts")


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))

    filename = Column(String(255))
    original_filename = Column(String(255))
    file_path = Column(String(500))
    thumbnail_path = Column(String(500), nullable=True)

    # Metadata
    description = Column(Text, nullable=True)  # For AI matching
    tags = Column(JSON, nullable=True)  # e.g., ["team", "office", "product"]

    # Timestamps
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    client = relationship("Client", back_populates="photos")
    posts = relationship("Post", back_populates="photo")


class Comment(Base):
    """Comments on posts during review process"""
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))

    author_type = Column(String(20))  # "agency" or "client"
    author_name = Column(String(100))
    content = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    post = relationship("Post", back_populates="comments")


class Batch(Base):
    """Group posts for review"""
    __tablename__ = "batches"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))

    name = Column(String(100))  # e.g., "Week of Dec 9, 2024"
    review_link = Column(String(64), unique=True, index=True)  # Unique link for client review

    status = Column(String(50), default="draft")  # draft, sent_for_review, approved, scheduled

    created_at = Column(DateTime, default=datetime.utcnow)
    sent_at = Column(DateTime, nullable=True)
    approved_at = Column(DateTime, nullable=True)


class ProfileAudit(Base):
    """Profile optimization audit checklist per platform"""
    __tablename__ = "profile_audits"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    platform = Column(String(50))  # facebook, instagram, gbp, linkedin

    # Store checklist items as JSON: {"item_key": {"checked": bool, "notes": str}}
    checklist_data = Column(JSON, default=dict)

    # Computed score (percentage complete)
    score = Column(Integer, default=0)  # 0-100

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_audited_at = Column(DateTime, nullable=True)

    # Relationship
    client = relationship("Client", back_populates="profile_audits")


class StrategyFile(Base):
    """Uploaded strategy documents for reference"""
    __tablename__ = "strategy_files"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))

    filename = Column(String(255))
    original_filename = Column(String(255))
    file_path = Column(String(500))
    file_type = Column(String(50))  # pdf, docx, txt, etc.

    # Extracted content summary
    extracted_summary = Column(Text, nullable=True)

    # Whether this file was processed
    processed = Column(Boolean, default=False)

    # Timestamps
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    # Relationship
    client = relationship("Client", back_populates="strategy_files")


# Define the audit checklists for each platform
AUDIT_CHECKLISTS = {
    "facebook": {
        "name": "Facebook Page",
        "items": [
            {"key": "page_name", "label": "Page name matches business exactly", "critical": True},
            {"key": "vanity_url", "label": "Vanity URL set (facebook.com/yourbusiness)", "critical": True},
            {"key": "about_section", "label": "About section with keywords (155 char intro)", "critical": True},
            {"key": "full_description", "label": "Full description with service keywords", "critical": False},
            {"key": "category", "label": "Category selected correctly", "critical": True},
            {"key": "cta_button", "label": "CTA button configured (Book, Call, etc.)", "critical": True},
            {"key": "contact_phone", "label": "Phone number added", "critical": True},
            {"key": "contact_email", "label": "Email added", "critical": False},
            {"key": "contact_website", "label": "Website URL added", "critical": True},
            {"key": "location", "label": "Location/service area set", "critical": True},
            {"key": "hours", "label": "Hours of operation set", "critical": True},
            {"key": "profile_photo", "label": "Profile photo (logo, 170x170)", "critical": True},
            {"key": "cover_photo", "label": "Cover photo (current, 820x312)", "critical": True},
            {"key": "services_listed", "label": "Services/Products listed", "critical": False},
        ]
    },
    "instagram": {
        "name": "Instagram Profile",
        "items": [
            {"key": "username", "label": "Username is searchable/brandable", "critical": True},
            {"key": "name_field", "label": "Name field has keywords (not just brand name)", "critical": True},
            {"key": "bio_value_prop", "label": "Bio has clear value proposition", "critical": True},
            {"key": "bio_cta", "label": "Bio has call-to-action", "critical": True},
            {"key": "bio_length", "label": "Bio optimized (150 chars max)", "critical": False},
            {"key": "link_in_bio", "label": "Link in bio (or Linktree)", "critical": True},
            {"key": "contact_buttons", "label": "Contact buttons enabled", "critical": True},
            {"key": "category", "label": "Category selected", "critical": True},
            {"key": "business_account", "label": "Business/Creator account (not personal)", "critical": True},
            {"key": "profile_photo", "label": "Profile photo clear and on-brand", "critical": True},
            {"key": "highlights", "label": "Highlights organized with covers", "critical": False},
            {"key": "highlight_services", "label": "Highlight for services/offerings", "critical": False},
            {"key": "highlight_testimonials", "label": "Highlight for testimonials/reviews", "critical": False},
        ]
    },
    "gbp": {
        "name": "Google Business Profile",
        "items": [
            {"key": "business_name", "label": "Business name exact match (no keyword stuffing)", "critical": True},
            {"key": "primary_category", "label": "Primary category selected correctly", "critical": True},
            {"key": "secondary_categories", "label": "Secondary categories added", "critical": False},
            {"key": "description", "label": "Description with local keywords (750 chars)", "critical": True},
            {"key": "services_listed", "label": "All services listed with descriptions", "critical": True},
            {"key": "products", "label": "Products added (if applicable)", "critical": False},
            {"key": "phone", "label": "Phone number correct", "critical": True},
            {"key": "website", "label": "Website URL correct", "critical": True},
            {"key": "address", "label": "Address verified", "critical": True},
            {"key": "service_area", "label": "Service area defined (if applicable)", "critical": False},
            {"key": "hours", "label": "Hours up to date", "critical": True},
            {"key": "special_hours", "label": "Special/holiday hours set", "critical": False},
            {"key": "attributes", "label": "Attributes selected (accessibility, amenities)", "critical": False},
            {"key": "photos_exterior", "label": "Exterior photos uploaded", "critical": True},
            {"key": "photos_interior", "label": "Interior photos uploaded", "critical": True},
            {"key": "photos_team", "label": "Team photos uploaded", "critical": False},
            {"key": "photos_products", "label": "Product/service photos uploaded", "critical": True},
            {"key": "photos_recent", "label": "Photos uploaded in last 30 days", "critical": True},
            {"key": "qa_seeded", "label": "Q&A section populated with common questions", "critical": False},
            {"key": "reviews_responded", "label": "All reviews responded to", "critical": True},
            {"key": "posts_active", "label": "Posts active (within last 7 days)", "critical": True},
        ]
    },
    "linkedin": {
        "name": "LinkedIn Company Page",
        "items": [
            {"key": "company_name", "label": "Company name correct", "critical": True},
            {"key": "tagline", "label": "Tagline with keywords (120 chars)", "critical": True},
            {"key": "about_section", "label": "About section complete with keywords", "critical": True},
            {"key": "website", "label": "Website URL added", "critical": True},
            {"key": "industry", "label": "Industry selected", "critical": True},
            {"key": "company_size", "label": "Company size set", "critical": False},
            {"key": "headquarters", "label": "Headquarters location set", "critical": True},
            {"key": "logo", "label": "Logo uploaded (300x300)", "critical": True},
            {"key": "cover_image", "label": "Cover image uploaded (1128x191)", "critical": True},
            {"key": "cta_button", "label": "Custom CTA button configured", "critical": False},
            {"key": "specialties", "label": "Specialties/keywords added", "critical": True},
            {"key": "hashtags", "label": "Branded hashtags in About", "critical": False},
        ]
    }
}
