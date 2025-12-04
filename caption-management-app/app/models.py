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


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True)  # URL-friendly name
    review_token = Column(String(64), unique=True, index=True)  # For client portal access

    # Metricool integration
    metricool_blog_id = Column(String(50), nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    # Relationships
    strategy = relationship("Strategy", back_populates="client", uselist=False, cascade="all, delete-orphan")
    posts = relationship("Post", back_populates="client", cascade="all, delete-orphan")
    previous_posts = relationship("PreviousPost", back_populates="client", cascade="all, delete-orphan")
    photos = relationship("Photo", back_populates="client", cascade="all, delete-orphan")


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
