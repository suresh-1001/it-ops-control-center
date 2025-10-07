
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from jinja2 import Environment, FileSystemLoader, select_autoescape
import subprocess, json, pathlib, datetime, os
app=FastAPI(title="IT Ops Control Center")
T=Environment(loader=FileSystemLoader(str(pathlib.Path(__file__).parent / "templates")), autoescape=select_autoescape())
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    comp=_read_compliance()
    return T.get_template("dashboard.html").render(request=request, compliance=comp, now=datetime.datetime.utcnow().isoformat()+"Z")
@app.get("/api/compliance")
def comp(): return JSONResponse(_read_compliance())
@app.post("/api/onboard")
def onboard(email: str, role: str="Engineer"):
    subprocess.run(["python","automation/onboarding_workflow.py","--email",email,"--role",role,"--out","automation_onboard_plan.json"], check=False)
    return JSONResponse({"ok":True,"plan":_read_json("automation_onboard_plan.json")})
def _read_compliance():
    if not os.path.exists("compliance_status.json"):
        subprocess.run(["python","compliance/control_status_collector.py"], check=False)
    return _read_json("compliance_status.json")
def _read_json(fp):
    try: return json.load(open(fp))
    except Exception: return {}
