
"""Slack adapter (stub).
Env:
  SLACK_BOT_TOKEN=xoxb-...
"""
import os
def invite(email, channels):
    # TODO: slack_sdk.WebClient.invite + conversations_join
    return {"ok": True, "email": email, "channels": channels, "note": "stub"}
def deactivate(email):
    return {"ok": True, "email": email, "note": "stub"}
