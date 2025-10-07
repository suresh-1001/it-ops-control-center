
#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from prometheus_client import CollectorRegistry, Gauge, generate_latest, CONTENT_TYPE_LATEST
registry=CollectorRegistry()
g1=Gauge('itops_vm_up','VM/Host heartbeat',['host'],registry=registry)
g2=Gauge('itops_vpn_up','VPN peer up',['peer'],registry=registry)
g3=Gauge('itops_open_actions','Open actions',['type'],registry=registry)
def scrape():
    hosts={'hypervisor1':1,'fileserver':1,'db01':1}
    vpns={'nyc':1,'sfo':1}
    actions={'onboarding':2,'offboarding':1,'soc2':3}
    for h,v in hosts.items(): g1.labels(h).set(v)
    for p,v in vpns.items(): g2.labels(p).set(v)
    for t,v in actions.items(): g3.labels(t).set(v)
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path!="/metrics": self.send_response(404); self.end_headers(); return
        scrape(); data=generate_latest(registry)
        self.send_response(200); self.send_header("Content-Type", CONTENT_TYPE_LATEST); self.end_headers(); self.wfile.write(data)
if __name__=="__main__":
    HTTPServer(("0.0.0.0",9108),H).serve_forever()
