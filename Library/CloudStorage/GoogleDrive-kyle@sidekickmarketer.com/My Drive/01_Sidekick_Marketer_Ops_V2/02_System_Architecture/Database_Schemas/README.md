# Notion Database Setup Instructions

## Quick Setup Guide

These JSON schemas define the exact structure for your 6 Notion databases. Here's how to use them:

### Option 1: Manual Setup with Reference (Recommended)
Use these JSON files as a reference while manually creating each database in Notion. This ensures you understand each property and can customize as needed.

### Option 2: Using Notion API (Advanced)
If you're comfortable with the Notion API, you can use these schemas to programmatically create the databases.

---

## Manual Setup Steps

### 1. Create Your Workspace Structure
In Notion, create this page hierarchy:
```
📊 Sidekick Operations Hub
├── 📂 Core Databases
│   └── (Your 6 databases will go here)
└── 🌐 Client Portals
    └── (Future client portals)
```

### 2. Create Each Database

For each JSON file:

1. **Create New Database**
   - Click "+ New Page" in the Core Databases folder
   - Select "Table" view
   - Name it using the `database_name` from the JSON

2. **Add Properties**
   - Click "+" next to properties
   - For each property in the JSON:
     - Add property with exact name
     - Select the correct type
     - For Select/Multi-select: Add all options listed
     - For Relations: Note the database to link to

3. **Create Views**
   - Click "Add a view" 
   - Create each view type specified
   - Apply filters and sorts as defined

---

## Database Connection Order

**IMPORTANT**: Create and set up databases in this order to properly establish relations:

1. **Client Master** - Create first (it's the hub)
2. **Discovery Notes** - Link to Client Master
3. **Agent Executions** - Link to Client Master
4. **Pattern Library** - Link to Client Master
5. **Task Queue** - Link to Client Master
6. **Quick Metrics** - Standalone (no relations)

---

## Property Type Mapping

When creating properties manually in Notion:

| JSON Type | Notion Property Type |
|-----------|---------------------|
| title | Title |
| rich_text | Text |
| number | Number |
| select | Select |
| multi_select | Multi-select |
| date | Date |
| checkbox | Checkbox |
| url | URL |
| email | Email |
| phone_number | Phone |
| people | Person |
| relation | Relation |
| created_time | Created time |
| last_edited_time | Last edited time |
| formula | Formula |
| files | Files & media |

---

## Setting Up Relations

When you see a `relation` type in the JSON:

1. The `database_id` value shows which database to link to
2. Replace `CLIENT_MASTER_ID` with your actual Client Master database
3. The `synced_property_name` creates a two-way relation

Example:
```json
"Client": {
  "type": "relation",
  "relation": {
    "database_id": "CLIENT_MASTER_ID",
    "synced_property_name": "Discovery Notes"
  }
}
```

This creates:
- "Client" property in Discovery Notes → links to Client Master
- "Discovery Notes" property in Client Master → shows all related notes

---

## Color Coding Guide

The schemas use consistent color coding:
- 🔴 Red = Urgent/Critical/Problems
- 🟠 Orange = Warning/Medium Priority
- 🟡 Yellow = Caution/Review Needed
- 🟢 Green = Good/Complete/Success
- 🔵 Blue = Information/Process
- 🟣 Purple = Special/Premium
- Gray = Default/Inactive

---

## Initial Data

The **metrics-dashboard-schema.json** includes `initial_metrics` - these are starter metrics you should create as individual entries in your Metrics database.

---

## API Setup (After Manual Creation)

Once databases are created:

1. **Create Integration**
   - Go to: https://www.notion.so/my-integrations
   - New Integration → Name: "Sidekick Agent System"
   - Copy the token (starts with `secret_`)

2. **Share Databases**
   - Open each database
   - Click "..." → "Add connections"
   - Select your integration

3. **Get Database IDs**
   - Open each database
   - Copy ID from URL (between last "/" and "?v=")
   - Save for Make.com integration

---

## Verification Checklist

After setup, verify:
- [ ] All 6 databases created
- [ ] Properties match schemas
- [ ] Relations connect properly
- [ ] Views show correct filters
- [ ] Integration has access
- [ ] Database IDs saved

---

## Need Help?

If you get stuck:
1. Check the JSON schema for exact property names
2. Ensure relations are set up in order
3. Verify integration has full access
4. Test with a sample client entry

The schemas are your blueprint - follow them exactly for a perfect setup!