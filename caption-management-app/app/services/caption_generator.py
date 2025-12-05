import os
from anthropic import Anthropic
from typing import Optional
import json

from .expert_frameworks import (
    build_enhanced_caption_prompt,
    get_experts_for_client,
    INDUSTRY_EXPERT_MAPPING,
    PLATFORM_BENCHMARKS
)

client = None

def get_anthropic_client():
    global client
    if client is None:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if api_key:
            client = Anthropic(api_key=api_key)
    return client


def get_available_industries() -> list[str]:
    """Return list of industries with mapped expert councils."""
    return list(INDUSTRY_EXPERT_MAPPING.keys())


def generate_captions_with_full_context(
    client_name: str,
    profile_markdown: str,
    master_strategy_markdown: Optional[str],
    platform_strategy_markdown: Optional[str],
    previous_posts: list[str],
    num_captions: int = 5,
    platform: str = "instagram",
    content_theme: Optional[str] = None,
    specific_topic: Optional[str] = None,
    edited_examples: Optional[list[dict]] = None
) -> list[dict]:
    """
    Generate captions using FULL profile and strategy documents.
    
    This is the enhanced generator that uses all the rich context from your
    Claude Skills outputs (CLIENT_PROFILE.md, MASTER_STRATEGY.md, platform strategies).
    
    Args:
        client_name: Name of the client
        profile_markdown: Full 00_CLIENT_PROFILE.md content
        master_strategy_markdown: Full 00_MASTER_STRATEGY.md content (optional)
        platform_strategy_markdown: Full platform-specific strategy (e.g., 00_IG_STRATEGY.md)
        previous_posts: List of previous caption texts to avoid duplication
        num_captions: Number of captions to generate
        platform: Target platform (instagram, facebook, gbp, linkedin, tiktok)
        content_theme: Optional content pillar to focus on
        specific_topic: Optional specific topic to address
        edited_examples: List of {original, edited} dicts showing how user refined captions
    """
    anthropic = get_anthropic_client()
    if not anthropic:
        return [{"error": "Anthropic API key not configured"}]

    # Get platform specs
    platform_specs = PLATFORM_BENCHMARKS.get(platform.lower(), PLATFORM_BENCHMARKS.get("instagram", {}))
    
    # Build the comprehensive prompt with full context
    prompt = f"""You are an expert social media copywriter for {client_name}.

You have access to their COMPLETE strategy documentation. Use ALL of this context to create perfectly on-brand captions.

# COMPLETE CLIENT PROFILE

{profile_markdown}

---

"""

    # Add master strategy if available
    if master_strategy_markdown:
        prompt += f"""# MASTER SOCIAL MEDIA STRATEGY

{master_strategy_markdown}

---

"""

    # Add platform-specific strategy if available
    if platform_strategy_markdown:
        prompt += f"""# {platform.upper()} PLATFORM STRATEGY

{platform_strategy_markdown}

---

"""

    # Add platform specs
    prompt += f"""# PLATFORM SPECIFICATIONS: {platform.upper()}

"""
    if "caption_length" in platform_specs:
        cl = platform_specs["caption_length"]
        prompt += f"""**Caption Length:**
- Optimal: {cl.get('optimal', 'N/A')}
- Truncation point: {cl.get('truncation_point', 'N/A')}

"""
    
    if "hashtags" in platform_specs:
        ht = platform_specs["hashtags"]
        prompt += f"""**Hashtags:** {ht.get('quantity', 'N/A')}
"""
        if "mix" in ht:
            prompt += f"- Mix: {ht['mix']}\n"
        prompt += "\n"

    # Add previous posts for deduplication
    prompt += f"""---

# PREVIOUS POSTS (DO NOT DUPLICATE THEMES OR HOOKS)

{chr(10).join([f"- {post[:200]}..." if len(post) > 200 else f"- {post}" for post in previous_posts[-20:]]) if previous_posts else "No previous posts yet."}

---

"""

    # Add learning from edited examples
    if edited_examples and len(edited_examples) > 0:
        prompt += """# LEARN FROM THESE REFINEMENTS

The following shows how AI-generated captions were refined by the user. 
**Study these patterns carefully and apply the same refinements to your output.**

"""
        for i, example in enumerate(edited_examples[:5], 1):  # Max 5 examples
            prompt += f"""## Example {i}

**Original (AI generated):**
{example.get('original', '')[:500]}

**Refined (user edited):**
{example.get('edited', '')[:500]}

---

"""
        prompt += """**Apply these refinement patterns to ALL captions you generate.**

---

"""

    prompt += f"""# GENERATION TASK

Generate exactly {num_captions} captions for {platform.upper()}.

"""

    if content_theme:
        prompt += f"""**Content Pillar Focus:** {content_theme}
Use the pillar-specific hooks, examples, and CTAs from the strategy documents above.

"""

    if specific_topic:
        prompt += f"""**Specific Topic:** {specific_topic}

"""

    prompt += """## CRITICAL REQUIREMENTS

1. **Use the EXACT brand voice** described in the profile - match tone, phrases, and personality
2. **Follow the hook examples** from the strategy documents - adapt them, don't invent new patterns
3. **Use the hashtag sets** defined in the strategy - don't create new ones
4. **Match caption length** to platform specs and strategy guidelines
5. **Include CTAs** that match the brand's preferred style
6. **Reference specific details** from the profile (instructor names, FAQs, services, etc.) when relevant
7. **Avoid topics** listed in the guidelines
8. **Match the quarterly theme** if applicable to current timing

## OUTPUT FORMAT

Return a JSON array with exactly """ + str(num_captions) + """ objects:

```json
[
  {
    "caption": "The full caption text (following brand voice exactly)",
    "hashtags": ["hashtags", "from", "strategy", "docs"],
    "hook": "The first line/scroll-stopper (use patterns from strategy)",
    "content_pillar": "Which pillar this falls under",
    "cta": "The call-to-action used",
    "format_recommendation": "single_image|carousel|reel",
    "reasoning": "How this applies the client's specific strategy"
  }
]
```

Generate {num_captions} unique, perfectly on-brand captions now. Every caption should sound like it came directly from {client_name}'s internal team.""".replace("{num_captions}", str(num_captions)).replace("{client_name}", client_name)

    try:
        response = anthropic.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract JSON from response
        response_text = response.content[0].text

        # Try to parse JSON from the response
        if "```json" in response_text:
            json_start = response_text.find("```json") + 7
            json_end = response_text.find("```", json_start)
            json_str = response_text[json_start:json_end].strip()
        elif "```" in response_text:
            json_start = response_text.find("```") + 3
            json_end = response_text.find("```", json_start)
            json_str = response_text[json_start:json_end].strip()
        else:
            json_start = response_text.find("[")
            json_end = response_text.rfind("]") + 1
            json_str = response_text[json_start:json_end]

        captions = json.loads(json_str)
        return captions

    except Exception as e:
        return [{"error": f"Generation failed: {str(e)}"}]


