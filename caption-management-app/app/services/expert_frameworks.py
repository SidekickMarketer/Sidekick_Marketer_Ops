"""
Expert Council Framework for Caption Generation

This module provides the expert frameworks from your existing system,
applied selectively based on client industry and content type.

Key principle: 3-4 experts max per generation, not all at once.
"""

# =============================================================================
# EXPERT DEFINITIONS
# =============================================================================

EXPERTS = {
    # PRIMARY COPY EXPERTS
    "eugene_schwartz": {
        "name": "Eugene Schwartz",
        "specialty": "Direct Response Copy",
        "core_philosophy": "Copy cannot create desire; it can only channel existing desire",
        "key_framework": "5 Stages of Awareness",
        "awareness_stages": {
            "unaware": "They don't know they have a problem. Lead with curiosity, not solution.",
            "problem_aware": "They know the problem, not the solution. Agitate the pain.",
            "solution_aware": "They know solutions exist. Differentiate your approach.",
            "product_aware": "They know your product. Overcome objections, build trust.",
            "most_aware": "They're ready. Make the offer clear and easy."
        },
        "caption_rules": [
            "Match sophistication level to audience awareness",
            "Build curiosity progressively - don't reveal everything",
            "The first line must stop the scroll",
            "Channel existing desire, don't create new ones"
        ]
    },

    "david_ogilvy": {
        "name": "David Ogilvy",
        "specialty": "Brand Advertising",
        "core_philosophy": "The consumer isn't a moron; she is your wife",
        "key_framework": "Headline Principles",
        "headline_rules": [
            "The headline is 80% of the ad - first line is 80% of caption",
            "Include the benefit in the headline",
            "Specifics are more believable than generalities",
            "News and 'new' always work",
            "Localize when possible"
        ],
        "caption_rules": [
            "Every caption should reinforce brand positioning",
            "Research-based creativity - know your audience deeply",
            "Long copy sells if it's interesting",
            "Be specific with numbers and facts"
        ]
    },

    "joseph_sugarman": {
        "name": "Joseph Sugarman",
        "specialty": "Psychological Triggers",
        "core_philosophy": "Every element exists to get the first sentence read",
        "key_framework": "31 Psychological Triggers",
        "top_triggers": {
            "curiosity": "Open loops that demand closure",
            "story": "Humans are wired for narrative",
            "specificity": "Specific = believable",
            "fear": "Fear of missing out, fear of loss",
            "greed": "Getting more than expected",
            "exclusivity": "Not for everyone",
            "social_proof": "Others like you did this",
            "urgency": "Time pressure creates action",
            "simplicity": "Easy to understand and act"
        },
        "caption_rules": [
            "First sentence must compel second sentence",
            "Create 'seeds of curiosity' throughout",
            "Use involvement devices (questions, gaps)",
            "Make reading feel like a 'slippery slide'"
        ]
    },

    "robert_cialdini": {
        "name": "Robert Cialdini",
        "specialty": "Influence Psychology",
        "core_philosophy": "Ethical influence through understanding human psychology",
        "key_framework": "6 Principles of Influence",
        "principles": {
            "reciprocity": "Give value first, then ask",
            "commitment": "Small yeses lead to big yeses",
            "social_proof": "People follow people like them",
            "authority": "Expertise creates trust",
            "liking": "We buy from people we like",
            "scarcity": "Limited = more valuable"
        },
        "caption_rules": [
            "Embed 1-2 principles per caption (not all 6)",
            "Reciprocity: Give value before asking for engagement",
            "Social proof: Reference community, results, others",
            "Scarcity: Limited time, exclusive access"
        ]
    },

    "seth_godin": {
        "name": "Seth Godin",
        "specialty": "Permission Marketing & Tribes",
        "core_philosophy": "Marketing is no longer about the stuff you make, but the stories you tell",
        "key_framework": "Purple Cow + Tribes",
        "concepts": {
            "purple_cow": "Be remarkable or be invisible",
            "tribes": "Build community around shared beliefs",
            "permission": "Earn attention, don't demand it",
            "smallest_viable_audience": "Don't try to reach everyone"
        },
        "caption_rules": [
            "Make content worth talking about",
            "Speak to your tribe's identity",
            "Don't interrupt - be worth seeking out",
            "Remarkable > safe"
        ]
    },

    "marcus_sheridan": {
        "name": "Marcus Sheridan",
        "specialty": "They Ask You Answer",
        "core_philosophy": "Answer every question your customers have, honestly",
        "key_framework": "Big 5 Content",
        "big_5_topics": [
            "Pricing and costs",
            "Problems and negatives",
            "Comparisons",
            "Reviews",
            "Best in class"
        ],
        "caption_rules": [
            "Address real questions your audience has",
            "Be honest about limitations",
            "Compare yourself to alternatives openly",
            "Educational content builds trust"
        ]
    },

    "gary_vaynerchuk": {
        "name": "Gary Vaynerchuk",
        "specialty": "Social Media & Attention",
        "core_philosophy": "Day Trading Attention - organic social is undervalued, interest-based algorithms reward quality over follower count",
        "key_framework": "Day Trading Attention (2024)",
        "platform_rules": {
            "instagram": "Carousels for education, strong hooks, save-worthy content beats follower count",
            "facebook": "Underrated in 2024-25, longer form works, community engagement, groups",
            "linkedin": "HUGE opportunity - demand outpaces supply, professional insights, thought leadership",
            "tiktok": "Interest-based algorithm, hook in 1 second, authentic > polished"
        },
        "caption_rules": [
            "First 3-5 words determine if algorithm shows it - make them count",
            "80% value, 20% ask (jab jab jab right hook)",
            "Document don't create - authenticity beats polish",
            "Interest-based algorithms: Quality of content > number of followers",
            "LinkedIn and Facebook are underrated opportunities in 2024-25"
        ],
        "algorithm_reality_2024": {
            "old_model": "Follower count determined reach",
            "new_model": "Content quality and engagement determine reach (TikTokification)",
            "implication": "A post can go viral with 100 followers if content resonates"
        }
    },

    "russell_brunson": {
        "name": "Russell Brunson",
        "specialty": "Funnels & Storytelling",
        "core_philosophy": "Hook, Story, Offer - every piece of content is a mini funnel",
        "key_framework": "Hook Story Offer",
        "framework_parts": {
            "hook": "Capture attention in first line (pattern interrupt)",
            "story": "Build connection through narrative and relatability",
            "offer": "Clear value proposition and CTA"
        },
        "caption_rules": [
            "Every caption = mini funnel",
            "Hook must stop the scroll",
            "Story creates emotional connection",
            "Offer can be soft (engage) or hard (buy)"
        ]
    }
}

