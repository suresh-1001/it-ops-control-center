
"""Intune/Entra adapter (stub).
Env:
  AZ_TENANT_ID=...
  AZ_CLIENT_ID=...
  AZ_CLIENT_SECRET=...
"""
def assign_policy(email, policy):
    # TODO: call MS Graph to assign configuration/profile
    return {"ok": True, "email": email, "policy": policy, "note": "stub"}
def retire_device(email):
    return {"ok": True, "email": email, "note": "stub"}
