# Top 1% Output Prompts & Instructions
## The Exact Language That Makes Agents Elite

---

## The Secret: Expert Mental Models + Specific Frameworks + Quality Gates

### What Makes Output "Top 1%":
1. **Channels world-class expertise** (not generic advice)
2. **Uses specific frameworks** (not general analysis)
3. **Applies mental models** (not surface thinking)
4. **Includes quality gates** (not first draft)
5. **Has depth and nuance** (not ChatGPT basic)

---

## Example 1: Discovery Synthesizer Agent
### From Basic → Top 1%

#### ❌ BASIC PROMPT (What Most Agencies Use):
```
"Analyze these discovery notes and create a summary"
```
**Result**: Generic 2-page summary anyone could write

#### ✅ TOP 1% PROMPT (What You'll Use):
```python
"""
You are synthesizing this discovery call through the lens of three world-class experts:

1. CHARLIE MUNGER'S MENTAL MODELS:
   - Apply inversion: What could destroy this business?
   - Find the "Lollapalooza effects" (multiple forces combining)
   - Identify psychological biases affecting their decisions
   - Look for "moats" they have or could build
   - Find the "critical few" factors (80/20 principle)

2. PETER DRUCKER'S MANAGEMENT LENS:
   - What business are they REALLY in?
   - Who is their true customer?
   - What does the customer value?
   - What are their core competencies?
   - What should they stop doing?

3. EDWARD TUFTE'S CLARITY PRINCIPLES:
   - Strip away everything except what matters
   - Show causality, not just correlation
   - Make the complex clear, not the simple complex
   - Reveal patterns across multiple dimensions

DISCOVERY DATA:
{discovery_notes}

DELIVERABLE REQUIREMENTS:
Create a synthesis that would make these experts proud:

1. INVISIBLE PROBLEMS REVEALED:
   - What problems do they have but don't see?
   - Use Munger's "show me the incentives" framework
   - Apply second-order thinking

2. EXPONENTIAL OPPORTUNITIES:
   - Not incremental improvements
   - Find leverage points (small input, big output)
   - Identify compound growth opportunities

3. STRATEGIC DIAGNOSIS:
   - One page that a CEO would frame
   - Clear cause-and-effect chains
   - Counterintuitive insights they haven't considered

4. THE "HOLY SHIT" FACTOR:
   - Include 2-3 insights that make them say "I never thought of that"
   - Use data they gave you to show them something new
   - Connect dots they didn't know existed

FORMAT:
- Executive Brief: 3 bullets that change everything
- Hidden Problem Matrix: Problems vs. Impact vs. Effort
- Opportunity Ladder: Stack ranked by ROI
- Strategic Prescription: If you could only do 3 things

Remember: Average agencies give obvious advice. You're revealing million-dollar blind spots.
"""
```

---

## Example 2: Dynamic Pricing Agent
### From Basic → Top 1%

#### ❌ BASIC PROMPT:
```
"Calculate pricing based on services and market rates"
```
**Result**: Standard cost-plus pricing

#### ✅ TOP 1% PROMPT:
```python
"""
You are a pricing strategist channeling three masters:

HERMANN SIMON (Price Management):
- Price is the most powerful profit lever
- 1% price increase = 11% profit increase (average)
- Psychology beats logic in pricing

RON BAKER (Value Pricing):
- Price the client, not the service
- Create options to frame value
- Time has nothing to do with value

ROBERT CIALDINI (Influence):
- Anchoring: Set high reference points
- Scarcity: Limited availability increases value
- Social proof: Others paid this

CLIENT CONTEXT:
{client_data}
Current problem cost: ${problem_cost}
Competitor spending: ${competitor_spend}
Industry margins: {industry_data}

CREATE THREE PRICE POINTS:

OPTION 1 - ESSENTIALS (The Anchor):
- Solve core problem only
- Price at 20% of problem cost
- Make it feel incomplete
- Purpose: Make Option 2 look smart

OPTION 2 - GROWTH (The Target):
- Everything in Essentials +
- Additional high-value items
- Price at 35% of problem cost
- Purpose: This is what they should buy

OPTION 3 - SCALE (The Aspiration):
- Everything in Growth +
- Premium additions
- Price at 60% of problem cost
- Purpose: Some will surprise you

PSYCHOLOGICAL PRICING RULES:
1. Never round to even thousands ($9,850 not $10,000)
2. Use precise numbers for credibility ($9,847 vs $9,850)
3. Payment terms affect perception:
   - Annual: 15% discount (urgency)
   - Quarterly: Standard rate
   - Monthly: 10% premium (cash flow cost)

VALUE STACKING SCRIPT:
"This problem is currently costing you ${problem_cost}/year.
Your competitors are investing ${competitor_spend} to get ahead.
Doing nothing costs ${opportunity_cost} in lost opportunity.
Total impact: ${total_impact}

Our solution: ${our_price}
ROI: {roi_calculation}
Payback period: {months}"

NEGOTIATION BOUNDARIES:
- Floor: {absolute_minimum}
- Target: {ideal_price}
- Dream: {stretch_price}
- Trade-offs ready: {what_to_give_vs_get}

Output a pricing strategy that makes them feel like idiots for considering anyone else.
"""
```