# =============================================================================
# EXPERT SELECTION BY INDUSTRY
# =============================================================================

INDUSTRY_EXPERT_MAPPING = {
    "default": {
        "primary": ["eugene_schwartz", "david_ogilvy"],
        "supporting": ["gary_vaynerchuk", "robert_cialdini"],
        "reason": "Core copywriting + social media + psychology"
    },
    "saas": {
        "primary": ["marcus_sheridan", "eugene_schwartz"],
        "supporting": ["seth_godin", "robert_cialdini"],
        "reason": "Educational content + awareness stages + community"
    },
    "ecommerce": {
        "primary": ["joseph_sugarman", "robert_cialdini"],
        "supporting": ["gary_vaynerchuk", "russell_brunson"],
        "reason": "Psychological triggers + influence + funnels"
    },
    "local_business": {
        "primary": ["marcus_sheridan", "david_ogilvy"],
        "supporting": ["gary_vaynerchuk", "robert_cialdini"],
        "reason": "Trust-building + community + social proof"
    },
    "professional_services": {
        "primary": ["david_ogilvy", "seth_godin"],
        "supporting": ["marcus_sheridan", "robert_cialdini"],
        "reason": "Authority + tribe building + trust"
    },
    "health_wellness": {
        "primary": ["eugene_schwartz", "robert_cialdini"],
        "supporting": ["marcus_sheridan", "seth_godin"],
        "reason": "Awareness stages + trust + education"
    },
    "real_estate": {
        "primary": ["marcus_sheridan", "david_ogilvy"],
        "supporting": ["robert_cialdini", "gary_vaynerchuk"],
        "reason": "Answer questions + local + social proof"
    },
    "coaching_consulting": {
        "primary": ["seth_godin", "russell_brunson"],
        "supporting": ["marcus_sheridan", "robert_cialdini"],
        "reason": "Tribe building + funnels + authority"
    },
    "restaurant_hospitality": {
        "primary": ["gary_vaynerchuk", "david_ogilvy"],
        "supporting": ["robert_cialdini", "joseph_sugarman"],
        "reason": "Social + visual + cravings + scarcity"
    }
}

