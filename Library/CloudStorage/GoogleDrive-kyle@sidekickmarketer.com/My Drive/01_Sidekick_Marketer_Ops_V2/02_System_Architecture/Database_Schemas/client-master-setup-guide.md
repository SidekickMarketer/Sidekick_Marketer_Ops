# Client Master Database - Exact Setup Guide

## Create New Database
1. Click "+ New Page" 
2. Select "Table"
3. Name: "🏢 Client Master"

## Properties to Add (In Order)

### 1. Company Name
- **Type**: Title (default, already exists)
- **Keep as is**

### 2. Contact Name
- **Click**: + Add a property
- **Type**: Text
- **Name**: Contact Name

### 3. Email
- **Click**: + Add a property
- **Type**: Email
- **Name**: Email

### 4. Phone
- **Click**: + Add a property
- **Type**: Phone
- **Name**: Phone

### 5. Website
- **Click**: + Add a property
- **Type**: URL
- **Name**: Website

### 6. Stage
- **Click**: + Add a property
- **Type**: Select
- **Name**: Stage
- **Options to add**:
  - Lead (gray)
  - Discovery (blue)
  - Proposal (yellow)
  - Negotiation (orange)
  - Client (green)
  - Churned (red)

### 7. Package
- **Click**: + Add a property
- **Type**: Select
- **Name**: Package
- **Options**:
  - Growth (blue)
  - Leader (purple)
  - Domination (red)
  - Custom (gray)

### 8. Monthly Investment
- **Click**: + Add a property
- **Type**: Number
- **Name**: Monthly Investment
- **Number format**: $ Dollar

### 9. Health Score
- **Click**: + Add a property
- **Type**: Number
- **Name**: Health Score
- **Number format**: Number (1-10 scale)

### 10. Last Contact
- **Click**: + Add a property
- **Type**: Date
- **Name**: Last Contact

### 11. Next Action
- **Click**: + Add a property
- **Type**: Text
- **Name**: Next Action

### 12. Google Drive Folder
- **Click**: + Add a property
- **Type**: URL
- **Name**: Google Drive Folder

### 13. VA Owner
- **Click**: + Add a property
- **Type**: Person
- **Name**: VA Owner

### 14. Industry
- **Click**: + Add a property
- **Type**: Select
- **Name**: Industry
- **Options**:
  - Landscaping (green)
  - Plumbing (blue)
  - HVAC (orange)
  - Roofing (brown)
  - Electrical (yellow)
  - Construction (gray)
  - SaaS (purple)
  - eCommerce (pink)
  - Professional Services (default)

### 15. Revenue Range
- **Click**: + Add a property
- **Type**: Select
- **Name**: Revenue Range
- **Options**:
  - <$1M (gray)
  - $1-5M (blue)
  - $5-10M (purple)
  - $10M+ (green)

### 16. Employee Count
- **Click**: + Add a property
- **Type**: Number
- **Name**: Employee Count
- **Number format**: Number

### 17. Lead Source
- **Click**: + Add a property
- **Type**: Select
- **Name**: Lead Source
- **Options**:
  - Referral (green)
  - Cold Outreach (blue)
  - Inbound (purple)
  - Event (orange)
  - Partner (pink)

### 18. Contract Length
- **Click**: + Add a property
- **Type**: Number
- **Name**: Contract Length
- **Number format**: Number
- **Note**: This is in months

### 19. Start Date
- **Click**: + Add a property
- **Type**: Date
- **Name**: Start Date

### 20. Lifetime Value
- **Click**: + Add a property
- **Type**: Number
- **Name**: Lifetime Value
- **Number format**: $ Dollar

### 21. Main Competitors
- **Click**: + Add a property
- **Type**: Multi-select
- **Name**: Main Competitors
- **Note**: Add competitor names as you encounter them

### 22. Current Marketing Spend
- **Click**: + Add a property
- **Type**: Number
- **Name**: Current Marketing Spend
- **Number format**: $ Dollar

### 23. Biggest Pain Points
- **Click**: + Add a property
- **Type**: Multi-select
- **Name**: Biggest Pain Points
- **Options**:
  - Lead Generation (red)
  - Brand Awareness (blue)
  - Conversion Rate (orange)
  - Customer Retention (green)
  - Competition (purple)
  - Pricing Pressure (yellow)
  - Operational Efficiency (gray)

### 24. Goals
- **Click**: + Add a property
- **Type**: Multi-select
- **Name**: Goals
- **Options**:
  - Increase Revenue (green)
  - Market Domination (red)
  - Improve Margins (blue)
  - Scale Operations (purple)
  - Beat Competition (orange)
  - Digital Transformation (pink)

### 25. Decision Makers
- **Click**: + Add a property
- **Type**: Text
- **Name**: Decision Makers

### 26. Portal Link
- **Click**: + Add a property
- **Type**: URL
- **Name**: Portal Link

### 27. Agents Deployed
- **Click**: + Add a property
- **Type**: Multi-select
- **Name**: Agents Deployed
- **Note**: Add agent names as you deploy them

### 28. Patterns Identified
- **Click**: + Add a property
- **Type**: Text
- **Name**: Patterns Identified

## Views to Create

### View 1: Pipeline View
1. Click "Add a view"
2. Select "Board"
3. Name: "Pipeline View"
4. Group by: Stage
5. Sort: Last Contact (Newest first)

### View 2: Active Clients
1. Click "Add a view"
2. Select "Table"
3. Name: "Active Clients"
4. Add Filter: Stage is Client
5. Show all properties

### View 3: Needs Attention
1. Click "Add a view"
2. Select "Table"
3. Name: "Needs Attention"
4. Add Filter Group (OR):
   - Health Score < 7
   - OR Last Contact is before 14 days ago
5. Sort: Health Score (Low to High)

### View 4: By Owner
1. Click "Add a view"
2. Select "Table"
3. Name: "By Owner"
4. Group by: VA Owner

## Color Selection Guide
When adding Select options, click the color dot to change:
- Gray = Inactive/Unknown
- Blue = Standard/Info
- Green = Good/Success
- Yellow = Warning
- Orange = Attention
- Red = Critical/Failed
- Purple = Premium/Special
- Pink = Unique/Custom
- Brown = Physical/Manual
- Default = No color

## Final Checklist
- [ ] All 28 properties added
- [ ] All select options configured with colors
- [ ] Number formats set correctly ($ for money)
- [ ] 4 views created
- [ ] Test by adding one sample client

## Time Estimate: 15 minutes