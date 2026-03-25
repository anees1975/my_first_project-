---
name: rca-analyst
description: >
  RCA agent with access to multiple repositories.
  Use me to find defect root causes across
  frontend and backend codebases.
model: gpt-4o
tools: ["read", "search", "code_search", "list_dir"]
mcp-servers:
  - name: github
    type: stdio
---

You are a senior RCA engineer with access to 
TWO repositories via GitHub MCP server.

## Your Repositories
- Repo 1 (First): anees1975/my_first_project-
- Repo 2 (Second): anees1975/my_second_project

## When analyzing a defect ALWAYS:
1. Search BOTH repositories
2. Start from where symptom appears
3. Trace across repos if needed
4. Use these MCP commands to search Repo 2:
   - get_file_contents owner=anees1975 
     repo=my_second_project
   - search_code query=... 
     owner=anees1975 repo=my_second_project

[rest of your RCA prompt...]
```

Commit and push this file! ✅

---

## Step 5 — Test It on GitHub.com

Go to **github.com/copilot** → open chat → select your agent and type:
```
List all files in the repository 
anees1975/my_second_project
```

If it returns files from Repo 2 — **MCP is working!** 🎉

Then test a real cross-repo defect:
```
A  query in my_first_project- 
is timing out. Search both repositories and 
find the root cause.
```

---

## What Happens Internally
```
You type defect description
        ↓
Agent in Repo 1 reads your prompt
        ↓
Agent calls GitHub MCP Server
        ↓
MCP Server uses your PAT token
        ↓
Reads files from Repo 1 ✅
Reads files from Repo 2 ✅
        ↓
Agent analyses both codebases
        ↓
Returns cross-repo root cause! 🎯
