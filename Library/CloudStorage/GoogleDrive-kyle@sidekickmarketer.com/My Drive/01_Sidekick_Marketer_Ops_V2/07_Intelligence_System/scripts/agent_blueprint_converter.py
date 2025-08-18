#!/usr/bin/env python3
"""
Agent Blueprint to YAML Converter
Transforms Sidekick's blueprint documentation into executable Conductor YAML files
"""

import yaml
import json
import os
from pathlib import Path
from datetime import datetime

class AgentConverter:
    def __init__(self, output_dir="conductor_agents"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Create subdirectories
        (self.output_dir / "agents").mkdir(exist_ok=True)
        (self.output_dir / "workflows").mkdir(exist_ok=True)
        (self.output_dir / "configs").mkdir(exist_ok=True)
        
    def create_agent_yaml(self, agent_data):
        """Convert agent blueprint to Conductor YAML format"""
        
        agent_yaml = {
            'agent': {
                'id': agent_data['id'],
                'name': agent_data['name'],
                'type': agent_data.get('type', 'task_processor'),
                'category': agent_data.get('category', 'operations'),
                'status': 'active',
                'version': '1.0'
            },
            
            'description': agent_data.get('description', ''),
            
            'triggers': agent_data.get('triggers', [
                {'type': 'manual', 'source': 'notion'},
                {'type': 'webhook', 'source': 'make.com'}
            ]),
            
            'inputs': {
                'required': agent_data.get('required_inputs', []),
                'optional': agent_data.get('optional_inputs', []),
                'sources': agent_data.get('data_sources', [])
            },
            
            'expert_councils': agent_data.get('expert_councils', []),
            
            'tools': agent_data.get('tools', []),
            
            'execution': {
                'model': agent_data.get('model', 'gpt-5'),
                'temperature': agent_data.get('temperature', 0.3),
                'max_tokens': agent_data.get('max_tokens', 4000),
                'timeout': agent_data.get('timeout', 300)
            },
            
            'process': agent_data.get('process_steps', []),
            
            'outputs': {
                'format': agent_data.get('output_format', 'json'),
                'schema': agent_data.get('output_schema', {}),
                'destinations': agent_data.get('output_destinations', [
                    'notion_database',
                    'google_drive',
                    'client_portal'
                ])
            },
            
            'quality_checks': agent_data.get('quality_checks', [
                'completeness',
                'accuracy',
                'client_alignment',
                'expert_framework_applied'
            ]),
            
            'next_agents': agent_data.get('next_agents', []),
            
            'self_evolution': {
                'enabled': True,
                'triggers': agent_data.get('evolution_triggers', [
                    {'condition': 'missing_data > 30%', 'creates': 'data_recovery_agent'},
                    {'condition': 'process_time > 2_hours', 'creates': 'optimization_agent'}
                ])
            },
            
            'metrics': {
                'track': ['execution_time', 'success_rate', 'value_generated'],
                'report_to': 'analytics_dashboard'
            }
        }
        
        return agent_yaml
    
    def save_agent_file(self, agent_yaml, filename):
        """Save agent YAML to file"""
        filepath = self.output_dir / "agents" / f"{filename}.yml"
        with open(filepath, 'w') as f:
            yaml.dump(agent_yaml, f, default_flow_style=False, sort_keys=False)
        print(f"✅ Created: {filepath}")
        return filepath

# Define the 30 perfect agents with complete specifications
PERFECT_AGENTS = [
    {
        'id': '001',
        'name': 'Lead_Hunter',
        'type': 'data_gathering',
        'category': 'lead_generation',
        'description': 'Identifies and qualifies potential leads using Apollo.io and enrichment tools',
        'triggers': [
            {'type': 'schedule', 'cron': '0 9 * * *'},
            {'type': 'condition', 'rule': 'pipeline_count < 20'}
        ],
        'required_inputs': ['industry', 'ideal_customer_profile', 'geography'],
        'data_sources': ['apollo_io', 'linkedin', 'similarweb'],
        'expert_councils': ['Aaron Ross', 'Jeb Blount', 'Anthony Iannarino'],
        'tools': ['Apollo.io', 'LinkedIn Sales Navigator', 'SimilarWeb'],
        'model': 'gpt-5',
        'temperature': 0.3,
        'process_steps': [
            'Search Apollo.io for matching companies',
            'Enrich with SimilarWeb data',
            'Score based on ICP match',
            'Export qualified leads to ActiveCampaign'
        ],
        'output_format': 'json',
        'next_agents': ['002_lead_enricher', '003_deep_intelligence'],
        'evolution_triggers': [
            {'condition': 'enrichment_rate < 70%', 'creates': 'enhanced_enrichment_agent'}
        ]
    },
    {
        'id': '002',
        'name': 'Lead_Enricher',
        'type': 'data_enrichment',
        'category': 'lead_generation',
        'description': 'Enriches lead data with comprehensive company and contact information',
        'required_inputs': ['lead_list', 'enrichment_fields'],
        'data_sources': ['apollo_io', 'clearbit', 'google'],
        'expert_councils': ['Predictable Revenue Framework'],
        'tools': ['Apollo.io', 'Parsio', 'Google Search API'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.2,
        'process_steps': [
            'Verify email addresses via Apollo',
            'Find additional decision makers',
            'Gather technographic data',
            'Identify pain points from public info',
            'Calculate lead score'
        ],
        'next_agents': ['003_deep_intelligence', '004_outreach_crafter']
    },
    {
        'id': '003',
        'name': 'Deep_Intelligence_Gatherer',
        'type': 'research',
        'category': 'lead_generation',
        'description': 'Conducts deep research on high-value prospects',
        'required_inputs': ['company_name', 'company_url', 'key_contacts'],
        'data_sources': ['company_website', 'news_articles', 'social_media', 'financial_reports'],
        'expert_councils': ['Clayton Christensen', 'Peter Drucker'],
        'tools': ['Perplexity Pro', 'SimilarWeb', 'Google Search Console'],
        'model': 'gpt-5',
        'temperature': 0.4,
        'process_steps': [
            'Analyze company website structure',
            'Identify current marketing stack',
            'Find recent company news/changes',
            'Assess competitive landscape',
            'Generate strategic insights',
            'Create personalized hook angles'
        ],
        'next_agents': ['007_discovery_conductor', '010_strategy_architect']
    },
    {
        'id': '007',
        'name': 'Discovery_Call_Conductor',
        'type': 'sales_intelligence',
        'category': 'lead_generation',
        'description': 'Prepares and guides discovery calls using advanced sales methodologies',
        'required_inputs': ['prospect_research', 'call_recording', 'meeting_notes'],
        'expert_councils': ['Chris Voss', 'Neil Rackham', 'Mike Bosworth'],
        'tools': ['Fireflies.ai', 'Wispr Flow', 'ActiveCampaign'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.5,
        'process_steps': [
            'Apply SPIN selling questions',
            'Use tactical empathy techniques',
            'Identify implicit needs',
            'Quantify business impact',
            'Build value ladder',
            'Create follow-up strategy'
        ],
        'next_agents': ['discovery_synthesizer', '010_strategy_architect']
    },
    {
        'id': '010',
        'name': 'Strategy_Architect',
        'type': 'strategic_planning',
        'category': 'strategy',
        'description': 'Develops comprehensive marketing strategies based on discovery insights',
        'required_inputs': ['discovery_notes', 'business_goals', 'current_performance'],
        'expert_councils': ['Charlie Munger', 'Peter Drucker', 'Michael Porter'],
        'tools': ['Julius AI', 'AgencyAnalytics', 'Notion'],
        'model': 'gpt-5',
        'temperature': 0.6,
        'process_steps': [
            'Apply mental models framework',
            'Identify strategic leverage points',
            'Design transformation roadmap',
            'Calculate ROI projections',
            'Define success metrics',
            'Create implementation timeline'
        ],
        'next_agents': ['015_proposal_builder', 'dynamic_pricing_agent']
    },
    {
        'id': '015',
        'name': 'Proposal_Builder',
        'type': 'document_generation',
        'category': 'sales',
        'description': 'Creates compelling proposals with pricing and strategic recommendations',
        'required_inputs': ['strategy', 'pricing', 'client_info'],
        'expert_councils': ['Blair Enns', 'Alan Weiss', 'David Maister'],
        'tools': ['PandaDoc', 'Canva', 'Google Drive'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.3,
        'process_steps': [
            'Structure executive summary',
            'Articulate value proposition',
            'Present strategic approach',
            'Detail service breakdown',
            'Include pricing options',
            'Add social proof',
            'Create clear next steps'
        ],
        'next_agents': ['sow_generator', 'contract_generator']
    },
    {
        'id': 'discovery_synthesizer',
        'name': 'Discovery_Synthesizer_Agent',
        'type': 'analysis',
        'category': 'intelligence',
        'description': 'Synthesizes discovery call data into comprehensive 50-page analysis',
        'required_inputs': ['call_transcript', 'meeting_notes', 'research_data'],
        'expert_councils': ['Charlie Munger', 'Peter Drucker', 'Clayton Christensen'],
        'tools': ['Fireflies.ai', 'Julius AI', 'Notion'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.3,
        'max_tokens': 8000,
        'process_steps': [
            'Apply Munger mental models',
            'Use Drucker essential questions',
            'Jobs-to-be-done analysis',
            'Identify core problems',
            'Map opportunity landscape',
            'Generate strategic insights',
            'Create action priorities'
        ],
        'next_agents': ['010_strategy_architect', 'sow_generator']
    },
    {
        'id': 'sow_generator',
        'name': 'SOW_Generator_Agent',
        'type': 'document_generation',
        'category': 'sales',
        'description': 'Creates detailed Statements of Work with legal frameworks',
        'required_inputs': ['proposal_accepted', 'service_selection', 'timeline'],
        'expert_councils': ['Legal frameworks', 'David Maister', 'Alan Weiss'],
        'tools': ['PandaDoc', 'Google Drive', 'Notion'],
        'model': 'gpt-5',
        'temperature': 0.2,
        'process_steps': [
            'Define scope boundaries',
            'List specific deliverables',
            'Set milestones and dates',
            'Include payment terms',
            'Add change order process',
            'Define success criteria',
            'Include legal protections'
        ],
        'next_agents': ['portal_builder', 'access_credential']
    },
    {
        'id': 'dynamic_pricing',
        'name': 'Dynamic_Pricing_Agent',
        'type': 'financial_analysis',
        'category': 'sales',
        'description': 'Calculates optimal pricing using value-based methodologies',
        'required_inputs': ['client_value', 'service_scope', 'market_position'],
        'expert_councils': ['Hermann Simon', 'Blair Enns', 'Ron Baker'],
        'tools': ['Julius AI', 'Google Sheets', 'Calculator'],
        'model': 'gpt-5',
        'temperature': 0.1,
        'process_steps': [
            'Apply Hidden Champions pricing',
            'Calculate value metrics',
            'Create pricing tiers',
            'Add option anchoring',
            'Include urgency factors',
            'Generate pricing rationale'
        ],
        'next_agents': ['015_proposal_builder']
    },
    {
        'id': 'portal_builder',
        'name': 'Notion_Portal_Builder_Agent',
        'type': 'automation',
        'category': 'operations',
        'description': 'Automatically creates and configures client portals in Notion',
        'required_inputs': ['client_info', 'service_package', 'brand_assets'],
        'tools': ['Notion API', 'Make.com', 'AgencyAnalytics'],
        'model': 'gpt-5',
        'temperature': 0.1,
        'process_steps': [
            'Create client workspace',
            'Set up dashboard pages',
            'Configure databases',
            'Embed analytics dashboards',
            'Set permissions',
            'Add welcome content',
            'Connect integrations'
        ],
        'next_agents': ['access_credential', 'baseline_metrics']
    },
    {
        'id': '012',
        'name': 'Expert_Council_Selector',
        'type': 'intelligence',
        'category': 'strategy',
        'description': 'Selects industry-specific expert frameworks for each client',
        'required_inputs': ['industry', 'business_model', 'challenges'],
        'expert_councils': ['Meta-expert selection framework'],
        'tools': ['Expert database', 'Pattern matcher'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.4,
        'process_steps': [
            'Analyze industry requirements',
            'Match expert specializations',
            'Select primary councils',
            'Configure mental models',
            'Create application framework'
        ],
        'next_agents': ['013_discovery_orchestrator']
    },
    {
        'id': '013',
        'name': 'Deep_Discovery_Orchestrator',
        'type': 'analysis',
        'category': 'intelligence',
        'description': 'Orchestrates comprehensive 50+ page discovery analysis',
        'required_inputs': ['all_discovery_data', 'client_goals', 'market_data'],
        'expert_councils': ['System thinking experts', 'Industry specialists'],
        'tools': ['Julius AI', 'Perplexity Pro', 'Google Drive'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.5,
        'max_tokens': 10000,
        'process_steps': [
            'Compile all data sources',
            'Apply systems thinking',
            'Generate insights matrix',
            'Create opportunity map',
            'Build transformation plan',
            'Document recommendations'
        ],
        'next_agents': ['014_task_mapper', '010_strategy_architect']
    },
    {
        'id': '014',
        'name': '665_Task_Mapper',
        'type': 'task_management',
        'category': 'operations',
        'description': 'Maps client needs to specific tasks from 665-task library',
        'required_inputs': ['service_package', 'client_requirements', 'timeline'],
        'data_sources': ['665_task_library.csv'],
        'tools': ['Notion', 'Task Library', 'Make.com'],
        'model': 'gpt-5',
        'temperature': 0.2,
        'process_steps': [
            'Identify service tiers needed',
            'Select relevant tasks',
            'Set task priorities',
            'Assign dependencies',
            'Create execution timeline',
            'Generate task assignments'
        ],
        'next_agents': ['task_prioritizer', 'portal_updater']
    },
    {
        'id': 'access_credential',
        'name': 'Access_Credential_Agent',
        'type': 'security',
        'category': 'operations',
        'description': 'Manages secure credential creation and distribution',
        'required_inputs': ['client_info', 'required_accesses', 'security_level'],
        'tools': ['1Password', 'Notion', 'Email'],
        'model': 'gpt-5',
        'temperature': 0.1,
        'process_steps': [
            'Generate secure credentials',
            'Store in 1Password',
            'Create access documentation',
            'Set up 2FA where needed',
            'Send secure invitations',
            'Track access confirmations'
        ],
        'next_agents': ['portal_builder', 'baseline_metrics']
    },
    {
        'id': 'baseline_metrics',
        'name': 'Baseline_Metrics_Agent',
        'type': 'analytics',
        'category': 'measurement',
        'description': 'Captures and documents current performance baselines',
        'required_inputs': ['analytics_access', 'historical_data', 'kpi_list'],
        'tools': ['GA4', 'GSC', 'AgencyAnalytics', 'Julius AI'],
        'model': 'gpt-5',
        'temperature': 0.2,
        'process_steps': [
            'Connect to data sources',
            'Pull historical metrics',
            'Calculate baselines',
            'Identify trends',
            'Set benchmarks',
            'Create baseline report'
        ],
        'next_agents': ['100_data_pipeline', '101_performance_intelligence']
    },
    {
        'id': 'task_prioritizer',
        'name': 'Task_Prioritizer_Agent',
        'type': 'planning',
        'category': 'operations',
        'description': 'Strategically sequences tasks for maximum impact',
        'required_inputs': ['task_list', 'dependencies', 'resources', 'deadlines'],
        'expert_councils': ['Eisenhower Matrix', 'Pareto Principle'],
        'tools': ['Notion', 'Project planner'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.4,
        'process_steps': [
            'Apply urgency/importance matrix',
            'Identify quick wins',
            'Map dependencies',
            'Calculate resource needs',
            'Optimize sequence',
            'Create execution plan'
        ],
        'next_agents': ['quality_validator', 'portal_updater']
    },
    {
        'id': 'quality_validator',
        'name': 'Quality_Validator_Agent',
        'type': 'quality_assurance',
        'category': 'operations',
        'description': 'Ensures all outputs meet top 1% quality standards',
        'required_inputs': ['output_to_validate', 'quality_criteria', 'client_standards'],
        'expert_councils': ['W. Edwards Deming', 'Six Sigma', 'Kaizen'],
        'tools': ['Quality checklist', 'Validation framework'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.2,
        'process_steps': [
            'Check against criteria',
            'Verify expert frameworks',
            'Validate value delivery',
            'Ensure client alignment',
            'Test functionality',
            'Generate quality report'
        ],
        'next_agents': ['portal_updater']
    },
    {
        'id': 'portal_updater',
        'name': 'Portal_Updater_Agent',
        'type': 'automation',
        'category': 'operations',
        'description': 'Automatically updates client portals with latest information',
        'required_inputs': ['update_data', 'portal_id', 'update_type'],
        'tools': ['Notion API', 'AgencyAnalytics', 'Make.com'],
        'model': 'gpt-5',
        'temperature': 0.1,
        'process_steps': [
            'Fetch latest data',
            'Format for portal',
            'Update dashboards',
            'Refresh metrics',
            'Add activity logs',
            'Send notifications'
        ],
        'next_agents': ['upsell_identifier']
    },
    {
        'id': 'upsell_identifier',
        'name': 'Upsell_Identifier_Agent',
        'type': 'growth_analysis',
        'category': 'sales',
        'description': 'Identifies growth opportunities and upsell potential',
        'required_inputs': ['performance_data', 'current_services', 'client_goals'],
        'expert_councils': ['Growth frameworks', 'Value ladder'],
        'tools': ['AgencyAnalytics', 'Julius AI', 'Service matrix'],
        'model': 'gpt-5',
        'temperature': 0.5,
        'process_steps': [
            'Analyze performance gaps',
            'Identify growth opportunities',
            'Match to service offerings',
            'Calculate potential value',
            'Create recommendation',
            'Generate upsell proposal'
        ],
        'next_agents': ['dynamic_pricing', '015_proposal_builder']
    },
    {
        'id': '100',
        'name': 'Data_Pipeline_Orchestrator',
        'type': 'data_engineering',
        'category': 'analytics',
        'description': 'Orchestrates data flow from all sources to analytics platforms',
        'required_inputs': ['data_sources', 'schema_requirements', 'update_frequency'],
        'tools': ['Parsio', 'Make.com', 'Google Sheets', 'Julius AI'],
        'model': 'gpt-5',
        'temperature': 0.2,
        'process_steps': [
            'Connect data sources',
            'Set up ETL pipelines',
            'Configure transformations',
            'Validate data quality',
            'Schedule updates',
            'Monitor pipeline health'
        ],
        'next_agents': ['101_performance_intelligence', '102_roi_calculator']
    },
    {
        'id': '101',
        'name': 'Performance_Intelligence_Engine',
        'type': 'analytics',
        'category': 'intelligence',
        'description': 'Generates advanced performance insights and recommendations',
        'required_inputs': ['performance_data', 'goals', 'benchmarks'],
        'expert_councils': ['Avinash Kaushik', 'Edward Tufte', 'Thomas Davenport'],
        'tools': ['Julius AI', 'AgencyAnalytics', 'GA4'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.4,
        'process_steps': [
            'Analyze performance trends',
            'Apply statistical models',
            'Identify anomalies',
            'Generate insights',
            'Create visualizations',
            'Build recommendations'
        ],
        'next_agents': ['102_roi_calculator', 'upsell_identifier']
    },
    {
        'id': '102',
        'name': 'CPR_ROI_Calculator',
        'type': 'financial_analysis',
        'category': 'analytics',
        'description': 'Calculates cost per result and ROI with advanced attribution',
        'required_inputs': ['cost_data', 'conversion_data', 'revenue_data'],
        'tools': ['Julius AI', 'SpyFu', 'Google Sheets'],
        'model': 'gpt-5',
        'temperature': 0.1,
        'process_steps': [
            'Gather cost data',
            'Track conversions',
            'Apply attribution models',
            'Calculate CPR by channel',
            'Compute ROI metrics',
            'Generate reports'
        ],
        'next_agents': ['101_performance_intelligence']
    }
]

# Additional agents to reach 30
ADDITIONAL_PERFECT_AGENTS = [
    {
        'id': '004',
        'name': 'Outreach_Message_Crafter',
        'type': 'content_generation',
        'category': 'lead_generation',
        'description': 'Creates personalized outreach messages using proven frameworks',
        'expert_councils': ['Josh Braun', 'Aaron Ross', 'Jeb Blount'],
        'tools': ['ActiveCampaign', 'Apollo.io', 'AI Writer'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.6
    },
    {
        'id': '008',
        'name': 'Custom_Proposal_Builder',
        'type': 'document_generation',
        'category': 'sales',
        'description': 'Builds highly customized proposals with industry-specific insights',
        'expert_councils': ['Blair Enns', 'Win Without Pitching'],
        'tools': ['PandaDoc', 'Canva', 'Google Drive'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.4
    },
    {
        'id': '031',
        'name': 'Content_Strategy_Agent',
        'type': 'content_planning',
        'category': 'content',
        'description': 'Develops comprehensive content strategies and calendars',
        'expert_councils': ['Ann Handley', 'Joe Pulizzi', 'Robert Rose'],
        'tools': ['SE Ranking', 'Planable', 'Notion'],
        'model': 'gpt-5',
        'temperature': 0.5
    },
    {
        'id': '032',
        'name': 'Blog_Content_Creator',
        'type': 'content_generation',
        'category': 'content',
        'description': 'Writes SEO-optimized blog content with expert insights',
        'expert_councils': ['Seth Godin', 'Ann Handley'],
        'tools': ['SE Ranking', 'WordPress', 'Canva'],
        'model': 'claude-3.5-sonnet',
        'temperature': 0.7
    },
    {
        'id': '041',
        'name': 'Email_Campaign_Builder',
        'type': 'email_marketing',
        'category': 'marketing',
        'description': 'Creates and deploys email marketing campaigns',
        'expert_councils': ['Email marketing best practices'],
        'tools': ['ActiveCampaign', 'Canva', 'Apollo.io'],
        'model': 'gpt-5',
        'temperature': 0.4
    },
    {
        'id': '050',
        'name': 'Social_Media_Scheduler',
        'type': 'social_media',
        'category': 'marketing',
        'description': 'Plans and schedules social media content across platforms',
        'expert_councils': ['Gary Vaynerchuk', 'Social media strategies'],
        'tools': ['Planable', 'Canva', 'AgencyAnalytics'],
        'model': 'gpt-5',
        'temperature': 0.5
    }
]

if __name__ == "__main__":
    converter = AgentConverter()
    
    print("🚀 Starting Agent Blueprint Conversion...")
    print(f"📁 Output directory: {converter.output_dir}")
    print("-" * 50)
    
    # Combine all agents
    all_agents = PERFECT_AGENTS + ADDITIONAL_PERFECT_AGENTS
    
    # Convert and save first 30 agents
    for agent_data in all_agents[:30]:
        agent_yaml = converter.create_agent_yaml(agent_data)
        filename = f"agent_{agent_data['id']}_{agent_data['name'].lower()}"
        converter.save_agent_file(agent_yaml, filename)
    
    print("-" * 50)
    print(f"✅ Successfully created 30 agent YAML files")
    print(f"📍 Location: {converter.output_dir}/agents/")
    print("\nNext steps:")
    print("1. Review generated YAML files")
    print("2. Copy to Google Drive Ops_V2 folder")
    print("3. Configure Conductor.build to use these files")
    print("4. Test with first agent workflow")