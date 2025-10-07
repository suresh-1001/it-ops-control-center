
#!/usr/bin/env python3
import argparse, json, time, hashlib
def plan(email):
    rid=hashlib.sha1(f"{email}{time.time()}".encode()).hexdigest()[:10]
    return {"meta":{"generated_at":time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),"op":"offboard","request_id":rid,"email":email},
            "actions":[{"system":"jira","op":"open_task","project":"IT","summary":f"Offboard {email}"},
                       {"system":"workspace","op":"suspend_user","email":email},
                       {"system":"slack","op":"deactivate","email":email},
                       {"system":"intune","op":"retire_device","email":email}]}
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--email", required=True); ap.add_argument("--out", default="automation_offboard_plan.json")
    a=ap.parse_args(); p=plan(a.email); open(a.out,"w").write(json.dumps(p, indent=2)); print("Wrote", a.out)
