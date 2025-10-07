
# IT Ops Control Center — Systems • Security • Automation
A daily mission-control for IT: device/user automation, infra health, and SOC 2 control status — with a FastAPI web UI, a Prometheus exporter, and Grafana dashboards.

## Quick start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python monitoring/prometheus_exporter.py --port 9108
uvicorn web-dashboard.main:app --reload --port 8000
```
Open http://localhost:8000 — metrics: http://localhost:9108/metrics
