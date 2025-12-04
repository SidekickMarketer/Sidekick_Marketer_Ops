"""
Expert Council Framework for Caption Generation

This module provides the expert frameworks from your existing system,
applied selectively based on client industry and content type.

Key principle: 3-4 experts max per generation, not all at once.

Integrated with Sidekick Marketer skills:
- Hook bank (50+ categorized hooks)
- CTA bank (by goal type)
- Caption templates (by pillar)
- Platform benchmarks (2024-2025 research data)
"""

from typing import Optional, List, Dict

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
# HOOK BANK (from Sidekick Skills)
# =============================================================================

HOOK_BANK = {
    "question": {
        "description": "Drive curiosity and engagement",
        "best_for": ["education", "tips", "thought_leadership"],
        "hooks": [
            "What's the #1 mistake new {audience} make?",
            "Why do most people fail at {topic}?",
            "Did you know this about {topic}?",
            "Ever wonder why {topic} is so hard?",
            "What would you do if {scenario}?",
            "Can you guess what happened next?",
            "Ready for a hard truth about {topic}?"
        ]
    },
    "statement": {
        "description": "Bold claims that stop the scroll",
        "best_for": ["thought_leadership", "promotion", "education"],
        "hooks": [
            "This changed everything for {subject}.",
            "Most people get this completely wrong.",
            "Here's what nobody tells you about {topic}.",
            "The secret to {outcome} isn't what you think.",
            "This is the post I wish I'd seen {timeframe} ago.",
            "Unpopular opinion: {statement}.",
            "Stop doing {action}. Here's why."
        ]
    },
    "story": {
        "description": "Draw readers into a narrative",
        "best_for": ["testimonials", "behind_the_scenes", "student_success"],
        "hooks": [
            "3 months ago, {name} couldn't {action}.",
            "I'll never forget the moment {event}.",
            "When {name} first walked in, they {state}.",
            "It started with a simple question: {question}.",
            "Last week, something incredible happened.",
            "{Name} almost gave up. Then {turning_point}.",
            "The day everything clicked for {subject}."
        ]
    },
    "number_list": {
        "description": "Promise specific, scannable value",
        "best_for": ["education", "tips", "product"],
        "hooks": [
            "5 mistakes that are {negative_outcome}.",
            "3 ways to {positive_outcome} today.",
            "The 4 things every {audience} needs to know.",
            "7 signs you need {solution}.",
            "1 simple trick that changes everything.",
            "10 {items} that will {benefit}."
        ]
    },
    "emotional": {
        "description": "Connect through feeling",
        "best_for": ["testimonials", "community", "behind_the_scenes"],
        "hooks": [
            "This moment made our whole week.",
            "We're not crying, you're crying.",
            "Pride doesn't even begin to describe it.",
            "This is why we do what we do.",
            "Grab the tissues for this one.",
            "Best. Day. Ever."
        ]
    },
    "pattern_interrupt": {
        "description": "Break expectations",
        "best_for": ["thought_leadership", "promotion", "entertainment"],
        "hooks": [
            "Forget everything you know about {topic}.",
            "Plot twist: {unexpected_statement}.",
            "Wait for it...",
            "Okay, we need to talk about {topic}.",
            "This isn't your typical {content_type} post.",
            "Read this before you {common_action}."
        ]
    },
    "urgency": {
        "description": "Create immediate interest",
        "best_for": ["promotion", "tips", "education"],
        "hooks": [
            "You're going to want to save this.",
            "Don't scroll past this one.",
            "This won't last long.",
            "If you've been waiting for a sign, this is it.",
            "Last chance to {action}."
        ]
    }
}

# Pillar to hook type mapping
PILLAR_HOOK_MAPPING = {
    "student_success": ["story", "emotional"],
    "testimonials": ["story", "emotional"],
    "education": ["question", "number_list"],
    "tips": ["question", "number_list"],
    "behind_the_scenes": ["story", "pattern_interrupt"],
    "community": ["emotional", "statement"],
    "promotion": ["urgency", "statement"],
    "thought_leadership": ["statement", "pattern_interrupt"],
    "entertainment": ["pattern_interrupt", "emotional"],
    "product": ["number_list", "statement"]
}

# =============================================================================
# CTA BANK (from Sidekick Skills)
# =============================================================================