def generate_captions(
    strategy: dict,
    previous_posts: list[str],
    num_captions: int = 5,
    platform: str = "instagram",
    content_theme: Optional[str] = None,
    specific_topic: Optional[str] = None,
    use_expert_frameworks: bool = True
) -> list[dict]:
    """
    Generate captions based on client strategy, avoiding duplication with previous posts.

    Uses selective expert frameworks (Schwartz, Ogilvy, Cialdini, etc.) based on
    client industry to produce higher-quality, on-brand captions.

    Args:
        strategy: Client strategy dict with brand_voice, content_pillars, etc.
        previous_posts: List of previous caption texts to avoid duplication
        num_captions: Number of captions to generate
        platform: Target platform (instagram, facebook, linkedin, tiktok)
        content_theme: Optional content pillar to focus on
        specific_topic: Optional specific topic to address
        use_expert_frameworks: Whether to use the enhanced expert council system
    """
    anthropic = get_anthropic_client()
    if not anthropic:
        return [{"error": "Anthropic API key not configured"}]

    # Use the enhanced expert-driven prompt
    if use_expert_frameworks:
        prompt = build_enhanced_caption_prompt(
            strategy=strategy,
            previous_posts=previous_posts,
            num_captions=num_captions,
            platform=platform,
            content_theme=content_theme,
            specific_topic=specific_topic
        )

        # Log which experts are being used (helpful for debugging)
        industry = strategy.get('industry', 'default')
        experts = get_experts_for_client(industry, content_theme)
        expert_names = [e['name'] for e in experts['primary']]
        print(f"[Caption Generator] Using expert council: {', '.join(expert_names)} for {industry}")
    else:
        # Fallback to basic prompt (kept for backwards compatibility)
        prompt = f"""You are an expert social media copywriter for an agency. Generate {num_captions} unique social media captions for {platform}.

## CLIENT STRATEGY

**Brand Voice:** {strategy.get('brand_voice', 'Professional and friendly')}
**Tone Keywords:** {', '.join(strategy.get('tone_keywords', ['professional', 'engaging']))}
**Content Pillars:** {', '.join(strategy.get('content_pillars', ['education', 'engagement']))}
**Target Audience:** {strategy.get('target_audience', 'General business audience')}
**Key Messages to Reinforce:** {', '.join(strategy.get('key_messages', []))}
**Industry:** {strategy.get('industry', 'General')}
**Unique Selling Points:** {', '.join(strategy.get('unique_selling_points', []))}

## PREVIOUS POSTS (DO NOT DUPLICATE)
{chr(10).join([f"- {post[:200]}..." for post in previous_posts[-20:]]) if previous_posts else "No previous posts yet."}

## OUTPUT FORMAT
Return a JSON array with {num_captions} caption objects with: caption, hashtags, content_pillar, hook, cta, reasoning.
"""

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
