import random
import time
import requests

# 1. ضع رابط موقعك أو مدونتك هنا
TARGET_URL = "https://timetogoedu.blogspot.com/"

# 2. عدد الزيارات في كل مرة يشتغل فيها السكريبت
VISITS_COUNT = 40

# قائمة بمتصفحات وأجهزة مختلفة للتمويه
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0"
]

def send_visit(visit_num):
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Cache-Control': 'no-cache',
    }
    try:
        response = requests.get(TARGET_URL, headers=headers, timeout=10)
        print(f"[{visit_num}/{VISITS_COUNT}] Visit successful! Status Code: {response.status_code}")
    except Exception as e:
        print(f"[{visit_num}/{VISITS_COUNT}] Failed: {e}")

if __name__ == "__main__":
    print(f"Starting traffic generation for: {TARGET_URL}")
    for i in range(1, VISITS_COUNT + 1):
        send_visit(i)
        # الانتظار بين الزيارة والأخرى لتبدو طبيعية (بين 2 إلى 5 ثوانٍ)
        time.sleep(random.randint(2, 5))
    print("Done generating visits for this session!")
