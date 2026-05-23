import csv
import random
from datetime import datetime, timedelta

# -----------------------------
# CONFIG
# -----------------------------
ROWS = 10_000
OUTPUT_FILE = "synthetic_logs.csv"

methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
urls = [
    "/login", "/Login", "/LOGIN", "/admin", "/api/data", "/api/data ",
    "/home", "/search?q=test", "/search?q=Test", "/weird☃path",
    "/config", "/settings", "/profile", "/logout"
]
user_agents = [
    "Mozilla/5.0", "curl/7.68.0", "python-requests/2.31",
    "Go-http-client/1.1", "", None, "Mozilla/4.0"
]
status_codes = [200, 201, 301, 302, 400, 401, 403, 404, 500, 502, "FAILED"]
response_times = list(range(10, 2000)) + ["", None, "abc"]

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def random_timestamp():
    base = datetime(2024, 1, 1, 0, 0, 0)
    delta = timedelta(seconds=random.randint(0, 86400))
    ts = base + delta

    # mix formats intentionally
    if random.random() < 0.5:
        return ts.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return ts.strftime("%Y/%m/%d %H:%M:%S")

# -----------------------------
# GENERATE CSV
# -----------------------------
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "ip", "url", "method", "status", "response_time", "user_agent"])

    for _ in range(ROWS):
        row = [
            random_timestamp(),
            random_ip(),
            random.choice(urls),
            random.choice(methods),
            random.choice(status_codes),
            random.choice(response_times),
            random.choice(user_agents),
        ]

        # introduce duplicates randomly
        if random.random() < 0.01:
            writer.writerow(row)

        writer.writerow(row)

print(f"Generated {ROWS} synthetic log rows → {OUTPUT_FILE}")
