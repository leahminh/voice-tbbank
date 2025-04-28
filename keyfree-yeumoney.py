import os
import sys
import time
import hashlib
import requests
from datetime import datetime, timedelta

KEY_FILE = "Key-kich-hoat-tool-by-LAMDev.txt"
START_SCRIPT_URL = "https://raw.githubusercontent.com/leahminh/voice-tbbank/refs/heads/main/start.py"
YEUMONEY_TOKEN = "56489910cde0777fbe31a6af660956c76c7fc1e18d09e9b5f19ee9da745231fe"

def save_key(key, expiry):
    with open(KEY_FILE, "w") as f:
        f.write(f"{key}|{expiry}")
    print(f"\n\033[92m✔ Key đã lưu: {key} (hết hạn {expiry})\033[0m\n")

def load_key():
    if not os.path.exists(KEY_FILE):
        return None, None
    try:
        key, expiry = open(KEY_FILE).read().strip().split("|",1)
        return key, expiry
    except:
        return None, None

def run_start():
    code = requests.get(START_SCRIPT_URL).text
    exec(code, globals())
    sys.exit(0)

def generate_free_key():
    raw = str(time.time()) + os.urandom(16).hex()
    return "LAMDev" + hashlib.sha256(raw.encode()).hexdigest()[:10]

def shorten_with_yeumoney(long_url):
    params = {"token": YEUMONEY_TOKEN, "format": "json", "url": long_url}
    r = requests.get("https://yeumoney.com/QL_api.php", params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    if data.get("status") == "success":
        return data.get("shortenedUrl")
    return None

def free_flow():
    key    = generate_free_key()
    expiry = (datetime.now() + timedelta(days=3)).strftime("%d/%m/%Y")

    long_url = f"https://keyfree.amteam.x10.mx?key={key}"
    short    = shorten_with_yeumoney(long_url)
    if not short:
        print("\033[91m✘ Không rút gọn được link!\033[0m")
        sys.exit(1)

    print(f"\n\033[92mLink lấy key của bạn: {short}\033[0m")
    print(f"⏳ Key sẽ hết hạn: {expiry}\033[0m\n")

    while True:
        inp = input("🔑 Nhập lại key vừa nhận: ").strip()
        if inp == key:
            save_key(key, expiry)
            run_start()
        else:
            print("\033[91m✘ Key sai, thử lại!\033[0m")

def main():
    key, expiry = load_key()

    if key and expiry:
        try:
            if datetime.strptime(expiry, "%d/%m/%Y") >= datetime.now():
                print(f"\033[92m✔ Đã có key hợp lệ (hết hạn {expiry})\033[0m")
                run_start()
                return
            else:
                print(f"\033[93mKey đã hết hạn {expiry}, sẽ lấy key mới...\033[0m")
        except:
            print("\033[93mFile key lỗi hoặc định dạng sai, sẽ lấy key mới...\033[0m")
    else:
        print("\033[93mBạn chưa có key hoặc file key không tồn tại, sẽ lấy key mới...\033[0m")

    free_flow()

if __name__=="__main__":
    main()
