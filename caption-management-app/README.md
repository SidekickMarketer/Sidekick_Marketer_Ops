# Caption Management App

A web application for agencies to manage social media caption creation, client approval, and publishing to Metricool.

## Features

- **Client Profiles**: Manage multiple clients with their brand strategies
- **AI Caption Generation**: Generate on-brand captions using Claude AI
- **Deduplication**: Automatically avoids repeating previous content
- **Photo Library**: Upload and manage photos per client
- **Client Review Portal**: Clean interface for clients to approve content
- **Metricool Integration**: Push approved content directly to Metricool for scheduling

## Setup

### 1. Install Dependencies

```bash
cd caption-management-app
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add:
- `ANTHROPIC_API_KEY`: Your Claude API key (for caption generation)
- `METRICOOL_USER_TOKEN`: Your Metricool API token (from Settings > API)
- `METRICOOL_USER_ID`: Your Metricool user ID (from URL)
- `SECRET_KEY`: A random string for session security

### 3. Run the App

```bash
python run.py
```

Or:
```bash
uvicorn app.main:app --reload
```

Open http://localhost:8000

## Workflow

### Agency Side

1. **Create Client**: Add a new client profile
2. **Set Strategy**: Define brand voice, content pillars, target audience, etc.
3. **Upload Photos**: Add photos to the client's library
4. **Generate Captions**: AI creates captions based on strategy
5. **Review & Edit**: Refine captions, assign photos, set dates
6. **Send for Review**: Move posts to client review status
7. **Handle Feedback**: Address any client change requests
8. **Publish**: Push approved posts to Metricool

### Client Side

1. Client receives review link (e.g., `/review/abc123`)
2. Reviews each post with caption and photo
3. Either approves or requests changes with comments
4. Agency gets notified of any feedback

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Dashboard |
| GET | `/clients` | List clients |
| POST | `/clients` | Create client |
| GET | `/clients/{id}` | Client detail |
| GET | `/clients/{id}/strategy` | Edit strategy |
| POST | `/clients/{id}/generate` | Generate captions |
| GET | `/clients/{id}/photos` | Photo library |
| POST | `/clients/{id}/photos` | Upload photo |
| GET | `/posts/{id}` | Edit post |
| POST | `/posts/{id}/status` | Update status |
| POST | `/posts/{id}/schedule` | Push to Metricool |
| GET | `/review/{token}` | Client review portal |

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite (SQLAlchemy ORM)
- **Frontend**: Jinja2 templates + Tailwind CSS + Alpine.js
- **AI**: Anthropic Claude API
- **Publishing**: Metricool API

## Directory Structure

```
caption-management-app/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI routes
│   ├── models.py        # Database models
│   ├── database.py      # DB connection
│   └── services/
│       ├── caption_generator.py  # AI caption generation
│       └── metricool.py          # Metricool API
├── templates/
│   ├── base.html
│   ├── agency/          # Agency dashboard templates
│   └── client/          # Client review templates
├── static/
│   └── uploads/         # Photo storage
├── requirements.txt
├── .env.example
└── run.py
```

## Metricool Setup

1. Get an Advanced or Custom Metricool plan (API access required)
2. Go to Settings > API in Metricool
3. Copy your API token
4. Find your user ID in the URL: `app.metricool.com/...?userId=XXXXX`
5. For each client, find their blog ID: `app.metricool.com/...?blogId=XXXXX`
6. Link clients to their Metricool blog ID in the app
