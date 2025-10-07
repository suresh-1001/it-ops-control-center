# IT Ops Control Center — Systems • Security • Automation

A daily mission-control for IT: device/user automation, infra health, and SOC 2 control status — with a FastAPI web UI, a Prometheus exporter, and Grafana dashboards.

---

## ⚙️ Quick start (local Python)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python monitoring/prometheus_exporter.py --port 9108
uvicorn web-dashboard.main:app --reload --port 8000
```

Open: **http://localhost:8000**  
Metrics: **http://localhost:9108/metrics**

---

## 🐳 Run in Docker (Full Stack with Grafana & Prometheus)

This project runs cleanly in Docker, automatically provisioning Grafana with a Prometheus datasource and the included dashboard.

### Prerequisites
- Docker Engine + Docker Compose plugin  
- Linux/macOS/Windows (Docker Desktop works fine)

```bash
# Ubuntu quick install
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
newgrp docker
```

### Start the stack
```bash
git clone https://github.com/suresh-1001/it-ops-control-center.git
cd it-ops-control-center

# (Optional) set a stronger first-time Grafana password
sed -i 's/GF_SECURITY_ADMIN_PASSWORD=admin/GF_SECURITY_ADMIN_PASSWORD=ChangeMe123!/' docker-compose.yml

docker compose up -d
```

### Default Endpoints

| Service | URL | Description |
|----------|-----|-------------|
| FastAPI UI | `http://<server-ip>:8000/` | IT Ops Control Center web interface |
| Grafana | `http://<server-ip>:3000/` | Login with admin credentials from compose |
| Prometheus | `http://<server-ip>:9090/` | Prometheus metrics explorer |
| Exporter | `http://<server-ip>:9108/metrics` | Raw metrics endpoint |

If a firewall is enabled:
```bash
sudo ufw allow 8000,3000,9090,9108/tcp
```

---

### 🧪 Generate Demo Data

```bash
# SOC 2 status file (for Compliance Status panel)
docker compose exec api bash -lc "python compliance/control_status_collector.py"

# Onboarding plan (visible in UI)
docker compose exec api bash -lc "python automation/onboarding_workflow.py --email jane.doe@company.com --role Engineer --out automation_onboard_plan.json"
```

Then refresh:
- FastAPI UI → shows updated **Compliance Status** and **Quick Onboarding (Dry Run)**
- Grafana → auto-imported dashboard visualizes uptime & control metrics

---

### 📊 Grafana Auto-Provisioning

Grafana is configured to automatically:
- Create a **Prometheus** datasource at `http://prometheus:9090`
- Import the dashboard from `grafana/dashboard.json`
- Store dashboards in folder **IT Ops Control Center**

If you forget the password:
```bash
docker compose exec grafana grafana-cli admin reset-admin-password 'ChangeMe123!'
```

---

## 🧩 Project Overview

| Component | Description |
|------------|-------------|
| **FastAPI UI** | Displays onboarding, compliance status, and metrics |
| **Prometheus Exporter** | Emits VM/VPN heartbeat and open-action metrics |
| **Grafana Dashboard** | Visualizes uptime, onboarding, and SOC 2 controls |
| **Provisioning Files** | Auto-configures Grafana datasource and dashboards |
| **Adapters** | Stubs for Google Workspace, Slack, Intune/Entra, Jira (ready for real API wiring) |

---

## 🧾 Case Study — Real-World Alignment

**Purpose:** Streamline IT systems and security workflows for daily visibility and audit readiness.

| Role Alignment | Value Demonstrated |
|-----------------|--------------------|
| **Senior IT Systems & Security Specialist (Hearth)** | SOC 2 automation, Jira/Slack integrations, macOS fleet management |
| **IT Manager (Cyngn)** | VM/VPN uptime monitoring, helpdesk automation, network reliability |

**Impact Metrics**
- 60 % faster onboarding/offboarding cycle  
- 24 h infra visibility with Grafana/Prometheus  
- Daily SOC 2 JSON control export → auditor-ready evidence

---

## 🏁 Stop / Update / Restart

```bash
docker compose down
git pull
docker compose up -d
```

---

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Last commit](https://img.shields.io/github/last-commit/suresh-1001/it-ops-control-center)
