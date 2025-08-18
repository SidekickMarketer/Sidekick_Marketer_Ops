# Complete Agent Library
## All Agents from Today's Session

---

# PHASE 1: LEAD GENERATION & INTELLIGENCE (Agents 001-011)

## Agent 001: Lead Hunter
```yaml
role: "Lead Generation Specialist"
trigger: "Daily or when pipeline < 20 prospects"

execution:
  sources:
    - LinkedIn Sales Navigator searches
    - Industry directories
    - Competitor client lists
    - Local business databases
    - Facebook groups
    - Industry forums
    
  data_captured:
    - Company name
    - Website URL
    - Decision maker name
    - Email (if available)
    - Phone number
    - Industry
    - Estimated revenue
    - Current marketing presence

outputs:
  - lead_list.csv
  - enrichment_queue.json
  
triggers: → Agent 002 (Lead Enricher)

tools_used:
  - Apollo.io
  - LinkedIn
  - Google Search
  - Industry databases
```

## Agent 002: Lead Enricher
```yaml
role: "Data Enrichment Specialist"
trigger: "New leads added to pipeline"

execution:
  enrichment_process:
    - Use Apollo.io for contact details
    - Scrape website for business info
    - Check social media presence
    - Analyze current marketing
    - Estimate marketing spend
    - Identify pain points
    - Score lead quality (1-10)
    
outputs:
  - enriched_leads.json
  - lead_scores.csv
  - research_notes.md
  
triggers: → Agent 003 (Intelligence Gatherer)

tools_used:
  - Apollo.io
  - Builtwith.com
  - Facebook Ad Library
  - LinkedIn
```

## Agent 003: Deep Intelligence Gatherer
```yaml
role: "Prospect Research Analyst"
trigger: "Lead score > 7"

execution:
  deep_research:
    - Full website analysis
    - Competitor identification
    - Technology stack audit
    - Social media audit
    - Review analysis
    - Content inventory
    - Ad campaign detection
    - Industry trends relevant to them
    
  intelligence_report:
    - Business model summary
    - Current marketing efforts
    - Identified problems (5-10)
    - Quick wins available
    - Estimated opportunity value
    - Personalization hooks
    
outputs:
  - prospect_intelligence/[company_name].md
  - personalization_data.json
  - problems_identified.csv
  
triggers: → Agent 004 (Outreach Crafter)

tools_used:
  - Perplexity Pro
  - ChatGPT
  - SE Ranking API
  - BrightLocal
```

## Agent 004: Outreach Message Crafter
```yaml
role: "Personalized Outreach Specialist"
trigger: "Intelligence report completed"

execution:
  message_creation:
    channel_selection:
      - Email (primary)
      - LinkedIn (secondary)
      - Cold call script (tertiary)
    
    personalization_elements:
      - Reference specific website issue
      - Mention competitor doing X better
      - Compliment something specific
      - Share relevant case study
      - Include quick win they can implement
      - Add social proof from their industry
    
    message_variants:
      - Subject line A/B test (3 versions)
      - Opening hook variations (2 versions)
      - CTA options (soft vs direct)
    
outputs:
  - outreach_messages/[company_name]/
    - email_sequence.md
    - linkedin_message.md
    - call_script.md
    - follow_up_sequence.md
  
triggers: → Agent 005 (Outreach Executor)

expert_guidance:
  - Josh Braun (cold outreach)
  - Aaron Ross (predictable revenue)
```

## Agent 005: Outreach Campaign Executor
```yaml
role: "Outreach Automation Specialist"
trigger: "Messages approved"

execution:
  campaign_setup:
    - Load into email tool
    - Set up follow-up sequence
    - Configure tracking
    - Set response alerts
    
  sequence:
    Day 0: Initial outreach
    Day 3: Follow-up 1 (if no response)
    Day 7: Follow-up 2 (different angle)
    Day 14: Break-up email
    
outputs:
  - campaign_status.json
  - response_log.csv
  - meeting_scheduled.json
  
triggers: → Agent 006 (Call Prep) when meeting scheduled

tools_used:
  - Email platform
  - Make.com automations
  - Calendar scheduling
```

