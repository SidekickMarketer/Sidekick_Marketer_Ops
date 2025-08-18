#!/usr/bin/env python3
"""
Pattern Detection & Self-Evolution Engine
Automatically detects patterns and creates new agents
"""

import json
import yaml
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import hashlib

class PatternType(Enum):
    """Types of patterns we can detect"""
    PERFORMANCE_GAP = "performance_gap"
    MISSING_DATA = "missing_data"
    MANUAL_PROCESS = "manual_process"
    REPETITIVE_TASK = "repetitive_task"
    ERROR_PATTERN = "error_pattern"
    OPTIMIZATION_OPPORTUNITY = "optimization_opportunity"
    NEW_DATA_SOURCE = "new_data_source"
    SCALING_NEED = "scaling_need"

@dataclass
class DetectedPattern:
    """Represents a detected pattern"""
    pattern_id: str
    pattern_type: PatternType
    description: str
    frequency: int
    impact_score: float
    confidence: float
    first_detected: datetime
    last_detected: datetime
    data_points: List[Dict]
    suggested_agent: Optional[str] = None
    auto_create: bool = False

class PatternDetectionEngine:
    """
    Detects patterns and triggers agent creation
    """
    
    def __init__(self):
        self.patterns = {}
        self.thresholds = self.load_thresholds()
        self.agent_templates = self.load_agent_templates()
        self.created_agents = []
        
    def load_thresholds(self):
        """Load pattern detection thresholds"""
        return {
            'min_frequency': 3,  # Pattern must occur 3+ times
            'min_confidence': 0.7,  # 70% confidence minimum
            'min_impact': 500,  # $500 or 5 hours impact
            'auto_create_threshold': 0.85  # 85% confidence for auto-creation
        }
    
    def load_agent_templates(self):
        """Load agent creation templates"""
        return {
            PatternType.PERFORMANCE_GAP: {
                'name_template': '{metric}_optimization_agent',
                'description': 'Optimizes {metric} performance',
                'expert_councils': ['optimization_experts'],
                'tools': ['analytics', 'testing', 'reporting']
            },
            PatternType.MISSING_DATA: {
                'name_template': '{source}_data_recovery_agent',
                'description': 'Recovers missing data from {source}',
                'expert_councils': ['data_experts'],
                'tools': ['parsio', 'api_connectors', 'validation']
            },
            PatternType.MANUAL_PROCESS: {
                'name_template': '{process}_automation_agent',
                'description': 'Automates {process} workflow',
                'expert_councils': ['automation_experts'],
                'tools': ['make_com', 'zapier', 'conductor']
            },
            PatternType.REPETITIVE_TASK: {
                'name_template': '{task}_batch_agent',
                'description': 'Batch processes {task}',
                'expert_councils': ['efficiency_experts'],
                'tools': ['batch_processor', 'scheduler']
            },
            PatternType.ERROR_PATTERN: {
                'name_template': '{error}_repair_agent',
                'description': 'Fixes {error} automatically',
                'expert_councils': ['debugging_experts'],
                'tools': ['error_handler', 'logging', 'alerting']
            },
            PatternType.NEW_DATA_SOURCE: {
                'name_template': '{platform}_connector_agent',
                'description': 'Connects to {platform} API',
                'expert_councils': ['integration_experts'],
                'tools': ['api_builder', 'data_mapper', 'validator']
            }
        }
    
    def analyze_data_stream(self, data: Dict[str, Any]):
        """Analyze incoming data for patterns"""
        patterns_found = []
        
        # Check for performance gaps
        if perf_gap := self.detect_performance_gap(data):
            patterns_found.append(perf_gap)
        
        # Check for missing data
        if missing := self.detect_missing_data(data):
            patterns_found.append(missing)
        
        # Check for manual processes
        if manual := self.detect_manual_process(data):
            patterns_found.append(manual)
        
        # Check for repetitive tasks
        if repetitive := self.detect_repetitive_task(data):
            patterns_found.append(repetitive)
        
        # Check for errors
        if errors := self.detect_error_pattern(data):
            patterns_found.append(errors)
        
        # Check for optimization opportunities
        if optimization := self.detect_optimization_opportunity(data):
            patterns_found.append(optimization)
        
        return patterns_found
    
    def detect_performance_gap(self, data: Dict) -> Optional[DetectedPattern]:
        """Detect performance below target"""
        if 'metrics' not in data:
            return None
        
        for metric_name, metric_data in data['metrics'].items():
            if 'actual' in metric_data and 'target' in metric_data:
                actual = metric_data['actual']
                target = metric_data['target']
                
                # Check if performance is significantly below target
                if actual < target * 0.8:  # 20% below target
                    pattern_id = self.generate_pattern_id(
                        PatternType.PERFORMANCE_GAP, 
                        metric_name
                    )
                    
                    # Check if we've seen this before
                    if pattern_id in self.patterns:
                        # Update existing pattern
                        pattern = self.patterns[pattern_id]
                        pattern.frequency += 1
                        pattern.last_detected = datetime.now()
                        pattern.data_points.append(metric_data)
                        pattern.confidence = min(0.95, pattern.confidence + 0.05)
                    else:
                        # Create new pattern
                        pattern = DetectedPattern(
                            pattern_id=pattern_id,
                            pattern_type=PatternType.PERFORMANCE_GAP,
                            description=f"{metric_name} is {(1 - actual/target)*100:.1f}% below target",
                            frequency=1,
                            impact_score=abs(target - actual) * 100,  # Rough impact calculation
                            confidence=0.7,
                            first_detected=datetime.now(),
                            last_detected=datetime.now(),
                            data_points=[metric_data],
                            suggested_agent=f"{metric_name}_optimization_agent"
                        )
                        self.patterns[pattern_id] = pattern
                    
                    return pattern
        
        return None
    
    def detect_missing_data(self, data: Dict) -> Optional[DetectedPattern]:
        """Detect missing data fields"""
        if 'data_quality' not in data:
            return None
        
        for field_name, quality_info in data['data_quality'].items():
            if quality_info.get('null_percentage', 0) > 30:  # >30% null
                pattern_id = self.generate_pattern_id(
                    PatternType.MISSING_DATA,
                    field_name
                )
                
                if pattern_id in self.patterns:
                    pattern = self.patterns[pattern_id]
                    pattern.frequency += 1
                    pattern.last_detected = datetime.now()
                    pattern.confidence = min(0.95, pattern.confidence + 0.05)
                else:
                    pattern = DetectedPattern(
                        pattern_id=pattern_id,
                        pattern_type=PatternType.MISSING_DATA,
                        description=f"{field_name} missing in {quality_info['null_percentage']}% of records",
                        frequency=1,
                        impact_score=quality_info.get('impact', 500),
                        confidence=0.75,
                        first_detected=datetime.now(),
                        last_detected=datetime.now(),
                        data_points=[quality_info],
                        suggested_agent=f"{field_name}_data_recovery_agent"
                    )
                    self.patterns[pattern_id] = pattern
                
                return pattern
        
        return None
    
    def detect_manual_process(self, data: Dict) -> Optional[DetectedPattern]:
        """Detect manual processes that could be automated"""
        if 'process_log' not in data:
            return None
        
        for process_name, process_info in data['process_log'].items():
            if process_info.get('is_manual', False) and process_info.get('frequency', 0) > 5:
                pattern_id = self.generate_pattern_id(
                    PatternType.MANUAL_PROCESS,
                    process_name
                )
                
                if pattern_id in self.patterns:
                    pattern = self.patterns[pattern_id]
                    pattern.frequency += 1
                    pattern.last_detected = datetime.now()
                    pattern.impact_score += process_info.get('time_spent', 0) * 100
                else:
                    pattern = DetectedPattern(
                        pattern_id=pattern_id,
                        pattern_type=PatternType.MANUAL_PROCESS,
                        description=f"Manual process '{process_name}' takes {process_info.get('time_spent', 0)} hours",
                        frequency=1,
                        impact_score=process_info.get('time_spent', 0) * 100,
                        confidence=0.8,
                        first_detected=datetime.now(),
                        last_detected=datetime.now(),
                        data_points=[process_info],
                        suggested_agent=f"{process_name}_automation_agent"
                    )
                    self.patterns[pattern_id] = pattern
                
                return pattern
        
        return None
    
    def detect_repetitive_task(self, data: Dict) -> Optional[DetectedPattern]:
        """Detect repetitive tasks"""
        if 'task_log' not in data:
            return None
        
        task_counts = {}
        for task in data['task_log']:
            task_type = task.get('type', 'unknown')
            task_counts[task_type] = task_counts.get(task_type, 0) + 1
        
        for task_type, count in task_counts.items():
            if count > 10:  # More than 10 occurrences
                pattern_id = self.generate_pattern_id(
                    PatternType.REPETITIVE_TASK,
                    task_type
                )
                
                if pattern_id not in self.patterns:
                    pattern = DetectedPattern(
                        pattern_id=pattern_id,
                        pattern_type=PatternType.REPETITIVE_TASK,
                        description=f"Task '{task_type}' repeated {count} times",
                        frequency=count,
                        impact_score=count * 10,  # Each repetition worth 10 points
                        confidence=0.85,
                        first_detected=datetime.now(),
                        last_detected=datetime.now(),
                        data_points=data['task_log'],
                        suggested_agent=f"{task_type}_batch_agent"
                    )
                    self.patterns[pattern_id] = pattern
                    return pattern
        
        return None
    
    def detect_error_pattern(self, data: Dict) -> Optional[DetectedPattern]:
        """Detect recurring errors"""
        if 'errors' not in data:
            return None
        
        error_counts = {}
        for error in data['errors']:
            error_type = error.get('type', 'unknown')
            error_counts[error_type] = error_counts.get(error_type, 0) + 1
        
        for error_type, count in error_counts.items():
            if count > 3:  # More than 3 occurrences
                pattern_id = self.generate_pattern_id(
                    PatternType.ERROR_PATTERN,
                    error_type
                )
                
                if pattern_id not in self.patterns:
                    pattern = DetectedPattern(
                        pattern_id=pattern_id,
                        pattern_type=PatternType.ERROR_PATTERN,
                        description=f"Error '{error_type}' occurred {count} times",
                        frequency=count,
                        impact_score=count * 50,  # Errors have high impact
                        confidence=0.9,
                        first_detected=datetime.now(),
                        last_detected=datetime.now(),
                        data_points=data['errors'],
                        suggested_agent=f"{error_type}_repair_agent"
                    )
                    self.patterns[pattern_id] = pattern
                    return pattern
        
        return None
    
    def detect_optimization_opportunity(self, data: Dict) -> Optional[DetectedPattern]:
        """Detect optimization opportunities"""
        if 'performance' not in data:
            return None
        
        for process_name, perf_data in data['performance'].items():
            baseline = perf_data.get('baseline', 0)
            current = perf_data.get('current', 0)
            best_practice = perf_data.get('best_practice', 0)
            
            if current > 0 and best_practice > 0:
                improvement_potential = (best_practice - current) / current
                
                if improvement_potential > 0.2:  # 20% improvement possible
                    pattern_id = self.generate_pattern_id(
                        PatternType.OPTIMIZATION_OPPORTUNITY,
                        process_name
                    )
                    
                    if pattern_id not in self.patterns:
                        pattern = DetectedPattern(
                            pattern_id=pattern_id,
                            pattern_type=PatternType.OPTIMIZATION_OPPORTUNITY,
                            description=f"{process_name} can be improved by {improvement_potential*100:.1f}%",
                            frequency=1,
                            impact_score=improvement_potential * 1000,
                            confidence=0.75,
                            first_detected=datetime.now(),
                            last_detected=datetime.now(),
                            data_points=[perf_data],
                            suggested_agent=f"{process_name}_optimization_agent"
                        )
                        self.patterns[pattern_id] = pattern
                        return pattern
        
        return None
    
    def generate_pattern_id(self, pattern_type: PatternType, identifier: str) -> str:
        """Generate unique pattern ID"""
        content = f"{pattern_type.value}_{identifier}"
        return hashlib.md5(content.encode()).hexdigest()[:12]
    
    def should_create_agent(self, pattern: DetectedPattern) -> bool:
        """Determine if we should create an agent for this pattern"""
        # Check thresholds
        if pattern.frequency < self.thresholds['min_frequency']:
            return False
        
        if pattern.confidence < self.thresholds['min_confidence']:
            return False
        
        if pattern.impact_score < self.thresholds['min_impact']:
            return False
        
        # Check if agent already exists
        if pattern.suggested_agent in self.created_agents:
            return False
        
        # Auto-create if confidence is very high
        if pattern.confidence >= self.thresholds['auto_create_threshold']:
            pattern.auto_create = True
            return True
        
        return True
    
    def create_agent_yaml(self, pattern: DetectedPattern) -> Dict:
        """Create YAML configuration for new agent"""
        template = self.agent_templates.get(pattern.pattern_type, {})
        
        # Extract context from pattern
        context = pattern.description.split("'")[1] if "'" in pattern.description else "unknown"
        
        agent_config = {
            'agent': {
                'id': pattern.suggested_agent,
                'name': pattern.suggested_agent.replace('_', ' ').title(),
                'type': 'self_evolved',
                'category': pattern.pattern_type.value,
                'status': 'pending_review' if not pattern.auto_create else 'active',
                'version': '1.0',
                'created_by': 'pattern_detection_engine',
                'created_date': datetime.now().isoformat()
            },
            'description': f"Auto-generated agent to handle: {pattern.description}",
            'pattern_metadata': {
                'pattern_id': pattern.pattern_id,
                'pattern_type': pattern.pattern_type.value,
                'frequency': pattern.frequency,
                'confidence': pattern.confidence,
                'impact_score': pattern.impact_score,
                'auto_created': pattern.auto_create
            },
            'triggers': [
                {
                    'type': 'pattern_match',
                    'pattern': pattern.pattern_type.value,
                    'threshold': pattern.confidence
                },
                {
                    'type': 'manual',
                    'source': 'conductor'
                }
            ],
            'expert_councils': template.get('expert_councils', []),
            'tools': template.get('tools', []),
            'execution': {
                'model_selection': {
                    'primary': 'gpt-5' if pattern.pattern_type in [
                        PatternType.REPETITIVE_TASK, 
                        PatternType.ERROR_PATTERN
                    ] else 'claude-3.5-sonnet',
                    'fallback': 'gpt-4',
                    'strategy': 'efficiency_optimized' if pattern.frequency > 10 else 'quality_optimized'
                },
                'temperature': 0.3,
                'max_tokens': 4000,
                'timeout': 600
            },
            'process': self.generate_process_steps(pattern),
            'outputs': {
                'format': 'structured',
                'destinations': ['notion', 'slack', 'analytics_dashboard']
            },
            'self_evolution': {
                'enabled': True,
                'learning_rate': 0.1,
                'improvement_threshold': 0.8
            },
            'metrics': {
                'track': [
                    'execution_time',
                    'success_rate',
                    'value_generated',
                    'errors_prevented'
                ],
                'report_to': 'analytics_dashboard'
            }
        }
        
        return agent_config
    
    def generate_process_steps(self, pattern: DetectedPattern) -> List[Dict]:
        """Generate process steps based on pattern type"""
        steps_map = {
            PatternType.PERFORMANCE_GAP: [
                {'step': 'Analyze current performance metrics', 'tools': ['analytics']},
                {'step': 'Identify bottlenecks and issues', 'tools': ['diagnosis']},
                {'step': 'Generate optimization recommendations', 'tools': ['ai_analysis']},
                {'step': 'Implement improvements', 'tools': ['automation']},
                {'step': 'Monitor results', 'tools': ['tracking']}
            ],
            PatternType.MISSING_DATA: [
                {'step': 'Identify data sources', 'tools': ['discovery']},
                {'step': 'Attempt data recovery', 'tools': ['api', 'scraping']},
                {'step': 'Validate recovered data', 'tools': ['validation']},
                {'step': 'Fill gaps with estimates if needed', 'tools': ['ml_models']},
                {'step': 'Update database', 'tools': ['database']}
            ],
            PatternType.MANUAL_PROCESS: [
                {'step': 'Document current process', 'tools': ['process_mapping']},
                {'step': 'Identify automation points', 'tools': ['analysis']},
                {'step': 'Build automation workflow', 'tools': ['make_com', 'zapier']},
                {'step': 'Test automation', 'tools': ['testing']},
                {'step': 'Deploy and monitor', 'tools': ['deployment', 'monitoring']}
            ],
            PatternType.REPETITIVE_TASK: [
                {'step': 'Batch similar tasks', 'tools': ['grouping']},
                {'step': 'Process in parallel', 'tools': ['parallel_processing']},
                {'step': 'Validate results', 'tools': ['validation']},
                {'step': 'Report completion', 'tools': ['reporting']}
            ],
            PatternType.ERROR_PATTERN: [
                {'step': 'Analyze error pattern', 'tools': ['error_analysis']},
                {'step': 'Identify root cause', 'tools': ['debugging']},
                {'step': 'Implement fix', 'tools': ['code_fix', 'configuration']},
                {'step': 'Test solution', 'tools': ['testing']},
                {'step': 'Deploy fix', 'tools': ['deployment']}
            ],
            PatternType.OPTIMIZATION_OPPORTUNITY: [
                {'step': 'Benchmark current state', 'tools': ['benchmarking']},
                {'step': 'Research best practices', 'tools': ['research']},
                {'step': 'Design improvements', 'tools': ['design']},
                {'step': 'Implement optimizations', 'tools': ['implementation']},
                {'step': 'Measure improvement', 'tools': ['analytics']}
            ],
            PatternType.NEW_DATA_SOURCE: [
                {'step': 'Analyze API documentation', 'tools': ['documentation']},
                {'step': 'Build connector', 'tools': ['api_builder']},
                {'step': 'Map data fields', 'tools': ['data_mapping']},
                {'step': 'Test connection', 'tools': ['testing']},
                {'step': 'Schedule sync', 'tools': ['scheduler']}
            ],
            PatternType.SCALING_NEED: [
                {'step': 'Analyze resource usage', 'tools': ['monitoring']},
                {'step': 'Identify scaling points', 'tools': ['analysis']},
                {'step': 'Implement scaling solution', 'tools': ['infrastructure']},
                {'step': 'Load test', 'tools': ['testing']},
                {'step': 'Deploy scaled solution', 'tools': ['deployment']}
            ]
        }
        
        return steps_map.get(pattern.pattern_type, [
            {'step': 'Analyze pattern', 'tools': ['analysis']},
            {'step': 'Generate solution', 'tools': ['ai']},
            {'step': 'Implement', 'tools': ['automation']},
            {'step': 'Monitor', 'tools': ['tracking']}
        ])
    
    def save_agent(self, agent_config: Dict, pattern: DetectedPattern):
        """Save agent configuration to file"""
        agent_id = agent_config['agent']['id']
        filename = f"/Users/kylenaughtrip/Desktop/conductor_agents/agents/self_evolved/{agent_id}.yml"
        
        # Save YAML file
        with open(filename, 'w') as f:
            yaml.dump(agent_config, f, default_flow_style=False)
        
        # Track created agent
        self.created_agents.append(agent_id)
        
        # Log creation
        print(f"\n🤖 NEW AGENT CREATED: {agent_id}")
        print(f"   Pattern: {pattern.pattern_type.value}")
        print(f"   Confidence: {pattern.confidence:.2%}")
        print(f"   Impact: ${pattern.impact_score:.0f}")
        print(f"   Auto-deployed: {pattern.auto_create}")
        print(f"   File: {filename}")
        
        return filename
    
    def run_detection_cycle(self, data: Dict[str, Any]):
        """Run a complete detection cycle"""
        print("\n🔍 Running Pattern Detection Cycle...")
        
        # Analyze data for patterns
        patterns = self.analyze_data_stream(data)
        
        if not patterns:
            print("   No new patterns detected")
            return []
        
        created_agents = []
        for pattern in patterns:
            if pattern and self.should_create_agent(pattern):
                # Create agent configuration
                agent_config = self.create_agent_yaml(pattern)
                
                # Save agent
                filename = self.save_agent(agent_config, pattern)
                created_agents.append({
                    'agent_id': agent_config['agent']['id'],
                    'pattern': pattern,
                    'filename': filename,
                    'auto_deployed': pattern.auto_create
                })
        
        return created_agents

