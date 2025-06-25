import requests

for svc in ["service1", "service2"]:
    url = f"http://localhost:8080/{svc}/ping"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print(f"[✓] {svc} is healthy: {r.json()}")
        else:
            print(f"[!] {svc} returned status: {r.status_code}")
    except Exception as e:
        print(f"[✗] {svc} is unreachable - {e}")
