# Make.com Google Drive Automation Setup Instructions

## Quick Setup (15 minutes)

### Step 1: Import the Scenario
1. Log into Make.com
2. Go to Scenarios → Create New Scenario
3. Click the three dots menu → Import Blueprint
4. Upload `make-google-drive-automation.json`

### Step 2: Configure Google Drive Connection
1. In the scenario, click on the first Google Drive module
2. Click "Add" next to Connection
3. Name it: "Sidekick Google Drive"
4. Follow OAuth flow to authorize
5. Select your Google account
6. Grant all permissions requested

### Step 3: Set Up the Webhook Trigger
1. Click on the Webhook module (first module)
2. Click "Add" next to Webhook
3. Name it: "Ops Folder Builder"
4. Copy the webhook URL that appears
5. Save this URL - you'll trigger the automation with it

### Step 4: Configure Notion (Optional but Recommended)
1. Find the Notion module (#7)
2. Add your Notion connection
3. Select your workspace
4. The databases will be created automatically

### Step 5: Test the Initial Setup
1. Turn ON the scenario (toggle switch)
2. Open a new browser tab
3. Send a test webhook:

```bash
curl -X POST YOUR_WEBHOOK_URL \
  -H "Content-Type: application/json" \
  -d '{"action": "initial_setup"}'
```

Or use Postman/Insomnia:
- Method: POST
- URL: [Your webhook URL]
- Body (JSON):
```json
{
  "action": "initial_setup"
}
```

### Step 6: Verify Creation
1. Check your Google Drive - you should see:
   - `01_Sidekick_Marketer_Ops_V2` folder
   - All 8 main subfolders
   - Framework documents
   - Tracking spreadsheets

---

## Adding Your Content

### Upload Your Frameworks
After the folder structure is created:

1. Navigate to `00_Master_Control` folder
2. Upload these files from your Desktop:
   - `expert-council-framework-final.md`
   - `complete-agency-orchestration.md`
   - `agent-intelligence-layer-blueprint.md`

3. Upload your task library:
   - Go to `02_Task_Library/665_Tasks_Master`
   - Upload your CSV file: `SM-Task-Library-DB-Version 1_CODE 3.csv`

---

## Webhook Triggers for Future Automation

### Create New Client Folder
```json
{
  "action": "new_client",
  "client_name": "Bob's Plumbing"
}
```

### Create New Agent Workspace
```json
{
  "action": "new_agent",
  "agent_type": "ServiceTitan_Connector"
}
```

### Create Weekly Report Structure
```json
{
  "action": "weekly_report",
  "week": "2025-W03",
  "clients": ["Client1", "Client2"]
}
```

---

## Advanced Automations to Add Later

### 1. Daily Organization (Add Schedule Trigger)
- Runs every night at midnight
- Organizes files uploaded during the day
- Archives old reports
- Cleans up duplicates

### 2. Client Onboarding (Connect to CRM)
- Triggers when deal closes in CRM
- Creates complete client structure
- Initializes tracking documents
- Sends welcome packet

### 3. Agent Deployment (Connect to Intelligence Layer)
- Triggers when new agent is created
- Sets up agent workspace
- Initializes execution logs
- Links to Notion registry

---

## Make.com Modules You'll Need

### Required (Free/Basic Plan):
- Webhooks
- Google Drive
- Google Docs
- Google Sheets
- Router
- Basic Tools

### Recommended (Might Need Upgrade):
- Notion
- Slack
- HTTP (for API calls)
- Data Store
- Text Parser

---

## Troubleshooting

### If folders aren't creating:
1. Check Google Drive connection permissions
2. Ensure you granted "See, edit, create, and delete all of your Google Drive files"
3. Re-authorize if needed

### If Notion fails:
1. It's optional - you can disable module #7
2. Or create databases manually and link later

### If webhook doesn't trigger:
1. Make sure scenario is ON
2. Check webhook URL is correct
3. Look at scenario execution history for errors

---

## Cost Optimization

This automation uses approximately:
- Initial setup: ~50 operations
- Per new client: ~20 operations
- Per new agent: ~10 operations

With Make.com free plan (1,000 ops/month):
- Initial setup: 5% of monthly quota
- Can onboard 40+ clients/month
- Can create 80+ agents/month

---

## Next Steps After Setup

1. **Test Client Creation**: Create a test client folder
2. **Test Agent Creation**: Create a test agent workspace
3. **Connect to Other Tools**: 
   - Link Parsio for document processing
   - Connect Julius AI for analysis
   - Set up AgencyAnalytics dashboards

4. **Schedule Recurring Tasks**:
   - Daily: File organization
   - Weekly: Report generation
   - Monthly: Archive old data

---

## Your Automation Is Now:
✅ Reusable for every client
✅ Triggered from anywhere
✅ Self-organizing
✅ Scalable to 100+ clients
✅ Connected to your entire stack

**This ONE automation replaces hours of manual folder creation forever!**