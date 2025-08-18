# Model Management Test Scripts
## Copy-Paste Ready Testing Commands

---

## 🧪 Test Script 1: Basic Model Router Test

### Send this to your Router Webhook:
```json
{
  "model_role": "creative",
  "system_prompt": "You are a creative marketing expert",
  "user_prompt": "Write a tagline for a landscaping company",
  "max_tokens": 100,
  "request_id": "test-001"
}
```

### Expected Response:
```json
{
  "success": true,
  "model_used": "gpt-5-turbo-2025-08",
  "response": "[Creative tagline here]",
  "tokens_used": 85,
  "cost": 0.0025,
  "request_id": "test-001"
}
```

---

## 🧪 Test Script 2: Test All 4 Models

### Creative Test:
```bash
curl -X POST https://hook.make.com/YOUR-ROUTER-URL \
  -H "Content-Type: application/json" \
  -d '{
    "model_role": "creative",
    "user_prompt": "Write a compelling opening for a proposal",
    "max_tokens": 200
  }'
```

### Analysis Test:
```bash
curl -X POST https://hook.make.com/YOUR-ROUTER-URL \
  -H "Content-Type: application/json" \
  -d '{
    "model_role": "analysis",
    "user_prompt": "Analyze this business model: SaaS with $50k MRR, 100 customers, 5% churn",
    "max_tokens": 500
  }'
```

### Realtime Test:
```bash
curl -X POST https://hook.make.com/YOUR-ROUTER-URL \
  -H "Content-Type: application/json" \
  -d '{
    "model_role": "realtime",
    "user_prompt": "What happened in tech news today?",
    "max_tokens": 300
  }'
```

### Data Test:
```bash
curl -X POST https://hook.make.com/YOUR-ROUTER-URL \
  -H "Content-Type: application/json" \
  -d '{
    "model_role": "data",
    "user_prompt": "Process this data: [1,5,3,9,2,8]. Find mean, median, mode, and patterns",
    "max_tokens": 200
  }'
```

---

## 🔄 Test Script 3: Model Switch Test

### Step 1: Check Current Model
```bash
curl -X GET https://hook.make.com/YOUR-CONFIG-URL
```

### Step 2: Switch to New Model
```bash
curl -X POST https://hook.make.com/YOUR-SWITCH-URL \
  -H "Content-Type: application/json" \
  -d '{
    "role": "creative",
    "new_model": "gpt-6-preview-test",
    "run_tests": false
  }'
```

### Step 3: Verify Switch
```bash
curl -X POST https://hook.make.com/YOUR-ROUTER-URL \
  -H "Content-Type: application/json" \
  -d '{
    "model_role": "creative",
    "user_prompt": "Test after switch",
    "max_tokens": 50
  }'
```
Should show `"model_used": "gpt-6-preview-test"`

### Step 4: Switch Back
```bash
curl -X POST https://hook.make.com/YOUR-SWITCH-URL \
  -H "Content-Type: application/json" \
  -d '{
    "role": "creative",
    "new_model": "gpt-5-turbo-2025-08",
    "run_tests": false
  }'
```

---

## 🏃 Test Script 4: Performance Comparison

### Run Same Prompt Through All Models:
```javascript
// Test prompt for comparison
const testPrompt = {
  "user_prompt": "A landscaping company wants to double revenue in 6 months. What are the top 5 strategies?",
  "max_tokens": 500,
  "track_performance": true
};

// Send to each model role
const models = ["creative", "analysis", "realtime", "data"];

models.forEach(role => {
  fetch('YOUR-ROUTER-URL', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      model_role: role,
      ...testPrompt,
      request_id: `compare-${role}`
    })
  });
});
```

---

## 🚨 Test Script 5: Error Handling Test

### Test with Invalid Model:
```bash
curl -X POST https://hook.make.com/YOUR-ROUTER-URL \
  -H "Content-Type: application/json" \
  -d '{
    "model_role": "invalid_role",
    "user_prompt": "This should fail gracefully",
    "max_tokens": 100
  }'
```

### Expected Response:
```json
{
  "success": false,
  "error": "Invalid model role. Use: creative, analysis, realtime, or data",
  "fallback_used": true,
  "model_used": "gpt-3.5-turbo"
}
```

---

## 📊 Test Script 6: A/B Model Testing

