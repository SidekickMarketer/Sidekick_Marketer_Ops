# API Connections Setup Guide
## All APIs & Keys Needed for SIDEKICK-117-AGENTS

---

## Critical APIs (Must Have First)

### 1. OpenAI / Claude API
**Purpose**: Powers agent intelligence and expert frameworks
**Where to Get**: 
- OpenAI: https://platform.openai.com/api-keys
- Claude: https://console.anthropic.com/settings/keys

**Setup in Make.com**:
```json
{
  "api_key": "sk-...",
  "model": "gpt-4" or "claude-3-opus",
  "temperature": 0.3,  // Lower for consistency
  "max_tokens": 4000
}
```

**Used by Agents**:
- Discovery_Synthesizer (analysis)
- SOW_Generator (document creation)
- All content generation agents

**Monthly Cost**: ~$100-500 depending on usage

---

### 2. Google Workspace APIs
**Purpose**: Create docs, sheets, drive folders, emails
**Where to Get**: https://console.cloud.google.com

**APIs to Enable**:
- Google Drive API
- Google Docs API
- Google Sheets API
- Gmail API

**Setup Process**:
1. Create project in Google Cloud Console
2. Enable APIs listed above
3. Create OAuth 2.0 credentials
4. Download credentials JSON

**Make.com Connection**:
- Use built-in Google modules
- Authenticate with OAuth
- Grant all permissions requested

**Used by Agents**:
- ALL agents (document creation)
- Portal_Builder (folder structure)
- Reporting agents (sheets)

---

### 3. Notion API
**Purpose**: Client portals, databases, task management
**Where to Get**: https://www.notion.so/my-integrations

**Setup**:
1. Create integration at https://www.notion.so/my-integrations
2. Copy Internal Integration Token
3. Share databases with integration

**Required Permissions**:
- Read content
- Update content
- Insert content
- Create databases

**Database IDs Needed**:
```javascript
{
  "agent_registry": "database_id_here",
  "pattern_library": "database_id_here",
  "task_queue": "database_id_here",
  "client_portals": "database_id_here"
}
```

**Used by Agents**:
- Notion_Portal_Builder
- Portal_Updater
- Task management agents

---

## Analytics & Intelligence APIs

### 4. Google Analytics 4 API
**Purpose**: Pull website and marketing data
**Where to Get**: Google Cloud Console

**Setup**:
1. Enable Analytics Data API
2. Create service account
3. Add service account to GA4 property
4. Download key JSON

**Scopes Needed**:
- `analytics.readonly`

**Used by Agents**:
- Baseline_Metrics_Agent
- Performance_Intelligence_Engine
- Reporting agents

---

### 5. Facebook Marketing API
**Purpose**: Ad campaign data and management
**Where to Get**: https://developers.facebook.com

**Required**:
- Facebook App ID
- App Secret
- Access Token (long-lived)
- Ad Account ID

**Permissions**:
- `ads_read`
- `ads_management`
- `pages_read_engagement`
- `pages_manage_ads`

**Used by Agents**:
- Paid ad campaign agents
- ROI calculators
- Performance analyzers

---

### 6. Google Ads API
**Purpose**: Google Ads data and management
**Where to Get**: https://ads.google.com/aw/apicenter

**Required**:
- Developer token
- OAuth2 credentials
- Customer ID
- Manager account (optional)

**Used by Agents**:
- PPC management agents
- Keyword research agents
- ROI calculators

---

## Enrichment & Data APIs

### 7. Apollo.io API
**Purpose**: Lead enrichment and contact finding
**Where to Get**: https://app.apollo.io/settings/integrations/api

**Endpoints Needed**:
```
/v1/people/search
/v1/organizations/search
/v1/enrichment/person
/v1/enrichment/organization
```

**Rate Limits**: 100 requests/hour on basic plan

**Used by Agents**:
- Lead_Enricher (Agent 002)
- Intelligence gathering agents

---

### 8. Parsio API
**Purpose**: Document parsing and extraction
**Where to Get**: https://parsio.io/account/api

**Setup**:
- API key from account settings
- Create parsing templates
- Set up webhooks for results

**Used by Agents**:
- Document processing agents
- Invoice/receipt processors
- Form data extractors

---

## AI & Analysis APIs

### 9. Julius AI
**Purpose**: Advanced data analysis
**Where to Get**: Contact Julius AI for API access

**Capabilities**:
- Statistical analysis
- Predictive modeling
- Data visualization
- Pattern detection

**Used by Agents**:
- Performance_Intelligence_Engine
- Data analysis agents

---

### 10. Obviously AI
**Purpose**: No-code predictive analytics
**Where to Get**: https://www.obviously.ai/api

**Models to Create**:
- Churn prediction
- LTV prediction
- Conversion probability
- Budget optimization

**Used by Agents**:
- Predictive analytics agents
- Forecasting agents

---

## Marketing Tools APIs

### 11. AgencyAnalytics API
**Purpose**: Client reporting dashboards
**Where to Get**: Account settings → API

**Required**:
- API key
- Campaign IDs
- Report template IDs

