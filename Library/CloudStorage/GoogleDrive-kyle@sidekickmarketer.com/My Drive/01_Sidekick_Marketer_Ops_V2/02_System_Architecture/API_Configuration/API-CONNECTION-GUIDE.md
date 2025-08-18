# Complete API Connection Guide
## Where to Link Everything Up

---

## Step 1: Get Your API Keys (15 minutes)

### 1A. OpenAI API (For AI Processing)
**Where**: https://platform.openai.com/api-keys
```
1. Sign up/Login
2. Go to API Keys section
3. Click "Create new secret key"
4. Name: "Sidekick-Agents"
5. Copy: sk-proj-xxxxxxxxxxxxx
6. SAVE THIS - you can't see it again!
```
**Cost**: ~$20-50/month starting

### 1B. Notion API (For Database Access)
**Where**: https://www.notion.so/my-integrations
```
1. Click "New Integration"
2. Name: "Sidekick Agent System"
3. Capabilities: Check all boxes
4. Click Submit
5. Copy: secret_xxxxxxxxxxxxx
```
**Cost**: Free

### 1C. Google Workspace (For Docs/Drive)
**Where**: Set up through Make.com (easier than manual)
```
Will connect via OAuth in Make.com
No API key needed - just login
```
**Cost**: Free (you already have Google Workspace)

---

## Step 2: Set Up Make.com (20 minutes)

### 2A. Create Make.com Account
**Where**: https://www.make.com
```
1. Sign up (free account)
2. Verify email
3. Create organization: "Sidekick Marketer"
```

### 2B. Connect Your APIs in Make.com

**In Make.com → Datastore → Connections**

#### Add OpenAI Connection:
```
1. Click "Add Connection"
2. Search "OpenAI"
3. Connection name: "Sidekick AI"
4. API Key: [paste your sk-proj-xxx key]
5. Test & Save
```

#### Add Notion Connection:
```
1. Click "Add Connection"
2. Search "Notion"
3. Connection name: "Sidekick Notion"
4. Internal Integration Token: [paste secret_xxx]
5. Test & Save
```

#### Add Google Connection:
```
1. Click "Add Connection"
2. Search "Google Drive"
3. Connection name: "Sidekick Google"
4. Click "Sign in with Google"
5. Choose your Google account
6. Allow all permissions
7. Save
```

---

## Step 3: Create Your First Test Automation (10 minutes)

### Create Test Scenario in Make.com:

```
Scenario Name: "Test - Discovery Synthesis"

Flow:
[Webhook] → [Notion Search] → [OpenAI] → [Google Docs] → [Notion Update]
```

#### Module 1: Webhook
```
1. Add Webhooks module
2. Choose "Custom webhook"
3. Name: "Discovery Trigger"
4. Copy webhook URL
5. Save: https://hook.us1.make.com/xxxxx
```

#### Module 2: Notion - Search Objects
```
1. Add Notion module
2. Action: "Search Objects"
3. Connection: Select "Sidekick Notion"
4. Database ID: [paste your Client Master ID]
5. Filter: Company Name = {{1.company_name}}
```

#### Module 3: OpenAI - Create Completion
```
1. Add OpenAI module
2. Action: "Create a Completion"
3. Connection: Select "Sidekick AI"
4. Model: gpt-4 or gpt-3.5-turbo
5. Messages: 
   Role: System
   Content: "You are a Discovery Synthesis Expert..."
   
   Role: User
   Content: {{1.discovery_notes}}
```

#### Module 4: Google Docs - Create Document
```
1. Add Google Docs module
2. Action: "Create a Document"
3. Connection: Select "Sidekick Google"
4. Folder: Browse and select client folder
5. Name: "{{2.Company Name}} - Discovery Synthesis"
6. Content: {{3.choices.0.message.content}}
```

#### Module 5: Notion - Update Database Item
```
1. Add Notion module
2. Action: "Update a Database Item"
3. Database ID: [Discovery Notes database ID]
4. Item ID: {{2.id}}
5. Properties to update:
   - Synthesis Complete: ✓
   - Google Doc Link: {{4.webViewLink}}
```

---

## Step 4: Store Your API Credentials Securely