# =============================================================================
# CONTENT PILLAR TO EXPERT MAPPING
# =============================================================================

PILLAR_EXPERT_EMPHASIS = {
    "education": {
        "lead_expert": "marcus_sheridan",
        "emphasis": "Answer real questions, be the trusted resource"
    },
    "behind_the_scenes": {
        "lead_expert": "gary_vaynerchuk",
        "emphasis": "Authenticity, day-in-the-life, process"
    },
    "testimonials": {
        "lead_expert": "robert_cialdini",
        "emphasis": "Social proof, specific results, relatability"
    },
    "tips": {
        "lead_expert": "eugene_schwartz",
        "emphasis": "Quick wins, awareness-appropriate depth"
    },
    "promotion": {
        "lead_expert": "joseph_sugarman",
        "emphasis": "Psychological triggers, urgency, specificity"
    },
    "thought_leadership": {
        "lead_expert": "seth_godin",
        "emphasis": "Contrarian takes, tribe rallying, big ideas"
    },
    "entertainment": {
        "lead_expert": "gary_vaynerchuk",
        "emphasis": "Platform trends, relatability, shareability"
    },
    "product": {
        "lead_expert": "david_ogilvy",
        "emphasis": "Benefits over features, specificity, proof"
    }
}

# =============================================================================
# 2024-2025 ALGORITHM REALITY
# =============================================================================

ALGORITHM_PRINCIPLES_2024 = {
    "interest_based": {
        "principle": "TikTokification of all platforms",
        "explanation": "Algorithms now show content based on interest/engagement, not follower count",
        "implication": "A great post from a small account can outperform a mediocre post from a big account"
    },
    "first_3_seconds": {
        "principle": "Hook determines reach",
        "explanation": "Algorithm measures if people stop scrolling - first line is everything",
        "implication": "Weak hooks = algorithm buries the post, regardless of how good the rest is"
    },
    "save_share_over_likes": {
        "principle": "Saves and shares signal value",
        "explanation": "Algorithms weight saves/shares higher than likes - they indicate real value",
        "implication": "Create content people want to reference later or share with others"
    },
    "platform_undervalued": {
        "principle": "LinkedIn and Facebook are undervalued (2024-25)",
        "explanation": "Everyone rushed to TikTok/Reels, leaving opportunity on LinkedIn and Facebook",
        "implication": "Consider these platforms for B2B and local businesses especially"
    }
}

# =============================================================================
# STATIC IMAGE POST OPTIMIZATION (for non-video content)
# =============================================================================