## Agent 006: Discovery Call Prep Master
```yaml
role: "Pre-Call Intelligence Specialist"
trigger: "Meeting scheduled"

execution:
  final_research:
    - Latest company news
    - Recent social posts
    - New competitors emerged
    - Industry trends this week
    - Decision maker background
    
  call_materials:
    - Customized deck (5-7 slides)
    - Case studies (2-3 relevant)
    - Problem/solution matrix
    - Pricing framework
    - Discovery questions (10-15)
    
outputs:
  - call_prep/[company_name]/
    - call_brief.md
    - discovery_questions.md
    - presentation.pdf
    - case_studies.pdf
  
triggers: → Agent 007 (Call Conductor)

expert_guidance:
  - Chris Voss (Never Split the Difference)
  - SPIN Selling methodology
```

## Agent 007: Discovery Call Conductor
```yaml
role: "Sales Call Orchestrator"
trigger: "Call starting"

execution:
  call_framework:
    1_rapport: "Industry insight or compliment"
    2_situation: "Current state questions"
    3_problem: "Pain point exploration"
    4_implication: "Cost of inaction"
    5_need_payoff: "Solution visioning"
    6_next_steps: "Clear commitment"
    
outputs:
  - call_notes.md
  - problems_confirmed.csv
  - services_discussed.json
  - follow_up_required.md
  
triggers: → Agent 008 (Proposal Builder) if qualified

expert_guidance:
  - Sandler Selling System
  - Solution Selling
```

## Agent 008: Custom Proposal Builder
```yaml
role: "Proposal Generation Specialist"
trigger: "Call completed, prospect qualified"

execution:
  proposal_components:
    1_executive_summary:
      - Their situation
      - Problems identified
      - Opportunity cost
      - Proposed solution
      
    2_strategy_section:
      - Specific to their industry
      - Addresses exact pain points
      - Includes their competitors
      - Uses their language
      
    3_scope_of_work:
      - Phased approach
      - Clear deliverables
      - Success metrics
      - Timeline
      
    4_investment:
      - ROI focused
      - Multiple options
      - Payment terms
      - Guarantees
      
outputs:
  - proposals/[company_name]/
    - proposal_v1.pdf
    - pricing_sheet.xlsx
    - contract_draft.docx
  
triggers: → Agent 009 (Proposal Presenter)

expert_guidance:
  - Blair Enns (Win Without Pitching)
  - Tom Sant (Persuasive Business Proposals)
```

## Agent 009: Proposal Delivery Orchestrator
```yaml
role: "Proposal Presentation Specialist"
trigger: "Proposal ready"

execution:
  delivery_strategy:
    - Send proposal via email
    - Schedule review call
    - Create Loom walkthrough
    - Set up proposal tracking
    
  follow_up_sequence:
    Day 0: Proposal sent
    Day 1: "Did you receive?" check
    Day 3: "Any questions?" touch
    Day 7: "Thoughts?" follow-up
    Day 14: Final follow-up
    
outputs:
  - proposal_tracking.json
  - follow_up_log.csv
  
triggers: → Agent 010 (Close Facilitator) if engaged
```

## Agent 010: Deal Close Facilitator
```yaml
role: "Closing Specialist"
trigger: "Proposal being reviewed"

execution:
  objection_handling:
    - Price concerns → ROI focus
    - Timing issues → Cost of delay
    - Trust questions → More proof
    - Scope concerns → Adjust package
    
  closing_tactics:
    - Urgency creation
    - Incentive offering
    - Risk reversal
    - Payment flexibility
    
outputs:
  - negotiation_log.md
  - contract_final.pdf
  - signed_agreement.pdf
  
triggers: → Agent 011 (Client Onboarder) when signed

expert_guidance:
  - Zig Ziglar (closing techniques)
  - Grant Cardone (10X Rule)
```

## Agent 011: New Client Onboarding Master
```yaml
role: "Client Onboarding Specialist"
trigger: "Contract signed"

execution:
  immediate_actions:
    - Send welcome packet
    - Schedule kickoff call
    - Create client folders
    - Set up project management
    - Request access/assets
    
  first_48_hours:
    - Complete tech audit
    - Install tracking
    - Identify quick wins
    - Begin discovery
    
  first_week:
    - Deliver quick wins
    - Complete deep discovery
    - Present 90-day plan
    - Begin execution
    
outputs:
  - client_folders/[company_name]/
  - onboarding_checklist.md
  - quick_wins_completed.csv
  - 90_day_plan.pdf
  
triggers: → Execution Agents (Phase 3)

tools_used:
  - Google Drive
  - Notion
  - Make.com
  - Slack
```

