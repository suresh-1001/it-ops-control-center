
#!/usr/bin/env python3
import argparse, json, time, hashlib
ROLE={"Engineer":{"groups":["engineering@company.com"],"channels":["#eng","#announcements"],"policy":"macOS_Engineer"}}
def plan(email, role="Engineer"):
    t=ROLE.get(role, ROLE["Engineer"]); rid=hashlib.sha1(f"{email}{time.time()}".encode()).hexdigest()[:10]
    return {"meta":{"generated_at":time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),"op":"onboard","request_id":rid,"email":email,"role":role},
            "actions":[{"system":"workspace","op":"create_user","email":email,"groups":t["groups"]},
                       {"system":"slack","op":"invite","email":email,"channels":t["channels"]},
                       {"system":"intune","op":"assign_policy","email":email,"policy":t["policy"]},
                       {"system":"jira","op":"open_task","project":"IT","summary":f"Onboard {email}"}]}
if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--email", required=True); ap.add_argument("--role", default="Engineer"); ap.add_argument("--out", default="automation_onboard_plan.json")
    a=ap.parse_args(); p=plan(a.email,a.role); open(a.out,"w").write(json.dumps(p, indent=2)); print("Wrote", a.out)
