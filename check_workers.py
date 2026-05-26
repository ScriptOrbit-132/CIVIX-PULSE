import httpx
import os
import json
from dotenv import load_dotenv

load_dotenv(override=True)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

headers = {
    "apikey": key,
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

print(f"Querying Supabase: {url}/rest/v1/workers...")

try:
    res = httpx.get(f"{url}/rest/v1/workers?select=*", headers=headers, timeout=10.0)
    print(f"Status Code: {res.status_code}")
    if res.status_code == 200:
        workers = res.json()
        print(f"Found {len(workers)} workers:")
        for w in workers:
            print(f"- ID: {w.get('worker_login_id')}, Name: {w.get('name')}, Status: {w.get('status')}")
    else:
        print(f"Error Response: {res.text}")
except Exception as e:
    print(f"Failed to query: {e}")