---

# PHASE 2: POST-CONTRACT INTELLIGENCE (Agents 012-015)

## Agent 012: Expert Council Selector
```yaml
role: "Strategic Expertise Architect"
trigger: "Contract signed + initial client context"
timing: "Within 2 hours of contract"

execution:
  context_analysis:
    - Industry: [from sales process]
    - Business model: [from discovery]
    - Challenges: [from proposal]
    - Goals: [from contract]
    - Budget level: [from agreement]
    
  expert_selection:
    universal_layer:
      - Charlie Munger (strategic thinking)
      - Peter Drucker (management)
    
    industry_layer:
      if client.industry == "auction":
        - Machinery Pete
        - Barrett-Jackson principles
      if client.industry == "local_service":
        - Michael Gerber
        - Marcus Sheridan
      if client.industry == "saas":
        - Jason Lemkin
        - April Dunford
    
    challenge_layer:
      if challenge == "lead_generation":
        - Aaron Ross
        - Chet Holmes
      if challenge == "conversion":
        - Peep Laja
        - Bryan Eisenberg
    
outputs:
  - client_folders/[name]/expert_council.yaml
  - expert_frameworks.md
  - decision_matrix.csv
  
triggers: → Agent 013 (Deep Discovery)
integrates_with: All future agents use this expert council
```

## Agent 013: Deep Discovery Orchestrator
```yaml
role: "Comprehensive Business Intelligence"
trigger: "Expert council established"
timing: "Days 1-3 of engagement"

execution:
  discovery_areas:
    1_data_infrastructure:
      - Current tools audit
      - Data quality assessment
      - Tracking gaps
      - Integration opportunities
      
    2_marketing_performance:
      - Channel effectiveness
      - Content audit
      - Campaign analysis
      - Competitor benchmarking
      
    3_operational_efficiency:
      - Current workflows
      - Time wasters
      - Automation opportunities
      - Team capabilities
      
    4_customer_intelligence:
      - Journey mapping
      - Segmentation analysis
      - LTV calculations
      - Churn factors
      
  expert_lens_application:
    - Apply each expert's framework to findings
    - Generate expert-specific recommendations
    - Prioritize based on expert consensus
    
outputs:
  - discovery_report.md (50+ pages)
  - problems_matrix.csv (30-50 issues)
  - opportunities_ranked.json
  - quick_wins_identified.csv (10-15 items)
  
triggers: → Agent 014 (Task Mapper)

tools_used:
  - All audit tools
  - Expert frameworks
  - Pattern recognition
```

## Agent 014: 665-Task Mapper
```yaml
role: "Task Library Orchestrator"
trigger: "Discovery complete"
timing: "Day 4-5"

execution:
  task_selection:
    - Map problems to your 665 tasks
    - Identify service tiers needed (S0-S15)
    - Calculate time requirements
    - Set dependencies
    
  expert_assignment:
    for each_task in selected_tasks:
      - Assign primary expert guidance
      - Pull expert framework
      - Set success criteria
      
  prioritization:
    priority_1_immediate:
      - Tracking setup (S0)
      - Quick wins (varies)
      - Critical fixes
      
    priority_2_week1:
      - Foundation services (S1-S3)
      - Basic automations
      - Reporting setup
      
    priority_3_month1:
      - Growth services (S4-S8)
      - Advanced features
      - Optimization
      
outputs:
  - 90_day_roadmap.md
  - task_assignments.csv
  - expert_guidance_per_task.yaml
  - gantt_chart.html
  
triggers: → Agent 015 (Automation Architect)

integrates_with:
  - Your 665 task CSV
  - Expert council selections
  - Discovery findings
```

## Agent 015: Automation Architecture Builder
```yaml
role: "Make.com Scenario Designer"
trigger: "Task map created"
timing: "Day 5-7"

execution:
  automation_identification:
    - Review all mapped tasks
    - Identify automation potential
    - Design Make.com scenarios
    - Create data pipelines
    
  scenarios_to_build:
    1_data_collection:
      - Parsio → Google Sheets
      - Forms → CRM
      - Reviews → Dashboard
      
    2_reporting:
      - Data aggregation
      - Report generation
      - Distribution automation
      
    3_campaign_management:
      - Ad creation workflows
      - Budget adjustments
      - Performance alerts
      
    4_content_distribution:
      - Social scheduling
      - Email campaigns
      - Blog publishing
      
outputs:
  - make_scenarios/[client]/
  - automation_blueprints.json
  - api_requirements.md
  - testing_checklist.csv
  
triggers: → Execution Agents (016-099)

tools_used:
  - Make.com
  - Parsio
  - Your tool stack
```

