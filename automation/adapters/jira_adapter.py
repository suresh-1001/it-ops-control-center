
"""Jira adapter (stub).
Env:
  JIRA_URL=https://yourdomain.atlassian.net
  JIRA_USER=you@company.com
  JIRA_TOKEN=api_token
"""
def open_task(project, summary):
    # TODO: POST /rest/api/3/issue
    key = "IT-0001"  # replace with response key
    return {"ok": True, "project": project, "summary": summary, "key": key, "note": "stub"}