# Example usage
if __name__ == "__main__":
    # Initialize engine
    engine = PatternDetectionEngine()
    
    # Sample data showing various patterns
    sample_data = {
        'metrics': {
            'lead_conversion': {
                'actual': 2.1,
                'target': 3.0
            },
            'cpr': {
                'actual': 145,
                'target': 100
            }
        },
        'data_quality': {
            'phone_number': {
                'null_percentage': 35,
                'impact': 800
            }
        },
        'process_log': {
            'report_generation': {
                'is_manual': True,
                'frequency': 30,
                'time_spent': 3
            }
        },
        'task_log': [
            {'type': 'keyword_research'} for _ in range(15)
        ],
        'errors': [
            {'type': 'api_timeout', 'timestamp': datetime.now()} for _ in range(5)
        ],
        'performance': {
            'email_open_rate': {
                'current': 18,
                'best_practice': 25
            }
        }
    }
    
    # Run detection
    created = engine.run_detection_cycle(sample_data)
    
    print(f"\n✅ Detection cycle complete")
    print(f"   Patterns detected: {len(engine.patterns)}")
    print(f"   Agents created: {len(created)}")
    
    if created:
        print("\n📋 Created Agents:")
        for agent_info in created:
            print(f"   • {agent_info['agent_id']}")
            print(f"     Pattern: {agent_info['pattern'].pattern_type.value}")
            print(f"     Auto-deployed: {agent_info['auto_deployed']}")