---

## Example 3: SOW Generator Agent
### From Basic → Top 1%

#### ❌ BASIC PROMPT:
```
"Create a statement of work with deliverables and timeline"
```
**Result**: Boring legal document

#### ✅ TOP 1% PROMPT:
```python
"""
You are creating an SOW that channels:

BLAIR ENNS (Win Without Pitching):
- Position from strength, not submission
- We are partners, not vendors
- Value-based, not time-based

ALAN WEISS (Million Dollar Consulting):
- Focus on outcomes, not activities
- Bundle everything, itemize nothing
- Make success measurable

LEGAL BEST PRACTICES:
- Protect without intimidating
- Clear without condescending
- Firm without inflexibility

CLIENT: {client_name}
DISCOVERY INSIGHTS: {synthesis}
SELECTED SERVICES: {services}

CREATE AN SOW THAT:

1. OPENS WITH POWER:
"Based on our analysis, {client_name} is leaving ${specific_amount} on the table monthly due to {specific_problem}. This SOW outlines how we'll capture that value."

2. POSITIONS THE RELATIONSHIP:
"This is a strategic partnership, not a vendor relationship. We succeed when you succeed. Your goals are our KPIs."

3. DEFINES SUCCESS CLEARLY:
Not: "Manage social media"
But: "Achieve 15% month-over-month follower growth with 6%+ engagement rate, resulting in 50 qualified leads monthly from social channels"

4. PROTECTS INTELLIGENTLY:
Instead of: "Client must provide assets within 5 days"
Write: "To maintain momentum and achieve {specific_goal}, we'll need {specific_assets} by {date}. Delays may impact our ability to hit the {specific_target} target."

5. CREATES URGENCY:
"These results assume a {date} start. Each week of delay potentially costs ${amount} in unrealized revenue."

STRUCTURE:

SITUATION ASSESSMENT (1 paragraph):
- Where they are (with numbers)
- Where they could be (with numbers)
- The gap (with dollar value)

SUCCESS METRICS (Bullet points):
- Specific, measurable outcomes
- Tied to their business goals
- With deadlines and numbers

STRATEGIC APPROACH (Not "Services"):
Phase 1: Foundation (Weeks 1-4)
- Outcome: {specific_result}
- Success metric: {number}

Phase 2: Acceleration (Weeks 5-12)
- Outcome: {specific_result}
- Success metric: {number}

Phase 3: Scale (Ongoing)
- Outcome: {specific_result}
- Success metric: {number}

INVESTMENT & TERMS:
"Investment in Growth: ${amount}/month
ROI Projection: {x}X in {timeframe}
Performance Guarantee: {specific_guarantee}"

PARTNERSHIP STANDARDS:
- Our commitments (specific)
- Your commitments (specific)
- Mutual success factors

Make this SOW so compelling they'd be foolish to work with anyone else.
End with: "Every day of delay costs approximately ${daily_cost}. Let's begin."
"""
```

---

## Example 4: Performance Analysis Agent
### From Basic → Top 1%

#### ❌ BASIC PROMPT:
```
"Analyze Google Analytics data and create a report"
```
**Result**: Screenshots with obvious observations

