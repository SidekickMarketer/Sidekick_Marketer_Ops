# Quick API Reference Card
## Keep This Open While Setting Up

---

## 🔗 Direct Links - Open These in Tabs:

1. **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. **Claude**: [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)
3. **Grok**: [console.x.ai](https://console.x.ai/)
4. **Notion**: [notion.so/my-integrations](https://www.notion.so/my-integrations)
5. **Make.com**: [make.com/en/register](https://www.make.com/en/register)

---

## 📝 What to Name Everything:

### API Keys:
- All named: "Sidekick-Agents"

### In Make.com Connections:
- OpenAI → "OpenAI-GPT4"
- Claude → "Claude-API"
- Grok → "Grok-API"
- Notion → "Notion-Sidekick"
- Google Drive → "Google-Sidekick"
- Google Docs → "Docs-Sidekick"
- Gmail → "Gmail-Sidekick"

---

## 🎯 AI Model Selection Logic:

| Task Type | Best Model | Why | Cost |
|-----------|------------|-----|------|
| Deep Analysis | Claude 3 Opus | Best reasoning | $$$ |
| Creative Content | GPT-4 | Most creative | $$$ |
| Real-time Data | Grok | Current info | $$ |
| Simple Tasks | GPT-3.5 | Fast & cheap | $ |
| Code Generation | GPT-4 | Best for code | $$$ |
| Data Synthesis | Claude | Best at patterns | $$$ |

---

## ⚡ Copy-Paste Templates:

### For HTTP Headers (Claude):
```
x-api-key: [your-claude-key]
anthropic-version: 2023-06-01
content-type: application/json
```

### For HTTP Headers (Grok):
```
Authorization: Bearer [your-grok-key]
Content-Type: application/json
```

### Test Message for Any AI:
```json
{
  "model": "[model-name]",
  "messages": [
    {
      "role": "user",
      "content": "Test connection - respond with OK"
    }
  ],
  "max_tokens": 10
}
```

---

## 🔑 What Each Key Looks Like:

- **OpenAI**: `sk-proj-` followed by ~48 characters
- **Claude**: `sk-ant-` followed by ~95 characters  
- **Grok**: `xai-` followed by ~32 characters
- **Notion**: `secret_` followed by ~45 characters

---

## ✅ Setup Order (30 minutes):

1. **Minutes 0-10**: Get all API keys
2. **Minutes 10-15**: Share Notion databases
3. **Minutes 15-25**: Connect in Make.com
4. **Minutes 25-30**: Test each connection

---

## 🚨 Don't Forget:

1. **Set spending limits**:
   - OpenAI: Settings → Billing → Usage limits
   - Claude: Settings → Usage → Set limit
   - Grok: Dashboard → Billing → Set cap

2. **Save credentials**:
   - Use password manager
   - Never share in chat/email
   - Create backup in secure note

3. **Test before building**:
   - Each API individually
   - Then test combined flow
   - Verify Notion updates

---

## 💡 Pro Tips:

1. **Open all API pages first** in separate tabs
2. **Use a text editor** to collect all keys before entering in Make.com
3. **Test with small requests** to avoid burning credits
4. **Set up billing alerts** at 80% of budget

---

## 📞 If Something's Not Working:

| Issue | Quick Fix |
|-------|-----------|
| "Invalid API key" | Remove any spaces, check for typos |
| "Database not found" | Ensure shared with integration |
| "Rate limited" | Wait 60 seconds, try again |
| "Connection failed" | Re-authenticate in Make.com |
| "No access" | Check all permissions granted |

---

## 🎯 Success Looks Like:

✅ All green connections in Make.com
✅ Test message returns "OK" from each AI
✅ Notion shows your databases
✅ Google Drive accessible
✅ First webhook test succeeds

**You've got this! Everything connects in one place - Make.com is your hub.**