CTA_BANK = {
    "engagement": {
        "description": "Drive comments and interaction",
        "best_for": ["community", "behind_the_scenes", "entertainment"],
        "ctas": [
            "Drop a {emoji} if you agree!",
            "Which one are you? Comment below!",
            "Tag someone who needs to see this.",
            "Tell us in the comments!",
            "What's your experience with {topic}?",
            "Agree or disagree? Let us know 👇",
            "Can you relate?"
        ]
    },
    "save": {
        "description": "Boost algorithm with saves",
        "best_for": ["education", "tips", "tutorials"],
        "ctas": [
            "Save this for later 📌",
            "Bookmark this post!",
            "Save this for your next {activity}.",
            "You'll want to come back to this.",
            "📌 Save and share with someone who needs it.",
            "Keep this in your back pocket."
        ]
    },
    "share": {
        "description": "Expand reach through shares",
        "best_for": ["testimonials", "tips", "emotional_content"],
        "ctas": [
            "Tag a friend who needs this!",
            "Share this with someone starting {journey}.",
            "Know someone who'd love this? Send it their way!",
            "Share with your {person_type}.",
            "Spread the word! 📣"
        ]
    },
    "action": {
        "description": "Drive specific conversions",
        "best_for": ["promotion", "product", "services"],
        "ctas": [
            "Link in bio to {action}!",
            "DM us \"{keyword}\" to get started.",
            "Click the link to learn more.",
            "Book your {offering} today →",
            "Tap the link in our bio!",
            "Call us at {phone} to {action}."
        ]
    },
    "soft": {
        "description": "Gentle nudges without pressure",
        "best_for": ["awareness", "brand_building", "sensitive_topics"],
        "ctas": [
            "Just something to think about.",
            "Here if you need us!",
            "Questions? We're always here.",
            "Ready when you are.",
            "No pressure, just possibilities."
        ]
    },
    "question": {
        "description": "Invite dialogue",
        "best_for": ["community", "thought_leadership", "discussion"],
        "ctas": [
            "What do you think?",
            "Have you tried this?",
            "What's your favorite {item}?",
            "How do you handle {situation}?",
            "What would you add to this list?",
            "Agree? Disagree? Tell us!"
        ]
    },
    "carousel": {
        "description": "For swipeable content",
        "best_for": ["education", "tips", "tutorials"],
        "ctas": [
            "Swipe for more →",
            "Don't stop at slide 1!",
            "The best tip is on the last slide 👀",
            "Keep swiping for {topic}.",
            "Slide {number} is the game-changer."
        ]
    }
}

# Pillar to CTA type mapping
PILLAR_CTA_MAPPING = {
    "student_success": ["share", "engagement"],
    "testimonials": ["share", "engagement"],
    "education": ["save", "share"],
    "tips": ["save", "carousel"],
    "behind_the_scenes": ["engagement", "question"],
    "community": ["engagement", "share"],
    "promotion": ["action", "soft"],
    "thought_leadership": ["question", "engagement"],
    "entertainment": ["engagement", "share"],
    "product": ["action", "save"]
}

# =============================================================================
# CAPTION TEMPLATES (from Sidekick Skills)
# =============================================================================