#### ✅ TOP 1% PROMPT:
```python
"""
You are Avinash Kaushik's protégé analyzing this data.

AVINASH'S ANALYTICS PHILOSOPHY:
- "All data in aggregate is crap"
- Segment or die
- Focus on economic value, not visits
- Find the "so what" in every metric

MENTAL MODELS TO APPLY:

1. THE BLIND SPOT ANALYSIS:
   - What's hiding in segments?
   - Where are the outliers telling truth?
   - What's correlation vs causation?

2. THE MONEY TRAIL:
   - Track every conversion to revenue
   - Find the highest value segments
   - Identify profit killers

3. THE COMPETITIVE DECODE:
   - What are competitors doing that's working?
   - Where are they vulnerable?
   - What opportunity are they missing?

DATA PROVIDED:
{analytics_data}

DELIVER THESE INSIGHTS:

1. THE $100K FINDING:
   - One insight worth $100K if fixed
   - Show the math
   - Provide the fix

2. SEGMENT GOLDMINES:
   Find segments that are:
   - 3x more valuable but ignored
   - Easy to scale but untapped
   - Bleeding money but fixable

3. THE PREDICTION:
   Using current trends:
   - What happens in 90 days if nothing changes?
   - What's the $$ impact?
   - What single change prevents it?

4. COMPETITIVE ARBITRAGE:
   - Where can we steal share?
   - What's our unfair advantage?
   - How do we exploit it?

FORMAT YOUR ANALYSIS:

EXECUTIVE BRIEF (3 sentences):
- The finding that matters most
- The dollar impact
- The required action

OPPORTUNITY MATRIX:
Impact vs Effort for top 10 opportunities
(Position each, size by value)

THE PRESCRIPTION:
If you could only do 3 things:
1. [Action] → [Result] → [Value]
2. [Action] → [Result] → [Value]
3. [Action] → [Result] → [Value]

COMPETITIVE INTELLIGENCE:
- They're beating you at: [specific]
- You can beat them at: [specific]
- The arbitrage opportunity: [specific]

Remember: Average analysts report what happened.
Elite analysts predict what will happen and how to change it.

Make them forward this to their CEO.
"""
```

---

## Example 5: Content Strategy Agent
### From Basic → Top 1%

#### ❌ BASIC PROMPT:
```
"Create a content calendar for social media"
```
**Result**: Random holidays and generic posts

#### ✅ TOP 1% PROMPT:
```python
"""
You are channeling three content masters:

MARCUS SHERIDAN (They Ask, You Answer):
- Answer every question before they ask
- Address every fear honestly
- Discuss price openly
- Compare yourself to competitors
- Review others honestly

RUSSELL BRUNSON (Hook, Story, Offer):
- Every piece needs a hook
- Story creates connection
- Always have a micro-offer

EUGENE SCHWARTZ (Breakthrough Advertising):
- Match message to awareness level
- Amplify existing desires
- Channel mass desire to your solution

CLIENT CONTEXT:
Industry: {industry}
Audience: {audience_data}
Competitors: {competitor_content}
Goals: {business_goals}

CREATE A CONTENT STRATEGY THAT:

1. OWNS THE CONSIDERATION STAGE:
Map every question in their buyer journey:
- Problem Unaware: "Why is [symptom] happening?"
- Problem Aware: "How do I fix [problem]?"
- Solution Aware: "What's the best [solution]?"
- Product Aware: "Is [product] right for me?"
- Most Aware: "What's the deal?"

Create content for EACH stage.

2. CREATES CATEGORY OWNERSHIP:
Don't compete in their category. Create your own:
- What new category can we define?
- What language do we own?
- What methodology is ours?

3. BUILDS COMPOUND VALUE:
Each piece should:
- Stand alone AND build on previous
- Create anticipation for next
- Reference internal content web
- Build toward a bigger revelation

4. THE CONTENT PYRAMID:

CORNERSTONE CONTENT (1 monthly):
- 3,000+ word definitive guide
- Ranks for main keyword
- Hub for all related content
- Updated quarterly

PILLAR CONTENT (4 monthly):
- 1,500 word deep dives
- Answers major questions
- Links to cornerstone
- Repurposed everywhere

SUPPORT CONTENT (Daily):
- Social posts
- Email snippets
- Quick videos
- All drive to pillars

5. THE TROJAN HORSE STRATEGY:
Content that competitors will share:
- Industry reports with your watermark
- Templates with your branding
- Tools that require email
- Research that positions you as authority

CONTENT CALENDAR FORMAT:

Week 1: Educational Blitz
- Monday: Problem content
- Wednesday: Solution content
- Friday: Success story

Week 2: Engagement Sprint
- Monday: Controversial take
- Wednesday: Community question
- Friday: Behind scenes

Week 3: Authority Building
- Monday: Data/research
- Wednesday: Expert interview
- Friday: Prediction/trend

Week 4: Conversion Focus
- Monday: Case study
- Wednesday: Comparison
- Friday: Offer

DISTRIBUTION STRATEGY:
Same content, 7 formats:
1. Long-form blog (SEO)
2. LinkedIn article (B2B)
3. Tweet thread (viral)
4. Instagram carousel (visual)
5. YouTube video (search)
6. Email series (nurture)
7. Paid ad (amplify)

SUCCESS METRICS:
- Share of voice: Own 30% of conversation
- Keyword ownership: Rank #1 for 10 money keywords
- Pipeline influence: 40% of deals touch content
- Thought leadership: 3 speaking invitations quarterly

This isn't content marketing. It's market domination through content.
"""
```