### Create a Secure Note with:
```yaml
# SIDEKICK API CREDENTIALS
# Store in password manager!

OpenAI:
  API_KEY: sk-proj-xxxxxxxxxxxxx
  Organization_ID: org-xxxxxxxxxxxxx (if applicable)

Notion:
  Integration_Token: secret_xxxxxxxxxxxxx
  
  Database_IDs:
    Client_Master: abc123def456...
    Discovery_Notes: ghi789jkl012...
    Agent_Executions: mno345pqr678...
    Pattern_Library: stu901vwx234...
    Task_Queue: yza567bcd890...
    Metrics: efg123hij456...

Make.com:
  Webhook_URLs:
    Discovery_Trigger: https://hook.us1.make.com/xxxxx
    Proposal_Trigger: https://hook.us1.make.com/yyyyy
    Onboarding_Trigger: https://hook.us1.make.com/zzzzz

Google:
  Connected_Account: kyle@sidekickmarketer.com
  Drive_Folder_ID: xxxxxxxxxxxxx
```

---

## Step 5: Test Everything

### Run Full Test:
```bash
# Using terminal/command line:
curl -X POST YOUR_WEBHOOK_URL \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "Test Company",
    "discovery_notes": "They need more leads..."
  }'

# Or use Postman/Insomnia for easier testing
```

### Check Results:
1. ✅ Webhook received data
2. ✅ Notion found/created client
3. ✅ OpenAI generated synthesis
4. ✅ Google Doc created
5. ✅ Notion updated with link

---

## Step 6: Additional APIs (As Needed)

### Optional APIs to Add Later:

#### ActiveCampaign (Email Marketing)
```
Where: Your ActiveCampaign → Settings → Developer
Get: API URL and API Key
Use for: Email automation, lead nurturing
```

#### Stripe (Payments)
```
Where: https://dashboard.stripe.com/apikeys
Get: Publishable key and Secret key
Use for: Payment processing, subscription management
```

#### Twilio (SMS)
```
Where: https://console.twilio.com
Get: Account SID and Auth Token
Use for: SMS notifications, reminders
```

#### Calendly (Scheduling)
```
Where: https://calendly.com/integrations/api_webhooks
Get: Personal Access Token
Use for: Automated scheduling
```

---

## Cost Breakdown

### Monthly Costs:
```
Essential (Start Here):
- OpenAI API: $20-50
- Make.com: $0 (free tier) → $9-29
- Notion: $0 (free) → $8/user
- Total: ~$30-50/month

With First Client ($3,500/month):
- ROI: 70x return on tool costs
```

---

## Security Best Practices

### DO:
- ✅ Store API keys in password manager
- ✅ Use environment variables in production
- ✅ Rotate keys every 90 days
- ✅ Set spending limits on OpenAI
- ✅ Use separate keys for testing

### DON'T:
- ❌ Share keys in emails/messages
- ❌ Commit keys to Git repositories
- ❌ Use same keys across projects
- ❌ Leave unlimited spending on APIs

---

## Quick Reference - Where Everything Lives

| Service | Where to Get API | What It Does |
|---------|-----------------|--------------|
| OpenAI | platform.openai.com | AI processing |
| Notion | notion.so/my-integrations | Database operations |
| Google | Via Make.com OAuth | Docs, Drive, Sheets |
| Make.com | make.com | Connects everything |

---

## Next Steps After API Setup

1. **Test the Discovery Flow** (Today)
   - Run test with sample data
   - Verify all connections work

2. **Build Second Agent** (Tomorrow)
   - Dynamic_Pricing_Agent
   - Uses same API connections

3. **Add More Scenarios** (This Week)
   - Proposal generation
   - Contract creation
   - Onboarding automation

---

## Troubleshooting

**"Invalid API Key"**
- Check for extra spaces
- Verify key hasn't expired
- Make sure using correct key type

**"Database not found"**
- Verify database is shared with integration
- Check database ID is correct
- Ensure integration has full permissions

**"Rate limit exceeded"**
- Add delays between operations
- Upgrade API plan if needed
- Implement retry logic

**"Connection failed"**
- Re-authenticate in Make.com
- Check API service status
- Verify network connectivity

---

## You're Connected! 🚀

With these APIs linked:
- Agents can read/write Notion
- AI processes your data
- Documents auto-generate
- Everything flows automatically

**Time to build your first agent automation!**