**Used by Agents**:
- Client_Reporting_Orchestrator
- Dashboard update agents

---

### 12. BrightLocal API
**Purpose**: Local SEO and listings management
**Where to Get**: https://www.brightlocal.com/api

**Endpoints**:
- `/rankings` - Track local rankings
- `/citations` - Manage listings
- `/reviews` - Monitor reviews
- `/gmb` - Google My Business data

**Used by Agents**:
- Local SEO agents
- GMB management agents
- Review monitoring agents

---

## Communication APIs

### 13. Slack API
**Purpose**: Team notifications and updates
**Where to Get**: https://api.slack.com

**Bot Permissions Needed**:
- `chat:write`
- `files:write`
- `channels:read`
- `users:read`

**Webhook URL**: For simple notifications

---

### 14. Email Service API (SendGrid/Mailgun)
**Purpose**: Transactional and marketing emails
**Where to Get**: 
- SendGrid: https://sendgrid.com/solutions/email-api
- Mailgun: https://mailgun.com

**Used for**:
- Client communications
- Report delivery
- Notifications

---

## Make.com Specific Setup

### Webhook URLs to Create
```javascript
{
  "discovery_complete": "https://hook.us1.make.com/xxx-discovery",
  "contract_signed": "https://hook.us1.make.com/xxx-contract",
  "task_complete": "https://hook.us1.make.com/xxx-task",
  "report_trigger": "https://hook.us1.make.com/xxx-report",
  "pattern_detected": "https://hook.us1.make.com/xxx-pattern"
}
```

### Data Stores to Create
```javascript
{
  "agent_registry": {
    "structure": {
      "agent_id": "string",
      "executions": "number",
      "last_run": "datetime",
      "success_rate": "number"
    }
  },
  "pattern_library": {
    "structure": {
      "pattern_id": "string",
      "occurrences": "number",
      "solution": "string",
      "agent_created": "boolean"
    }
  }
}
```

---

## API Key Management

### Security Best Practices
1. **Never commit keys to Git**
2. **Use environment variables**
3. **Rotate keys quarterly**
4. **Use separate keys for dev/prod**
5. **Monitor usage for anomalies**

### In Make.com
- Store in Data Stores (encrypted)
- Use Connections (OAuth when possible)
- Set up team access controls

### Environment Variables Structure
```bash
# .env file (never commit this!)
OPENAI_API_KEY=sk-...
NOTION_TOKEN=secret_...
GOOGLE_SERVICE_ACCOUNT=/path/to/key.json
APOLLO_API_KEY=...
FB_ACCESS_TOKEN=...
SLACK_WEBHOOK_URL=...
```

---

## Cost Estimation

### Monthly API Costs (Estimate)
| Service | Estimated Cost | Usage |
|---------|---------------|-------|
| OpenAI/Claude | $100-500 | Based on agent runs |
| Apollo.io | $49-99 | Lead enrichment |
| Parsio | $39-99 | Document parsing |
| Julius AI | $50-200 | Data analysis |
| AgencyAnalytics | $100+ | Client reporting |
| BrightLocal | $29-99 | Local SEO |
| SendGrid | $15-50 | Email sending |
| **Total** | **$400-1,200/month** | For full system |

---

## Priority Order for Setup

### Phase 1 (Week 1) - Core APIs
1. ✅ Google Workspace (free)
2. ✅ OpenAI or Claude ($)
3. ✅ Notion (free tier ok)
4. ✅ Make.com webhooks

### Phase 2 (Week 2) - Analytics
5. ✅ Google Analytics 4
6. ✅ Facebook Marketing API
7. ✅ Google Ads API

### Phase 3 (Week 3) - Enhancement
8. ✅ Apollo.io (if doing outreach)
9. ✅ Parsio (if processing documents)
10. ✅ AgencyAnalytics (for client reporting)

### Phase 4 (As Needed)
- Julius AI (advanced analysis)
- Obviously AI (predictions)
- BrightLocal (local clients)
- Others based on client needs

---

## Testing Your APIs

### Quick Test Script (Python)
```python
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Test OpenAI
def test_openai():
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json={
            "model": "gpt-4",
            "messages": [{"role": "user", "content": "Hello"}],
            "max_tokens": 10
        }
    )
    return response.status_code == 200

# Test each API
apis_working = {
    "OpenAI": test_openai(),
    # Add other tests
}

print("API Status:", apis_working)
```

---

## Common Issues & Solutions

### "API Key Invalid"
- Check for extra spaces
- Verify key not expired
- Ensure correct environment

### "Rate Limit Exceeded"
- Implement exponential backoff
- Use batch operations
- Upgrade plan if needed

### "Permission Denied"
- Check OAuth scopes
- Verify service account permissions
- Re-authenticate connection

### "Webhook Not Triggering"
- Verify URL is correct
- Check scenario is ON
- Test with manual trigger

---

## Remember

**Start with the essentials:**
1. Google Workspace
2. OpenAI/Claude
3. Notion
4. Basic webhooks

**You can run 80% of agents with just these!**

Add other APIs as you need specific functionality. Don't overcomplicate the initial setup.