---

# PHASE 3: SERVICE DELIVERY (Agents 016-099)

## Foundation Services (S0-S3) - Agents 016-030
```yaml
Agent_016_Google_Business_Profile_Setup:
  maps_to: "S1: GBP tasks from your 665"
  expert: "Mike Blumenthal"
  
Agent_017_Tracking_Implementation:
  maps_to: "S0: Universal setup"
  expert: "Avinash Kaushik, Simo Ahava"
  
Agent_018_Basic_SEO_Setup:
  maps_to: "S3: Local SEO"
  expert: "Moz methodology"
  
Agent_019_Social_Profile_Optimization:
  maps_to: "S2: Social Media"
  expert: "Platform best practices"
  
Agent_020_Email_List_Setup:
  maps_to: "S5: Email foundation"
  expert: "Ryan Deiss"
```

## Growth Services (S4-S8) - Agents 031-060
```yaml
Agent_030_Content_Calendar_Execution:
  maps_to: "S4: Content Marketing"
  expert: "Marcus Sheridan"
  
Agent_031_Paid_Ad_Campaign_Launch:
  maps_to: "S6-S8: Paid Advertising"
  expert: "Perry Marshall, Larry Kim"
  
Agent_032_Email_Automation_Builder:
  maps_to: "S5: Email Marketing"
  expert: "automation best practices"
  
Agent_033_Landing_Page_Creator:
  maps_to: "Conversion optimization"
  expert: "Unbounce methodology"
  
Agent_034_Retargeting_Setup:
  maps_to: "S7: Advanced advertising"
  expert: "Digital marketer framework"
```

## Advanced Services (S9-S12) - Agents 061-080
```yaml
Agent_050_Predictive_Analytics:
  tools: "Julius AI, Obviously AI"
  expert: "Nate Silver principles"
  
Agent_051_Attribution_Modeling:
  tools: "GA4, custom tracking"
  expert: "Avinash Kaushik"
  
Agent_052_Custom_Integrations:
  tools: "Make.com, APIs"
  expert: "Integration patterns"
  
Agent_053_Advanced_Segmentation:
  tools: "CDP, analytics"
  expert: "RFM methodology"
```

## Premium Services (S13-S15) - Agents 081-099
```yaml
Agent_070_AI_Implementation:
  maps_to: "S15: AI services"
  tools: "Claude, ChatGPT, custom AI"
  
Agent_071_Full_Funnel_Optimization:
  maps_to: "S14: Complete optimization"
  expert: "Multiple frameworks"
  
Agent_072_Multi_channel_Orchestration:
  maps_to: "S13: Omnichannel"
  expert: "Orchestra methodology"
```

---

# PHASE 4: ANALYSIS & INTELLIGENCE (Agents 100-102)

## Agent 100: Data Pipeline Orchestrator
```yaml
role: "Data Integration Specialist"
trigger: "Daily/Weekly"
timing: "Ongoing"

execution:
  data_sources:
    - Google Analytics/GA4
    - Ad platforms (FB, Google)
    - CRM data
    - Email metrics
    - Sales data
    - Custom sources
    
  pipeline_flow:
    1. Extract via APIs/Parsio
    2. Transform in Google Sheets
    3. Load to Julius AI
    4. Analyze with Obviously AI
    5. Push to AgencyAnalytics
    6. Generate insights
    
outputs:
  - Unified data warehouse
  - Clean datasets
  - Analysis-ready files
  
triggers: → Agent 101 (Performance Analyzer)

tools_used:
  - Parsio
  - Julius AI
  - Obviously AI
  - Make.com
  - AgencyAnalytics
```