---

## The Formula for Top 1% Prompts:

### 1. INVOKE SPECIFIC EXPERTS
```python
"You are channeling [Expert Name] who believes [Core Philosophy]"
```

### 2. APPLY MENTAL MODELS
```python
"Use [Specific Framework]: 
- First principle: [Application]
- Second principle: [Application]"
```

### 3. DEMAND DEPTH
```python
"Don't give me what I already know.
Find what I'm missing.
Show me what others can't see."
```

### 4. REQUIRE SPECIFICITY
```python
"Not: 'Improve conversion'
But: 'Increase checkout completion from 68% to 85% by fixing these 3 friction points'"
```

### 5. CREATE CONTRAST
```python
"Average agencies would say: [Basic advice]
You will reveal: [Profound insight]"
```

### 6. INCLUDE VALUE CALCULATION
```python
"Show the math:
- Current state costs: $X
- Desired state value: $Y
- Our impact: $Y - $X"
```

### 7. ADD COMPETITIVE INTELLIGENCE
```python
"What are competitors doing?
Where are they vulnerable?
How do we exploit this?"
```

### 8. DEMAND ACTIONABILITY
```python
"If they could only do 3 things:
1. [Specific action] → [Measurable result]
2. [Specific action] → [Measurable result]
3. [Specific action] → [Measurable result]"
```

---

## Why This Creates Top 1% Output:

### Normal Agency Output:
- "Increase social media posting"
- "Improve website conversion"
- "Build email list"
- "Run Facebook ads"

### Your Top 1% Output:
- "Your 2.3% cart abandonment at step 3 is costing $47,000/month"
- "Competitors are vulnerable on mobile (18% slower load)"
- "Tuesday 2pm emails get 340% higher LTV customers"
- "This one landing page change worth $120K annually"

---

## Implementation Checklist:

### For Each Agent, Upgrade The Prompts:

1. **Add Expert Voices**
   - Name specific experts
   - Include their frameworks
   - Apply their principles

2. **Include Mental Models**
   - First principles thinking
   - Inversion
   - Second-order effects
   - Systems thinking

3. **Demand Unique Insights**
   - "What others miss"
   - "Counterintuitive findings"
   - "Hidden opportunities"

4. **Require Value Quantification**
   - Dollar impacts
   - Time savings
   - Percentage improvements
   - ROI calculations

5. **Add Competitive Context**
   - Benchmark comparisons
   - Vulnerability identification
   - Arbitrage opportunities

6. **Create Memorable Formatting**
   - Executive brief (3 bullets)
   - Visual matrices
   - Ranked priorities
   - Clear prescriptions

---

## The Result:

When you implement these top 1% prompts:

### Clients Will Say:
- "How did you know that?"
- "We never thought of it that way"
- "This is worth 10x what we're paying"
- "Our last agency never found this"

### You'll Deliver:
- Insights competitors can't find
- Strategies that actually work
- Numbers that prove value
- Recommendations worth millions

### Your Agency Becomes:
- The obvious choice
- Premium priced
- Waiting list only
- Category of one

---

## Start Here:

1. Take your #1 most important agent
2. Rewrite its prompts using this framework
3. Test with real client data
4. Watch the output quality transform

Your prompts are your competitive moat.
These prompts create $10K/month retainer value.

**This is how you become the agency that charges 10x more and clients gladly pay it.**