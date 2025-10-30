import requests
import time

URL = "https://example.com"   # Replace with any site you want to check

def check_app():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print(f"{URL} is UP ✅")
        else:
            print(f"{URL} is DOWN ❌ (Status code: {response.status_code})")
    except requests.exceptions.RequestException:
        print(f"{URL} is DOWN ❌ (No response)")

while True:
    check_app()
    time.sleep(30)
