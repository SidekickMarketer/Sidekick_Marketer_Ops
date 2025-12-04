import os
from anthropic import Anthropic
from typing import Optional
import json

client = None

def get_anthropic_client():
    global client
    if client is None:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if api_key:
            client = Anthropic(api_key=api_key)
    return client


def generate_captions(
    strategy: dict,
    previous_posts: list[str],
    num_captions: int = 5,
    platform: str = "instagram",
    content_theme: Optional[str] = None,
    specific_topic: Optional[str] = None
) -> list[dict]:
    """
    Generate captions based on client strategy, avoiding duplication with previous posts.
    """
    anthropic = get_anthropic_client()
    if not anthropic:
        return [{"error": "Anthropic API key not configured"}]

    # Build the prompt
    prompt = f"""You are an expert social media copywriter for an agency. Generate {num_captions} unique social media captions for {platform}.

## CLIENT STRATEGY

**Brand Voice:** {strategy.get('brand_voice', 'Professional and friendly')}

**Tone Keywords:** {', '.join(strategy.get('tone_keywords', ['professional', 'engaging']))}

**Content Pillars:** {', '.join(strategy.get('content_pillars', ['education', 'engagement']))}

**Target Audience:** {strategy.get('target_audience', 'General business audience')}

**Key Messages to Reinforce:** {', '.join(strategy.get('key_messages', []))}

**Industry:** {strategy.get('industry', 'General')}

**Unique Selling Points:** {', '.join(strategy.get('unique_selling_points', []))}

## PLATFORM GUIDELINES

Platform: {platform}
{"- Instagram: 2,200 character max, use line breaks, emoji-friendly, 20-30 hashtags work well" if platform == "instagram" else ""}
{"- Facebook: Can be longer form, less hashtags (3-5), more conversational" if platform == "facebook" else ""}
{"- LinkedIn: Professional tone, industry insights, minimal hashtags (3-5), thought leadership" if platform == "linkedin" else ""}
{"- TikTok: Casual, trendy, hook in first line, relevant hashtags" if platform == "tiktok" else ""}

## CONTENT DIRECTION
{f"Theme/Pillar to focus on: {content_theme}" if content_theme else "Mix of content pillars"}
{f"Specific topic to address: {specific_topic}" if specific_topic else ""}

## PREVIOUS POSTS (DO NOT DUPLICATE OR BE TOO SIMILAR)
{chr(10).join([f"- {post[:200]}..." if len(post) > 200 else f"- {post}" for post in previous_posts[-20:]]) if previous_posts else "No previous posts yet."}

## TOPICS/PHRASES TO AVOID
{', '.join(strategy.get('topics_to_avoid', [])) if strategy.get('topics_to_avoid') else 'None specified'}

## OUTPUT FORMAT

Return a JSON array with exactly {num_captions} caption objects. Each object should have:
- "caption": The main caption text (without hashtags)
- "hashtags": Array of relevant hashtags (without # symbol)
- "content_pillar": Which pillar this falls under
- "hook": The opening line/hook
- "cta": The call-to-action used
- "reasoning": Brief explanation of why this caption works for the strategy

Example format:
```json
[
  {{
    "caption": "The caption text here...",
    "hashtags": ["marketing", "business", "growth"],
    "content_pillar": "education",
    "hook": "The opening hook",
    "cta": "Save this for later!",
    "reasoning": "This works because..."
  }}
]
```

Generate {num_captions} unique, on-brand captions now:"""

    try:
        response = anthropic.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract JSON from response
        response_text = response.content[0].text

        # Try to parse JSON from the response
        # Handle both direct JSON and markdown-wrapped JSON
        if "```json" in response_text:
            json_start = response_text.find("```json") + 7
            json_end = response_text.find("```", json_start)
            json_str = response_text[json_start:json_end].strip()
        elif "```" in response_text:
            json_start = response_text.find("```") + 3
            json_end = response_text.find("```", json_start)
            json_str = response_text[json_start:json_end].strip()
        else:
            # Try to find JSON array directly
            json_start = response_text.find("[")
            json_end = response_text.rfind("]") + 1
            json_str = response_text[json_start:json_end]

        captions = json.loads(json_str)
        return captions

    except Exception as e:
        return [{"error": f"Generation failed: {str(e)}"}]


def check_similarity(new_caption: str, previous_posts: list[str], threshold: float = 0.7) -> dict:
    """
    Check if a new caption is too similar to previous posts.
    Returns similarity info.
    """
    # Simple word overlap check (could be enhanced with embeddings later)
    new_words = set(new_caption.lower().split())

    most_similar = None
    highest_similarity = 0

    for post in previous_posts:
        post_words = set(post.lower().split())
        if not post_words:
            continue

        overlap = len(new_words & post_words)
        similarity = overlap / max(len(new_words), len(post_words))

        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar = post

    return {
        "is_similar": highest_similarity > threshold,
        "similarity_score": highest_similarity,
        "similar_to": most_similar[:100] + "..." if most_similar and len(most_similar) > 100 else most_similar
    }


def suggest_photo_match(caption: str, photo_descriptions: list[dict]) -> list[dict]:
    """
    Suggest photos that might match a caption based on descriptions/tags.
    """
    anthropic = get_anthropic_client()
    if not anthropic or not photo_descriptions:
        return []

    prompt = f"""Given this social media caption:

"{caption}"

And these available photos with their descriptions/tags:

{json.dumps(photo_descriptions, indent=2)}

Which photos would best match this caption? Return a JSON array of photo IDs ranked by relevance, with reasoning:

```json
[
  {{"photo_id": 1, "relevance_score": 0.9, "reasoning": "Why this photo fits"}},
  ...
]
```

Only include photos with relevance_score > 0.5. Return empty array if no good matches."""

    try:
        response = anthropic.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = response.content[0].text
        if "```json" in response_text:
            json_start = response_text.find("```json") + 7
            json_end = response_text.find("```", json_start)
            json_str = response_text[json_start:json_end].strip()
        else:
            json_start = response_text.find("[")
            json_end = response_text.rfind("]") + 1
            json_str = response_text[json_start:json_end]

        return json.loads(json_str)
    except:
        return []
