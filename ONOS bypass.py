import requests

methods = ["GET", "POST", "HEAD", "OPTIONS"]
target_url = "http://target.com"

for method in methods:
    requests.request(method, target_url)
