# New Agent Quality Control Protocol
## Ensuring EVERY Agent Meets Top 1% Standards

---

## When You Identify a Missing Agent

### Step 1: Validate the Need
```yaml
questions_to_answer:
  - What specific problem does this agent solve?
  - What happens without this agent? (cost/impact)
  - Can an existing agent handle this?
  - Is this universal or client-specific?
  - What's the ROI of building this agent?

if all_answers_valid:
  proceed_to_step_2
else:
  reconsider_need
```

### Step 2: Define the Agent's Place
```yaml
placement_questions:
  - Where in the flow does it fit?
  - What agents come before it?
  - What agents come after it?
  - What data does it receive?
  - What data does it pass forward?
  
create_flow_diagram:
  [Previous Agent] → [New Agent] → [Next Agent]
```

---

## The 12-Point Creation Checklist

### Phase 1: Core Definition (Points 1-3)

#### ✅ 1. Clear Role & Purpose
```yaml
template:
  role: "[Specific Specialist Type]"
  purpose: "[What it accomplishes]"
  value_proposition: "[Time/money saved or value created]"

quality_check:
  - Is role crystal clear?
  - Could someone understand purpose in 5 seconds?
  - Is value quantified?
```

#### ✅ 2. Specific Triggers
```yaml
template:
  trigger: "[Exact condition]"
  timing: "[When it fires]"
  condition: "[Logic/formula]"
  priority: "[CRITICAL/HIGH/MEDIUM]"

quality_check:
  - No ambiguity in trigger?
  - Timing specified?
  - Priority justified?
```

#### ✅ 3. Expert Council Selection
```yaml
process:
  1. Identify problem domain
  2. Find 2-3 world-class experts in that domain
  3. Research their frameworks/philosophies
  4. Map their principles to agent logic

template:
  expert_council:
    primary_expert: "[Name] - [Key framework]"
    supporting_experts: 
      - "[Name] - [Framework]"
      - "[Name] - [Framework]"
    
quality_check:
  - Real experts (not generic "best practices")?
  - Specific frameworks referenced?
  - Principles actively applied in logic?
```

### Phase 2: Execution Design (Points 4-7)

#### ✅ 4. Detailed Execution (5+ steps)
```yaml
template:
  execution:
    1_phase_name:
      - Specific action
      - Expected outcome
      - Success criteria
    2_phase_name:
      - Specific action
      - Expected outcome
      - Success criteria
    [... minimum 5 phases]

quality_check:
  - Each step specific and actionable?
  - Success criteria measurable?
  - Expert frameworks applied?
```

#### ✅ 5. Specific Outputs
```yaml
template:
  outputs:
    - folder/filename.ext (description)
    - folder/filename.ext (description)
    [minimum 3 outputs]

quality_check:
  - File paths specified?
  - Formats defined?
  - Output useful for next agent?
```

#### ✅ 6. Tool Stack
```yaml
template:
  tools_used:
    - ToolName (specific purpose)
    - API/Service (what it does)
    [minimum 3 tools]

quality_check:
  - Tools actually available?
  - APIs documented?
  - Costs understood?
```

#### ✅ 7. Next Agent Triggers
```yaml
template:
  triggers:
    on_success: → [Agent Name]
    on_failure: → [Agent Name]
    on_condition: → [Agent Name]

quality_check:
  - All paths covered?
  - Handoffs clear?
  - Data passed specified?
```

### Phase 3: Quality & Measurement (Points 8-10)

#### ✅ 8. Success Metrics
```yaml
template:
  success_metrics:
    - Metric: Target (e.g., "Time to complete: < 5 minutes")
    - Metric: Target (e.g., "Accuracy rate: > 95%")
    - Metric: Target (e.g., "Client satisfaction: > 90%")
    [minimum 3 metrics]

quality_check:
  - Metrics measurable?
  - Targets realistic but ambitious?
  - Aligned with value prop?
```

#### ✅ 9. Data Schema
```yaml
template:
  data_structure:
    input_data:
      field_name: type
      field_name: type
    output_data:
      field_name: type
      field_name: type

quality_check:
  - All fields defined?
  - Types specified?
  - Validation rules included?
```

#### ✅ 10. Error Handling
```yaml
template:
  error_handling:
    common_error_1:
      - Detection method
      - Resolution steps
      - Fallback option
    common_error_2:
      - Detection method
      - Resolution steps
      - Fallback option

quality_check:
  - Common errors anticipated?
  - Graceful degradation?
  - User notified appropriately?
```