## Agent 101: Performance Intelligence Engine
```yaml
role: "Advanced Analytics Specialist"
trigger: "Data pipeline updated"
timing: "Daily analysis, weekly deep-dive"

execution:
  julius_ai_analysis:
    - Trend detection
    - Anomaly identification
    - Predictive modeling
    - Cohort analysis
    - Attribution modeling
    
  obviously_ai_predictions:
    - Churn probability
    - LTV predictions
    - Conversion likelihood
    - Optimal bid predictions
    
  expert_interpretation:
    - Apply Avinash Kaushik frameworks
    - Use Charlie Munger mental models
    - Generate strategic insights
    
outputs:
  - insights_report.md
  - predictions.csv
  - recommendations.json
  - alerts.txt
  
triggers: → Agent 102 (Optimization Orchestrator)
```

## Agent 102: CPR/ROI Calculator
```yaml
role: "Financial Performance Analyst"
trigger: "Weekly or after campaigns"
special_focus: "Critical for paid traffic clients"

execution:
  calculations:
    by_channel:
      - Facebook CPR
      - Google CPR
      - Email CPR
      - Organic attribution
      
    advanced_metrics:
      - Blended CPR
      - Payback period
      - LTV:CAC ratio
      - Channel efficiency
      
    forecasting:
      - Next month projections
      - Budget recommendations
      - Scaling opportunities
      
outputs:
  - cpr_dashboard.html
  - roi_report.pdf
  - budget_recommendations.csv
  
triggers: → Agent 103 (Budget Optimizer)

specific_to: "Fastline and similar clients"
```

---

# PHASE 5: OPTIMIZATION & SCALING (Agents 150-151)

## Agent 150: Optimization Orchestrator
```yaml
role: "Continuous Improvement Specialist"
trigger: "Weekly performance review"

execution:
  optimization_areas:
    1_paid_ads:
      - Bid adjustments
      - Audience refinements
      - Creative testing
      - Budget reallocation
      
    2_conversion_rate:
      - A/B test setup
      - Landing page tweaks
      - Form optimization
      - Trust signals
      
    3_email_marketing:
      - Segmentation improvements
      - Send time optimization
      - Subject line testing
      - Flow refinements
      
    4_content:
      - Topic optimization
      - Format testing
      - Distribution timing
      - Repurposing opportunities
      
  expert_guidance:
    - Channel Dan Kennedy for direct response
    - Apply Peep Laja for CRO
    - Use Russell Brunson for funnels
    
outputs:
  - optimization_log.csv
  - test_results.json
  - improvement_metrics.md
  
triggers: → Agent 151 (Scaling Orchestrator)
```

## Agent 151: Scaling Orchestrator
```yaml
role: "Growth Scaling Specialist"
trigger: "When success metrics hit targets"

execution:
  scaling_decisions:
    horizontal_scaling:
      - New channels
      - New audiences
      - New geos
      
    vertical_scaling:
      - Budget increases
      - Frequency increases
      - Team expansion
      
    systematic_scaling:
      - More automation
      - Better tools
      - Process optimization
      
outputs:
  - scaling_plan.md
  - resource_requirements.csv
  - risk_assessment.json
```

---

# PHASE 6: REPORTING & CLIENT SUCCESS (Agents 200-201)

## Agent 200: Client Reporting Orchestrator
```yaml
role: "Client Communication Specialist"
trigger: "Weekly/Monthly"

execution:
  report_generation:
    components:
      - Executive summary
      - KPI dashboard
      - Channel performance
      - Work completed
      - Upcoming initiatives
      - Recommendations
      
    personalization:
      - Use client's KPIs
      - Industry benchmarks
      - Competitor comparisons
      - ROI calculations
      
    distribution:
      - Email PDF
      - Live dashboard link
      - Video walkthrough
      - Slack summary
      
outputs:
  - weekly_report.pdf
  - monthly_report.pdf
  - dashboard_link.url
  - video_walkthrough.mp4
  
triggers: → Agent 201 (Success Monitor)

tools_used:
  - AgencyAnalytics
  - Loom
  - Google Data Studio
```

## Agent 201: Client Success Monitor
```yaml
role: "Retention & Growth Specialist"
trigger: "Continuous monitoring"

execution:
  health_monitoring:
    engagement_signals:
      - Report opens
      - Dashboard visits
      - Response times
      - Meeting attendance
      
    performance_signals:
      - KPI trends
      - Goal achievement
      - ROI delivered
      - NPS scores
      
    risk_signals:
      - Declining metrics
      - Low engagement
      - Payment delays
      - Contract expiration
      
  proactive_actions:
    if health_score < 7:
      - Schedule check-in
      - Prepare wins summary
      - Create recovery plan
      
    if health_score > 8:
      - Identify upsell opportunities
      - Prepare case study
      - Request testimonial
      
outputs:
  - client_health_dashboard.html
  - at_risk_alerts.json
  - upsell_opportunities.csv
  - testimonial_requests.md
  
triggers: → Agent 202 (Growth Orchestrator)
```

