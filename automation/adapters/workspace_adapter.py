
"""Google Workspace adapter (stub).
Set env vars:
  GWSA_JSON=/path/to/service_account.json
  GWSA_DELEGATE=admin@company.com
Replace `raise NotImplementedError` with real Google Admin SDK calls.
"""
import os, json
def create_user(email, groups):
    # TODO: use googleapiclient to insert user and add to groups
    return {"ok": True, "email": email, "groups": groups, "note": "stub"}
def suspend_user(email):
    return {"ok": True, "email": email, "note": "stub"}