CAPTION_TEMPLATES = {
    "student_success": {
        "name": "Student Success / Testimonial",
        "structure": [
            "[STUDENT NAME/DESCRIPTOR] just hit a major milestone. [EMOJI]",
            "",
            "[SPECIFIC ACHIEVEMENT - what they did, how long it took]",
            "",
            "[EMOTIONAL MOMENT - the reaction, the feeling]",
            "",
            "[CONNECTION TO AUDIENCE - this could be you]",
            "",
            "[CTA]"
        ],
        "example": """This moment changed everything for Marcus. 🎹

After 3 months of consistent practice, he played his first complete song for his family. No mistakes. Just pure joy on everyone's faces.

That's what we live for at Cincinnati Music Academy.

Ready to create your own moment?
Link in bio to book your first lesson →"""
    },
    "education": {
        "name": "Educational / Tips",
        "structure": [
            "[PROBLEM or MYTH statement - what people get wrong]",
            "",
            "[THE TRUTH or SOLUTION - what actually works]",
            "",
            "[BRIEF EXPLANATION - why this matters]",
            "",
            "[ACTIONABLE ADVICE - what to do now]",
            "",
            "[CTA - save, try, share]"
        ],
        "example": """Most beginners make this mistake without even knowing it. 🎸

They practice the same thing over and over—but never actually improve.

Here's why: repetition without intention doesn't build skill. You need focused practice with specific goals.

Try this instead: Set a 3-minute timer. Focus on ONE section. Rest. Repeat.

Save this for your next practice session 📌"""
    },
    "behind_the_scenes": {
        "name": "Behind-the-Scenes / Team",
        "structure": [
            "[PEEK BEHIND THE CURTAIN - what you're showing]",
            "",
            "[STORY or CONTEXT - why this matters]",
            "",
            "[HUMAN ELEMENT - personality, authenticity]",
            "",
            "[CONNECTION - relate to audience]",
            "",
            "[CTA - engage, ask, comment]"
        ],
        "example": """Ever wonder what happens before lessons start? ☕

Our instructors arrive 30 minutes early every day. Not because they have to—because they love preparing for their students.

That's Sarah reviewing her lesson plans and sipping her third coffee of the day (don't judge 😅).

What does your morning prep look like? Tell us below! 👇"""
    },
    "community": {
        "name": "Community / Local",
        "structure": [
            "[LOCAL REFERENCE or COMMUNITY MOMENT]",
            "",
            "[WHY THIS MATTERS - connection to your business]",
            "",
            "[APPRECIATION - gratitude, acknowledgment]",
            "",
            "[ENGAGEMENT PROMPT - question, tag request]"
        ],
        "example": """Cincinnati, we love you! ❤️

This weekend we got to perform at Fountain Square for the Summer Music Festival. Seeing our students on that stage, in front of their hometown—incredible.

Thank you to everyone who came out to support. Our community makes everything we do possible.

Were you there? Drop a 🎵 if you caught the show!"""
    },
    "promotion": {
        "name": "Promotional / CTA",
        "structure": [
            "[VALUE HOOK - lead with benefit, not feature]",
            "",
            "[THE OFFER - what's available]",
            "",
            "[SOCIAL PROOF - quick credibility]",
            "",
            "[URGENCY if appropriate - limited time/spots]",
            "",
            "[CLEAR CTA - specific next step]"
        ],
        "example": """Your child's musical journey starts here. 🎶

Spring registration is NOW OPEN for piano, guitar, voice, and drums.

Join 200+ families who've already discovered what makes our lessons different: patient instructors, flexible scheduling, and real results.

Early bird pricing ends Friday—only 8 spots left for new students!

👉 Link in bio to reserve your spot"""
    },
    "carousel": {
        "name": "Carousel / Multi-slide",
        "structure": [
            "[HOOK - curiosity-driving, swipe-inviting opening]",
            "",
            "[CONTEXT - why this matters, sets up slides]",
            "",
            "[CTA - Save/Share emphasis]"
        ],
        "slide_structure": [
            "📍 Slide 1: [Hook visual + text]",
            "📍 Slides 2-X: [Content breakdown]",
            "📍 Final Slide: [CTA + summary]"
        ],
        "example": """5 practice mistakes that are slowing you down ⬇️

We see these with students every single week. The good news? They're all fixable once you know what to look for.

Swipe through to see if you're making any of these—and the simple fixes that make a huge difference.

Which one are you guilty of? Drop a number below! 👇

📌 Save this post for your next practice session"""
    },
    "gbp": {
        "name": "Google Business Profile",
        "structure": [
            "[VALUE STATEMENT - What you offer/update]",
            "",
            "[BRIEF CONTEXT - 1-2 sentences max]",
            "",
            "[CTA - Specific action with urgency if appropriate]"
        ],
        "example": """Spring lesson registration is now open! 🎵

New students can book a free 30-minute trial lesson to find the perfect instructor match.

Call (513) XXX-XXXX or visit our website to reserve your spot—spaces fill quickly!""",
        "notes": "GBP posts should be shorter, business-focused, NO hashtags"
    }
}

# =============================================================================
# PLATFORM BENCHMARKS (from Sidekick Skills - 2024-2025 data)
# =============================================================================