### Compare Two Models for Same Role:
```bash
# Test current model
curl -X POST https://hook.make.com/YOUR-TEST-URL \
  -H "Content-Type: application/json" \
  -d '{
    "test_type": "ab_comparison",
    "role": "analysis",
    "model_a": "claude-opus-4-1-20250805",
    "model_b": "claude-opus-4-2-preview",
    "test_prompts": [
      "Analyze this P&L statement...",
      "Find hidden opportunities in...",
      "What patterns do you see in..."
    ],
    "iterations": 3
  }'
```

### Returns:
```json
{
  "winner": "claude-opus-4-2-preview",
  "model_a_score": 7.5,
  "model_b_score": 9.2,
  "speed_difference": "+0.3s",
  "cost_difference": "+$0.02",
  "quality_improvement": "22%",
  "recommendation": "UPGRADE"
}
```

---

## 🔥 Test Script 7: Stress Test

### Send 10 Rapid Requests:
```javascript
// Stress test script
for(let i = 0; i < 10; i++) {
  setTimeout(() => {
    fetch('YOUR-ROUTER-URL', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        model_role: 'creative',
        user_prompt: `Test request ${i}`,
        max_tokens: 50,
        request_id: `stress-${i}`
      })
    }).then(r => r.json())
      .then(data => console.log(`Request ${i}:`, data.success));
  }, i * 100); // 100ms apart
}
```

---

## 📈 Test Script 8: Cost Tracking Test

### Run Known-Cost Operation:
```bash
curl -X POST https://hook.make.com/YOUR-ROUTER-URL \
  -H "Content-Type: application/json" \
  -d '{
    "model_role": "analysis",
    "user_prompt": "Count to 10",
    "max_tokens": 50,
    "track_cost": true,
    "request_id": "cost-test-001"
  }'
```

### Check Cost Logged:
```bash
curl -X GET "https://hook.make.com/YOUR-COSTS-URL?request_id=cost-test-001"
```

---

## 🎯 Test Script 9: Full Integration Test

### Simulate Complete Discovery Flow:
```javascript
const discoveryTest = async () => {
  // Step 1: Analysis
  const analysis = await fetch('YOUR-ROUTER-URL', {
    method: 'POST',
    body: JSON.stringify({
      model_role: 'analysis',
      user_prompt: 'Analyze: Local plumber, $2M revenue, 10 employees',
      max_tokens: 1000
    })
  });

  // Step 2: Creative proposal
  const proposal = await fetch('YOUR-ROUTER-URL', {
    method: 'POST',
    body: JSON.stringify({
      model_role: 'creative',
      user_prompt: 'Create proposal based on: ' + analysis.response,
      max_tokens: 1500
    })
  });

  // Step 3: Real-time competitor check
  const competitors = await fetch('YOUR-ROUTER-URL', {
    method: 'POST',
    body: JSON.stringify({
      model_role: 'realtime',
      user_prompt: 'Current plumber marketing strategies August 2025',
      max_tokens: 500
    })
  });

  console.log('Full flow completed:', {
    analysis: analysis.success,
    proposal: proposal.success,
    competitors: competitors.success
  });
};

discoveryTest();
```

---

## ✅ Test Validation Checklist

After running all tests, verify:

- [ ] All 4 model routes return responses
- [ ] Model switching takes < 1 second
- [ ] Costs are tracked accurately
- [ ] Errors handled gracefully
- [ ] Fallbacks work when needed
- [ ] Performance meets expectations
- [ ] A/B testing identifies better model
- [ ] Stress test passes without failures

---

## 🚀 Production Test (Final)

### Once system is live, test with real agent:
```bash
# Trigger actual Discovery Synthesizer with new model
curl -X POST https://hook.make.com/YOUR-DISCOVERY-URL \
  -H "Content-Type: application/json" \
  -d '{
    "client_name": "Test Corp",
    "discovery_notes": "Real discovery notes here...",
    "use_model_router": true
  }'
```

Success = Your agent uses the router and produces quality output!

---

## 💡 Pro Testing Tips

1. **Save all test URLs** in a single document
2. **Run tests after each model switch**
3. **Keep test data consistent** for comparisons
4. **Log all test results** for patterns
5. **Test during low-usage times** initially

---

**These scripts ensure your model management system works perfectly before going live!**