STATIC_IMAGE_STRATEGY = {
    "reality": "Most small businesses can't produce consistent video content - and that's okay",
    "opportunity": "Strong captions + quality images can outperform mediocre video",
    "principles": {
        "caption_carries_weight": "Without video, the caption does ALL the storytelling work",
        "image_stops_scroll": "Image gets attention, caption keeps it and drives action",
        "carousel_power": "Carousels (multi-image) get higher engagement than single images on Instagram",
        "save_worthy": "Educational carousels get saved - saves boost algorithm ranking"
    },
    "format_recommendations": {
        "instagram": "Carousels with text overlays + strong caption = high saves",
        "facebook": "Single image with longer storytelling caption works well",
        "linkedin": "Document posts (PDF carousels) or single image + thought leadership caption"
    },
    "caption_must_do": [
        "Tell the story the image can't tell",
        "Create context and meaning for the visual",
        "Include a clear next step (even if soft)",
        "Be worth reading even without the image"
    ]
}

# =============================================================================
# QUALITY GATES
# =============================================================================

QUALITY_GATES = {
    "schwartz_awareness": {
        "question": "Does this caption match the audience's awareness stage?",
        "check": "Unaware audience shouldn't see product pitch. Most-aware shouldn't need education."
    },
    "ogilvy_headline": {
        "question": "Does the first line contain a benefit or news?",
        "check": "If first line is generic ('Happy Monday!'), it fails."
    },
    "sugarman_curiosity": {
        "question": "Does this create a 'knowledge gap' the reader wants to close?",
        "check": "Would you keep reading after line 1?"
    },
    "cialdini_principle": {
        "question": "Is at least one influence principle embedded naturally?",
        "check": "Social proof, scarcity, authority, etc. - but not forced."
    },
    "godin_remarkable": {
        "question": "Would someone share this or screenshot it?",
        "check": "If it's forgettable, it fails."
    },
    "platform_native": {
        "question": "Is this optimized for the specific platform?",
        "check": "Instagram carousel ≠ LinkedIn post ≠ TikTok caption"
    },
    "algorithm_first": {
        "question": "Will the algorithm show this to people?",
        "check": "First line must hook. Content must be save/share-worthy. Interest > follower count."
    },
    "static_image_strength": {
        "question": "Does this caption carry the full story for a static post?",
        "check": "Without video, caption must do ALL the work. Is it strong enough to stand alone?"
    }
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_experts_for_client(industry: str, content_pillar: str = None) -> dict:
    """
    Select the right 3-4 experts for a client based on industry.
    Optionally adjust for content pillar.
    """
    # Get base experts for industry
    industry_key = industry.lower().replace(" ", "_").replace("&", "_")
    expert_config = INDUSTRY_EXPERT_MAPPING.get(industry_key, INDUSTRY_EXPERT_MAPPING["default"])

    selected = {
        "primary": [EXPERTS[e] for e in expert_config["primary"]],
        "supporting": [EXPERTS[e] for e in expert_config["supporting"]],
        "reason": expert_config["reason"]
    }

    # If content pillar specified, add emphasis
    if content_pillar:
        pillar_key = content_pillar.lower().replace(" ", "_").replace("-", "_")
        if pillar_key in PILLAR_EXPERT_EMPHASIS:
            pillar_expert = PILLAR_EXPERT_EMPHASIS[pillar_key]
            selected["pillar_emphasis"] = {
                "expert": EXPERTS[pillar_expert["lead_expert"]],
                "emphasis": pillar_expert["emphasis"]
            }

    return selected


def build_expert_prompt_section(experts: dict) -> str:
    """
    Build the expert framework section for the caption generation prompt.
    This is the key to not "doing too much" - focused, selective application.
    """
    prompt_parts = []

    # Primary experts - these are the main frameworks
    prompt_parts.append("## PRIMARY EXPERT FRAMEWORKS (Apply These)")
    for expert in experts["primary"]:
        prompt_parts.append(f"""
### {expert['name']} - {expert['specialty']}
**Philosophy**: "{expert['core_philosophy']}"
**Key Rules for Captions**:
{chr(10).join(f"- {rule}" for rule in expert['caption_rules'])}
""")

    # Supporting experts - lighter touch
    prompt_parts.append("\n## SUPPORTING PERSPECTIVES (Consider These)")
    for expert in experts["supporting"]:
        prompt_parts.append(f"""
### {expert['name']}
- Apply: {expert['caption_rules'][0]}
""")

    # Content pillar emphasis if present
    if "pillar_emphasis" in experts:
        pe = experts["pillar_emphasis"]
        prompt_parts.append(f"""
## CONTENT PILLAR EMPHASIS
For this content type, lean into **{pe['expert']['name']}**:
- {pe['emphasis']}
""")

    return "\n".join(prompt_parts)


def build_quality_gates_section() -> str:
    """Build the quality gates that captions must pass."""
    gates = []
    gates.append("## QUALITY GATES (Each Caption Must Pass)")
    for gate_name, gate_info in QUALITY_GATES.items():
        gates.append(f"- **{gate_info['question']}** {gate_info['check']}")
    return "\n".join(gates)


def get_awareness_guidance(target_audience: str) -> str:
    """
    Provide guidance on audience awareness stage based on description.
    This prevents the common mistake of pitching to unaware audiences.
    """
    # Simple heuristics - could be enhanced with AI analysis
    audience_lower = target_audience.lower() if target_audience else ""

    if any(word in audience_lower for word in ["cold", "new", "don't know", "never heard"]):
        return """
**AWARENESS STAGE: Mostly Unaware to Problem-Aware**
- Don't pitch products yet
- Lead with relatable problems and curiosity
- Focus on "Did you know..." and "Ever feel like..."
- NO hard CTAs - just engagement
"""
    elif any(word in audience_lower for word in ["looking for", "researching", "considering", "shopping"]):
        return """
**AWARENESS STAGE: Solution-Aware to Product-Aware**
- Can discuss your solution directly
- Differentiate from alternatives
- Use social proof and results
- Soft CTAs okay (learn more, DM us)
"""
    elif any(word in audience_lower for word in ["existing", "current", "returning", "loyal"]):
        return """
**AWARENESS STAGE: Most Aware**
- Can make direct offers
- Reminder content, exclusive access
- Hard CTAs fine (buy now, book today)
- Focus on loyalty and community
"""
    else:
        return """
**AWARENESS STAGE: Mixed (Default to Problem-Aware)**
- Mix of education and soft promotion
- Lead with value, CTA at end
- Balance between awareness stages
- When in doubt, educate first
"""


# =============================================================================
# MAIN PROMPT BUILDER
# =============================================================================

def build_algorithm_section() -> str:
    """Build the 2024-25 algorithm reality section."""
    lines = ["## 2024-2025 ALGORITHM REALITY (This is how social media works now)"]
    for key, info in ALGORITHM_PRINCIPLES_2024.items():
        lines.append(f"- **{info['principle']}**: {info['explanation']}")
    return "\n".join(lines)


def build_static_image_section() -> str:
    """Build guidance for static image posts (non-video)."""
    s = STATIC_IMAGE_STRATEGY
    lines = [
        "## STATIC IMAGE POST STRATEGY",
        f"**Reality**: {s['reality']}",
        f"**Opportunity**: {s['opportunity']}",
        "",
        "**Your caption must**:"
    ]
    for item in s["caption_must_do"]:
        lines.append(f"- {item}")
    return "\n".join(lines)


def build_enhanced_caption_prompt(
    strategy: dict,
    previous_posts: list,
    num_captions: int,
    platform: str,
    content_theme: str = None,
    specific_topic: str = None
) -> str:
    """
    Build a caption generation prompt using selective expert frameworks.
    This is the key improvement - focused application, not everything at once.

    Updated for 2024-2025:
    - Interest-based algorithm awareness
    - Static image optimization (most clients don't have video)
    - Gary V's Day Trading Attention principles
    """

    # 1. Select the right experts for this client
    industry = strategy.get("industry", "default")
    experts = get_experts_for_client(industry, content_theme)

    # 2. Build the expert framework section
    expert_section = build_expert_prompt_section(experts)

    # 3. Get awareness stage guidance
    awareness_guidance = get_awareness_guidance(strategy.get("target_audience", ""))

    # 4. Build quality gates
    quality_gates = build_quality_gates_section()

    # 5. Build algorithm reality section (2024-25 update)
    algorithm_section = build_algorithm_section()

    # 6. Build static image strategy (since most clients don't have video)
    static_image_section = build_static_image_section()

    # 7. Platform-specific rules (updated for 2024)
    platform_rules = EXPERTS["gary_vaynerchuk"]["platform_rules"].get(
        platform.lower(),
        "Optimize for the platform's native format and algorithm"
    )

    # Get platform-specific format recommendation
    format_rec = STATIC_IMAGE_STRATEGY["format_recommendations"].get(
        platform.lower(),
        "Strong visual + caption that tells the full story"
    )

    prompt = f"""You are an expert social media copywriter applying proven frameworks.

**IMPORTANT CONTEXT**: These are captions for STATIC IMAGE posts (not video). The caption must carry the full storytelling weight.

{expert_section}

---

## CLIENT STRATEGY

**Brand Voice**: {strategy.get('brand_voice', 'Professional and engaging')}
**Tone**: {', '.join(strategy.get('tone_keywords', ['friendly', 'expert']))}
**Content Pillars**: {', '.join(strategy.get('content_pillars', ['education', 'engagement']))}
**Target Audience**: {strategy.get('target_audience', 'General audience')}
**Industry**: {strategy.get('industry', 'General')}
**Key Messages**: {', '.join(strategy.get('key_messages', []))}
**USPs**: {', '.join(strategy.get('unique_selling_points', []))}

{awareness_guidance}

---

## PLATFORM: {platform.upper()}

{platform_rules}

**Best format for static posts on {platform}**: {format_rec}

Character limits:
- Instagram: 2,200 max (but first 125 chars shown in feed)
- Facebook: Can be longer, but engagement drops after 80 chars preview
- LinkedIn: 3,000 max, but hook must be in first 2 lines
- TikTok: 150 max for captions

---

{algorithm_section}

---

{static_image_section}

---

## CONTENT DIRECTION

{f"**Theme/Pillar**: {content_theme}" if content_theme else "**Theme**: Mix of content pillars"}
{f"**Specific Topic**: {specific_topic}" if specific_topic else ""}

---

## PREVIOUS POSTS (Avoid Similarity)

{chr(10).join([f"- {post[:150]}..." if len(post) > 150 else f"- {post}" for post in previous_posts[-15:]]) if previous_posts else "No previous posts yet - full creative freedom."}

---

## TOPICS TO AVOID

{', '.join(strategy.get('topics_to_avoid', [])) if strategy.get('topics_to_avoid') else 'None specified'}

---

{quality_gates}

---

## YOUR TASK

Generate exactly {num_captions} captions for STATIC IMAGE posts that:

1. **Pass all quality gates** above
2. **Apply the expert frameworks** (not generic social media advice)
3. **Match the awareness stage** of the target audience
4. **Sound like the brand**, not like AI
5. **Are platform-native** for {platform}
6. **Work for the algorithm** (hook in first line, save/share-worthy content)
7. **Carry the full story** since there's no video - the caption must do ALL the work

---

## OUTPUT FORMAT

Return a JSON array with exactly {num_captions} objects:

```json
[
  {{
    "caption": "The full caption text (without hashtags)",
    "hashtags": ["relevant", "hashtags", "without", "hash", "symbol"],
    "hook": "The first line/scroll-stopper",
    "content_pillar": "Which pillar this falls under",
    "awareness_stage": "unaware|problem_aware|solution_aware|product_aware|most_aware",
    "expert_frameworks_applied": ["Which expert principles were used"],
    "cta_type": "none|soft|medium|hard",
    "why_it_works": "1-2 sentences on why this caption works for this brand"
  }}
]
```

Generate {num_captions} unique, on-brand captions now. Remember: You're channeling {experts['primary'][0]['name']} and {experts['primary'][1]['name']}, not writing generic social media content."""

    return prompt