PLATFORM_BENCHMARKS = {
    "instagram": {
        "engagement_rates": {
            "education": "4.2% - 4.52%",
            "all_industries": "0.55% - 1.5%",
            "healthcare": "3.89%"
        },
        "caption_length": {
            "optimal": "125-150 characters",
            "carousels": "300-500 characters acceptable",
            "max": "2,200 characters",
            "truncation_point": "125 characters (hook must be before this)"
        },
        "hashtags": {
            "quantity": "5-10 (not 30)",
            "mix": "1 broad + 2-3 niche + 1-2 branded + 1-2 local"
        },
        "format_performance": {
            "carousels": "+22-38% higher engagement than single images",
            "reels": "6.92% engagement (highest reach)",
            "single_images": "Declining performance"
        },
        "optimal_slides": "8-10 slides perform best (or keep it short at 3)",
        "best_times": {
            "best_days": ["Tuesday", "Wednesday", "Thursday"],
            "best_hours": "6-8 AM or 4-6 PM",
            "worst_day": "Saturday"
        },
        "posting_frequency": "4-5x per week"
    },
    "facebook": {
        "engagement_rates": {
            "all_industries": "0.5% - 1%",
            "healthcare": "2.22%"
        },
        "caption_length": {
            "optimal": "40-80 characters (66% higher engagement)",
            "note": "Shorter is dramatically better",
            "max": "63,206 characters (avoid)"
        },
        "hashtags": {
            "quantity": "1-3 only"
        },
        "best_times": {
            "best_days": ["Wednesday", "Sunday", "Thursday"],
            "best_hours": "1-3 PM (especially 2 PM)"
        },
        "posting_frequency": "3-4x per week",
        "notes": [
            "Links are clickable in captions",
            "Questions drive comments",
            "Less posting = higher engagement"
        ]
    },
    "gbp": {
        "caption_length": {
            "optimal": "100-300 characters",
            "max": "1,500 characters"
        },
        "hashtags": {
            "quantity": "NONE (not a social platform)"
        },
        "posting_frequency": "2-3x per week minimum",
        "image_requirements": {
            "resolution": "1080 x 1080 pixels",
            "frequency": "3+ photos weekly"
        },
        "impact": {
            "photos": "+42% direction requests, +35% website clicks",
            "cta_buttons": "Always include (Call, Book, Learn More)"
        },
        "post_types": ["Update", "Offer", "Event", "Product"],
        "notes": [
            "Front-load local SEO keywords",
            "Respond to ALL reviews within 24 hours",
            "Posts expire after 7 days (except offers/events)"
        ]
    },
    "linkedin": {
        "caption_length": {
            "optimal": "First 2 lines must hook",
            "max": "3,000 characters"
        },
        "notes": [
            "HUGE opportunity in 2024-25",
            "Demand outpaces supply",
            "Document posts (PDF carousels) perform well",
            "Thought leadership + professional insights"
        ]
    }
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_hooks_for_pillar(pillar: str) -> dict:
    """Get recommended hooks for a content pillar."""
    pillar_key = pillar.lower().replace(" ", "_").replace("-", "_")
    hook_types = PILLAR_HOOK_MAPPING.get(pillar_key, ["question", "statement"])

    hooks = {}
    for hook_type in hook_types:
        if hook_type in HOOK_BANK:
            hooks[hook_type] = HOOK_BANK[hook_type]

    return hooks


def get_ctas_for_pillar(pillar: str) -> dict:
    """Get recommended CTAs for a content pillar."""
    pillar_key = pillar.lower().replace(" ", "_").replace("-", "_")
    cta_types = PILLAR_CTA_MAPPING.get(pillar_key, ["engagement", "save"])

    ctas = {}
    for cta_type in cta_types:
        if cta_type in CTA_BANK:
            ctas[cta_type] = CTA_BANK[cta_type]

    return ctas


def get_template_for_pillar(pillar: str) -> dict:
    """Get caption template for a content pillar."""
    pillar_key = pillar.lower().replace(" ", "_").replace("-", "_")
    return CAPTION_TEMPLATES.get(pillar_key, CAPTION_TEMPLATES.get("education"))


def get_platform_specs(platform: str) -> dict:
    """Get platform-specific benchmarks and specs."""
    return PLATFORM_BENCHMARKS.get(platform.lower(), PLATFORM_BENCHMARKS.get("instagram"))


def build_hooks_section(pillar: str) -> str:
    """Build the hooks section for the prompt."""
    hooks = get_hooks_for_pillar(pillar)
    if not hooks:
        return ""

    lines = [f"## RECOMMENDED HOOKS (for {pillar} content)"]
    lines.append("Choose ONE hook style and adapt it to your topic:\n")

    for hook_type, hook_data in hooks.items():
        lines.append(f"**{hook_type.replace('_', ' ').title()}** - {hook_data['description']}")
        for hook in hook_data['hooks'][:4]:  # Show top 4 examples
            lines.append(f"  - \"{hook}\"")
        lines.append("")

    return "\n".join(lines)


def build_cta_section(pillar: str) -> str:
    """Build the CTA section for the prompt."""
    ctas = get_ctas_for_pillar(pillar)
    if not ctas:
        return ""

    lines = [f"## RECOMMENDED CTAs (for {pillar} content)"]
    lines.append("Choose ONE CTA style:\n")

    for cta_type, cta_data in ctas.items():
        lines.append(f"**{cta_type.replace('_', ' ').title()}** - {cta_data['description']}")
        for cta in cta_data['ctas'][:3]:  # Show top 3 examples
            lines.append(f"  - \"{cta}\"")
        lines.append("")

    return "\n".join(lines)


def build_template_section(pillar: str) -> str:
    """Build the caption template section for the prompt."""
    template = get_template_for_pillar(pillar)
    if not template:
        return ""

    lines = [f"## CAPTION TEMPLATE (for {template['name']})"]
    lines.append("Follow this structure:\n")
    lines.append("```")
    lines.extend(template['structure'])
    lines.append("```\n")
    lines.append("**Example:**")
    lines.append(f"```\n{template['example']}\n```")

    return "\n".join(lines)


def build_platform_specs_section(platform: str) -> str:
    """Build platform-specific specs section for the prompt."""
    specs = get_platform_specs(platform)
    if not specs:
        return ""

    lines = [f"## PLATFORM SPECS: {platform.upper()} (2024-2025 Data)"]

    # Caption length
    if "caption_length" in specs:
        cl = specs["caption_length"]
        lines.append(f"\n**Caption Length:**")
        lines.append(f"  - Optimal: {cl.get('optimal', 'N/A')}")
        if "truncation_point" in cl:
            lines.append(f"  - Truncation: {cl['truncation_point']}")

    # Hashtags
    if "hashtags" in specs:
        ht = specs["hashtags"]
        lines.append(f"\n**Hashtags:** {ht.get('quantity', 'N/A')}")
        if "mix" in ht:
            lines.append(f"  - Mix: {ht['mix']}")

    # Best times
    if "best_times" in specs:
        bt = specs["best_times"]
        lines.append(f"\n**Best Posting Times:**")
        if "best_days" in bt:
            lines.append(f"  - Days: {', '.join(bt['best_days'])}")
        if "best_hours" in bt:
            lines.append(f"  - Hours: {bt['best_hours']}")

    # Format performance (Instagram)
    if "format_performance" in specs:
        fp = specs["format_performance"]
        lines.append(f"\n**Format Performance:**")
        for format_type, perf in fp.items():
            lines.append(f"  - {format_type.replace('_', ' ').title()}: {perf}")

    # Notes
    if "notes" in specs:
        lines.append(f"\n**Platform Notes:**")
        for note in specs["notes"]:
            lines.append(f"  - {note}")

    return "\n".join(lines)


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

    Integrated with Sidekick Skills:
    - Hook bank with pillar-specific recommendations
    - CTA bank with goal-specific options
    - Caption templates with proven structures
    - Platform benchmarks with 2024-2025 data
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

    # 8. NEW: Build hooks section based on content pillar
    pillar = content_theme or "education"
    hooks_section = build_hooks_section(pillar)

    # 9. NEW: Build CTA section based on content pillar
    cta_section = build_cta_section(pillar)

    # 10. NEW: Build template section based on content pillar
    template_section = build_template_section(pillar)

    # 11. NEW: Build platform specs section with benchmarks
    platform_specs_section = build_platform_specs_section(platform)

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

{platform_specs_section}

---

{hooks_section}

---

{cta_section}

---

{template_section}

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

1. **Use a hook from the RECOMMENDED HOOKS section** - Adapt one to fit the topic
2. **Follow the CAPTION TEMPLATE structure** - Don't reinvent, use what works
3. **End with a CTA from the RECOMMENDED CTAs section** - Match to goal
4. **Apply the expert frameworks** - Channel the named experts, not generic advice
5. **Match the awareness stage** of the target audience
6. **Sound like the brand**, not like AI
7. **Are platform-native** for {platform} - Follow the platform specs above
8. **Work for the algorithm** - Hook in first line, save/share-worthy content
9. **Pass all quality gates** above

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
