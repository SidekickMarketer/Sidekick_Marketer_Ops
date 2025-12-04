import os
import httpx
from typing import Optional
from datetime import datetime

METRICOOL_BASE_URL = "https://app.metricool.com/api"


def get_headers():
    """Get auth headers for Metricool API"""
    token = os.getenv("METRICOOL_USER_TOKEN")
    if not token:
        return None
    return {"X-Mc-Auth": token}


def get_user_id():
    """Get user ID from environment"""
    return os.getenv("METRICOOL_USER_ID")


async def get_brands() -> list[dict]:
    """
    Get all brands/accounts managed in Metricool.
    Each brand has a blogId that we use to associate with our clients.
    """
    headers = get_headers()
    user_id = get_user_id()

    if not headers or not user_id:
        return [{"error": "Metricool credentials not configured"}]

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{METRICOOL_BASE_URL}/admin/simpleProfiles",
                params={"userId": user_id},
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return [{"error": f"Failed to fetch brands: {str(e)}"}]


async def normalize_media(media_url: str) -> Optional[str]:
    """
    Normalize a media URL through Metricool to get a mediaId.
    Required before scheduling posts with media.
    """
    headers = get_headers()
    if not headers:
        return None

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{METRICOOL_BASE_URL}/actions/normalize/image/url",
                params={"url": media_url},
                headers=headers
            )
            response.raise_for_status()
            return response.json().get("mediaId")
        except Exception as e:
            print(f"Media normalization failed: {e}")
            return None


async def schedule_post(
    blog_id: str,
    caption: str,
    platform: str,
    scheduled_datetime: datetime,
    timezone: str = "America/New_York",
    media_id: Optional[str] = None
) -> dict:
    """
    Schedule a post in Metricool.

    Args:
        blog_id: The Metricool brand/blog ID
        caption: The post caption text
        platform: Platform name (instagram, facebook, etc.)
        scheduled_datetime: When to publish
        timezone: Timezone for scheduling
        media_id: Optional media ID from normalize_media()

    Returns:
        Response from Metricool API
    """
    headers = get_headers()
    user_id = get_user_id()

    if not headers or not user_id:
        return {"error": "Metricool credentials not configured"}

    # Map our platform names to Metricool's
    platform_map = {
        "instagram": "INSTAGRAM",
        "facebook": "FACEBOOK",
        "linkedin": "LINKEDIN",
        "tiktok": "TIKTOK",
        "twitter": "TWITTER",
        "gbp": "GOOGLE_BUSINESS"
    }

    metricool_platform = platform_map.get(platform.lower(), platform.upper())

    # Build the post payload
    payload = {
        "blogId": blog_id,
        "userId": user_id,
        "text": caption,
        "networks": [metricool_platform],
        "publicationDate": {
            "dateTime": scheduled_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
            "timezone": timezone
        }
    }

    if media_id:
        payload["mediaIds"] = [media_id]

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{METRICOOL_BASE_URL}/v2/scheduler/posts",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"Scheduling failed: {e.response.text}"}
        except Exception as e:
            return {"error": f"Scheduling failed: {str(e)}"}


async def get_scheduled_posts(blog_id: str) -> list[dict]:
    """Get all scheduled posts for a brand"""
    headers = get_headers()
    user_id = get_user_id()

    if not headers or not user_id:
        return [{"error": "Metricool credentials not configured"}]

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{METRICOOL_BASE_URL}/v2/scheduler/posts",
                params={"blogId": blog_id, "userId": user_id},
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return [{"error": f"Failed to fetch posts: {str(e)}"}]


async def delete_scheduled_post(post_id: str) -> dict:
    """Delete a scheduled post"""
    headers = get_headers()

    if not headers:
        return {"error": "Metricool credentials not configured"}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(
                f"{METRICOOL_BASE_URL}/v2/scheduler/posts/{post_id}",
                headers=headers
            )
            response.raise_for_status()
            return {"success": True}
        except Exception as e:
            return {"error": f"Delete failed: {str(e)}"}


def validate_metricool_config() -> dict:
    """Check if Metricool is properly configured"""
    token = os.getenv("METRICOOL_USER_TOKEN")
    user_id = os.getenv("METRICOOL_USER_ID")

    return {
        "configured": bool(token and user_id),
        "has_token": bool(token),
        "has_user_id": bool(user_id)
    }
