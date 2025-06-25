# 🚀 DevOps Intern Assignment – Docker + Nginx Reverse Proxy

This project sets up a **Docker Compose-based system** with:

- A **Golang service** (`service1`)
- A **Python Flask service** (`service2`)
- An **NGINX reverse proxy** that routes traffic to both

---

## 📁 Project Structure

```
.
├── docker-compose.yml
├── test_services.py
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── service_1/
│   ├── main.go
│   └── Dockerfile
├── service_2/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
└── README.md
```

---

## ✅ Features

- 🐳 All services containerized using Docker
- 🔁 NGINX reverse proxy routes:
  - `/service1` → Golang service (port `8001`)
  - `/service2` → Flask service (port `8002`)
- 📜 NGINX logs timestamped requests
- ❤️ Healthchecks for both services
- 🧪 Test script to verify service availability

---

## ⚙️ Setup Instructions

1. Clone the repo or copy the project files.

2. Run the project:
   ```bash
   docker-compose up --build
   ```

3. Access services via:
   - [http://localhost:8080/service1/ping](http://localhost:8080/service1/ping)
   - [http://localhost:8080/service2/ping](http://localhost:8080/service2/ping)

4. To verify services using the test script:
   ```bash
   python test_services.py
   ```

---

## 📌 Routing Logic (via NGINX)

Requests go through `nginx_proxy`:

| Path Prefix        | Target Container       | Port |
|--------------------|------------------------|------|
| `/service1`        | `golang_service`       | 8001 |
| `/service2`        | `python_service`       | 8002 |

Configured in `nginx/nginx.conf`.

---

## 🩺 Healthchecks

Included in `docker-compose.yml`:

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8001/ping"]
  interval: 30s
  timeout: 5s
  retries: 3
```

NGINX waits for services to be healthy before starting.

---

## 🧪 Test Script

Run this script to check both services:

```bash
python test_services.py
```

### Sample Output:

```
[✓] service1 is healthy: {'status': 'ok', 'service': '1'}
[✓] service2 is healthy: {'status': 'ok', 'service': '2'}
```

---

## 🌟 Bonus Implemented

- ✅ Clear NGINX access logs with timestamps
- ✅ Modular Dockerfile structure for each service
- ✅ Healthchecks and Python-based test script

---

## 📬 Submission

- Upload this project to GitHub or GitLab
- Submit the repo link here: https://forms.gle/6LmZR5b2HsfDJLXS6

---

> ✅ Everything is Dockerized, reverse-proxied, and tested — ready for submission!