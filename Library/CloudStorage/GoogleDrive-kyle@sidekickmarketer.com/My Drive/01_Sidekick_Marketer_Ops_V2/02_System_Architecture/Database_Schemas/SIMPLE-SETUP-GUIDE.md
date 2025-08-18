# Super Simple Notion Setup - Just Follow These Steps

## What You're Building
6 databases that will run your entire agency operations. Takes 30 minutes total.

---

## Step 1: Create Client Master (10 minutes)

### Create the Database
1. In Notion, create new page
2. Choose "Table" 
3. Name it: 🏢 Client Master

### Add These Properties (click + for each):

**Basic Info:**
- Contact Name (Text)
- Email (Email)
- Phone (Phone)
- Website (URL)

**Status Tracking:**
- Stage (Select): Lead, Discovery, Proposal, Client, Churned
- Package (Select): Growth, Leader, Domination
- Monthly Investment (Number → Format as $)
- Health Score (Number, 1-10)

**Activity:**
- Last Contact (Date)
- Next Action (Text)
- VA Owner (Person)

**Links:**
- Google Drive Folder (URL)
- Portal Link (URL)

### Create 2 Quick Views:
1. **Pipeline** - Board view, grouped by Stage
2. **Needs Attention** - Table, filtered by Health Score < 7

---

## Step 2: Create Discovery Notes (5 minutes)

### Create the Database
1. New page → Table → Name: 📝 Discovery Notes

### Add Properties:
- Client (Relation → Select Client Master)
- Call Date (Date)
- Problems Identified (Multi-select): Add as you find them
- Budget Mentioned (Number → $)
- Key Insights (Text)
- Synthesis Complete (Checkbox)
- Google Doc Link (URL)

---

## Step 3: Create Agent Executions (5 minutes)

### Create the Database
1. New page → Table → Name: 🤖 Agent Executions

### Add Properties:
- Agent Name (Select): Add your agent names
- Client (Relation → Client Master)
- Status (Select): Success, Failed, Pending
- Execution Time (Number) 
- Output Location (URL)
- Insights Generated (Text)

### Create View:
- **Today's Runs** - Filter by Created Time = Today

---

## Step 4: Create Pattern Library (3 minutes)

### Create the Database
1. New page → Table → Name: 🔍 Pattern Library

### Add Properties:
- Pattern Type (Select): Problem, Opportunity, Process
- Times Encountered (Number)
- Solution Applied (Text)
- Reusable (Checkbox)

---

## Step 5: Create Task Queue (5 minutes)

### Create the Database
1. New page → Table → Name: 📋 Task Queue

### Add Properties:
- Client (Relation → Client Master)
- Assigned To (Person)
- Due Date (Date)
- Priority (Select): High, Medium, Low
- Status (Select): To Do, In Progress, Done

### Create Views:
1. **My Tasks** - Filter: Assigned to Me
2. **Today** - Filter: Due Date is Today

---

## Step 6: Create Metrics Dashboard (2 minutes)

### Create the Database
1. New page → Gallery view → Name: 📊 Quick Metrics

### Add Properties:
- Current Value (Number)
- Target (Number)
- Period (Select): Daily, Weekly, Monthly

### Add These Metrics (as entries):
1. Active Clients (Target: 20)
2. Monthly Revenue (Target: $100K)
3. Pipeline Value (Target: $250K)
4. Avg Health Score (Target: 8)
5. Tasks This Week (Target: 50)

---

## Step 7: Connect to API (5 minutes)

### Create Integration:
1. Go to: https://www.notion.so/my-integrations
2. New Integration → Name: "Sidekick Agents"
3. Copy the token (starts with secret_)

### Share with Databases:
For each database:
1. Open it
2. Click ••• → Add connections
3. Select "Sidekick Agents"

### Get Database IDs:
1. Open each database
2. Copy the ID from URL (the long string)
3. Save in a note:
```
Client Master: [ID]
Discovery: [ID]
Agents: [ID]
Patterns: [ID]
Tasks: [ID]
Metrics: [ID]
```

---

## You're Done! 🎉

### Test It:
1. Add a test client to Client Master
2. Create a discovery note for that client
3. Check the relation works
4. You're ready for automations!

### What You Now Have:
- ✅ Complete operational brain
- ✅ API-ready for agents
- ✅ VA-friendly interface
- ✅ Google Drive stays unchanged
- ✅ Everything searchable

### Next Step:
Connect Make.com using your API token and database IDs!

---

## Troubleshooting

**Relations not working?**
- Make sure Client Master was created first
- Check that relation property links to Client Master

**Can't find database ID?**
- It's in the URL after "notion.so/" and before "?v="
- About 32 characters long

**Integration not connecting?**
- Make sure you clicked "Share" on each database
- Check token hasn't expired

---

**Total Time: 30 minutes**
**Difficulty: Easy**
**Result: Professional agency operations system**