### Phase 4: Intelligence Layer (Points 11-12)

#### ✅ 11. Algorithms/Logic
```yaml
template:
  algorithms:
    calculation_name: |
      formula or logic
      step by step
      
quality_check:
  - Logic clearly explained?
  - Expert frameworks visible?
  - Testable and verifiable?
```

#### ✅ 12. Templates/Examples
```yaml
template:
  examples:
    scenario_1:
      input: [sample]
      output: [expected result]
    template_1: |
      Actual template text
      That agent would use

quality_check:
  - Real examples provided?
  - Templates high quality?
  - Top 1% output demonstrated?
```

---

## The Quality Validation Process

### Before Creating Agent, Ask:

#### 1. Is This Actually Top 1%?
```yaml
comparison_test:
  average_agency_output: "[What they'd produce]"
  our_agent_output: "[What we produce]"
  
  validation:
    - Is ours 10x better?
    - Would client be impressed?
    - Does it justify premium pricing?
```

#### 2. Does It Channel Real Expertise?
```yaml
expert_test:
  - Would [Expert Name] approve this approach?
  - Are we using their actual frameworks?
  - Not just name-dropping but applying principles?
```

#### 3. Is The Output Valuable?
```yaml
value_test:
  - Saves how much time?
  - Generates how much value?
  - Solves what specific problem?
  - Worth building and maintaining?
```

---

## The Top 1% Prompt Template

### For ANY New Agent:
```python
"""
You are creating [Agent Name] that channels:

[EXPERT 1 NAME] - [Their Core Philosophy]:
- [Specific framework/principle]
- [How it applies to this problem]

[EXPERT 2 NAME] - [Their Core Philosophy]:
- [Specific framework/principle]
- [How it applies to this problem]

CONTEXT:
[What this agent receives as input]
[What problem it's solving]
[What outcome it must produce]

CREATE OUTPUT THAT:
1. [Specific requirement based on expert framework]
2. [Specific requirement based on expert framework]
3. [Specific requirement based on expert framework]

The output should make the recipient think:
"[Desired reaction showing exceptional quality]"

NOT:
"[What average output produces]"

Include:
- [Specific elements that show expertise]
- [Unique insights only expert would find]
- [Value that justifies premium pricing]

Format as:
[Specific format requirements]
"""
```

---

## Red Flags: When an Agent Isn't Top 1%

### ❌ Warning Signs:
- Generic role like "Marketing Helper"
- Trigger is "when needed"
- Expert council is "best practices"
- Execution is "analyze and report"
- Output is "recommendations"
- No specific tools mentioned
- No clear next steps
- No success metrics
- No error handling
- No algorithms
- No templates

### ✅ Signs of Top 1% Quality:
- Specific role with clear value
- Precise trigger conditions
- Named experts with frameworks
- Detailed execution steps
- Specific file outputs
- Exact tools and APIs
- Clear agent handoffs
- Measurable success metrics
- Comprehensive error handling
- Documented algorithms
- Real templates and examples

---

## The Final Test

### Before Deploying ANY New Agent:

```yaml
final_validation:
  12_point_checklist: "All items complete?"
  expert_integration: "Frameworks applied?"
  output_quality: "Genuinely exceptional?"
  value_creation: "Worth the effort?"
  flow_integration: "Fits seamlessly?"
  
  if all == true:
    agent_status: "PERFECT - Ready to Deploy"
  else:
    agent_status: "NEEDS REFINEMENT"
    return_to: "Specific missing element"
```

---

## Example: How We Created Contract_Generator_Agent

1. **Identified Need**: Proposal accepted but no contract agent
2. **Placed in Flow**: After proposal, before SOW
3. **Selected Experts**: Monteiro (contracts), Enns (positioning), Cialdini (psychology)
4. **Defined 12 Points**: All completed with specific details
5. **Created Templates**: Real contract language
6. **Validated Quality**: Compared to standard contracts
7. **Result**: Top 1% agent ready to deploy

---

## Your New Agent Protocol

### Whenever you discover a missing agent:

1. **Document the gap** (what's missing, why it matters)
2. **Run through 12-point checklist** (fill in each completely)
3. **Select appropriate experts** (real names, real frameworks)
4. **Create example outputs** (show top 1% quality)
5. **Validate against standards** (is it truly exceptional?)
6. **Integrate with flow** (clear handoffs both ways)
7. **Test with real data** (does it work as designed?)

**This ensures EVERY agent maintains top 1% quality!**