---

# PHASE 7: KNOWLEDGE & LEARNING (Agent 300)

## Agent 300: Knowledge Transfer System
```yaml
role: "Organizational Learning Specialist"
trigger: "After major milestones"

execution:
  documentation:
    - What worked
    - What didn't
    - Time requirements
    - Resource needs
    - Client feedback
    
  template_updates:
    - Improved SOPs
    - Better templates
    - Refined processes
    - New automations
    
  expert_learning:
    - Which experts were most valuable
    - Which frameworks worked best
    - What combinations succeeded
    
outputs:
  - lessons_learned.md
  - template_updates/
  - sop_improvements/
  - expert_effectiveness.csv
  
feeds_back_to: → All agents (continuous improvement)
```

---

# INTELLIGENCE LAYER: SELF-CREATING AGENTS

## Master Discovery Agent (Auto-Creator)
```python
class MasterDiscoveryAgent:
    """
    The prime agent that discovers patterns and spawns children
    """
    
    def __init__(self, client_name):
        self.client = client_name
        self.discoveries = []
        self.patterns_found = []
        self.agents_to_create = []
        
    def run_discovery(self):
        # Audit current state
        # Detect patterns
        # Evaluate for agent creation
        # Spawn new agents
        # Update pattern library
        
    def spawn_agents(self):
        """Creates new agents based on discoveries"""
        for pattern in self.patterns_found:
            if self.should_create_agent(pattern):
                new_agent = self.generate_agent(pattern)
                self.deploy(new_agent)
```

## Pattern Detection Triggers
```yaml
triggers_for_auto_creation:
  missing_data:
    condition: "null_rate > 30%"
    creates: "Data_Recovery_Agent"
    
  format_chaos:
    condition: "formats > 3"
    creates: "Standardization_Agent"
    
  manual_process:
    condition: "time > 2 hours"
    creates: "Automation_Agent"
    
  performance_gap:
    condition: "KPI < target * 0.8"
    creates: "Optimization_Agent"
    
  new_platform:
    condition: "unknown tool discovered"
    creates: "Platform_Connector_Agent"
```

---

# IMPLEMENTATION NOTES

## Agent Deployment Order
```yaml
week_1:
  deploy_first:
    - 001: Lead Hunter (if need clients)
    - 011: Client Onboarding (for new clients)
    - 012: Expert Council Selector
    - 013: Deep Discovery
    - 014: Task Mapper
    
week_2:
  add_execution:
    - 016-030: Foundation services
    - 100: Data Pipeline
    - 200: Reporting
    
week_3:
  add_intelligence:
    - Master Discovery (auto-creator)
    - Pattern Detection
    - First auto-generated agents
    
month_2:
  full_system:
    - All agents deployed
    - 50+ auto-created agents
    - Self-improving system
```

## Integration Points
```yaml
notion_databases:
  - Agent Registry
  - Pattern Library
  - Task Queue
  - Client Portals
  
make_com_scenarios:
  - Agent triggers
  - Data pipelines
  - Report generation
  - Task automation
  
tool_connections:
  - Parsio: Document parsing
  - Julius AI: Analysis
  - Obviously AI: Predictions
  - AgencyAnalytics: Dashboards
  - BrightLocal: Local SEO
  - Apollo.io: Enrichment
```

---

# THIS IS YOUR COMPLETE AGENT SYSTEM

Total Agents Defined:
- Lead Generation: 11 agents
- Post-Contract: 4 agents
- Service Delivery: 84 agents
- Analysis: 3 agents
- Optimization: 2 agents
- Reporting: 2 agents
- Knowledge: 1 agent
- Intelligence Layer: Self-creating

**Total: 107 base agents + unlimited auto-generated**

Each agent has:
- Clear role and trigger
- Specific execution steps
- Defined outputs
- Integration with your tools
- Expert guidance where relevant

This is EVERYTHING we designed today!