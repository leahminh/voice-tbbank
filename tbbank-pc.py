import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gtts import gTTS
from io import BytesIO
import os
import time
import sys
import requests
from time import sleep
from datetime import datetime
from playsound import playsound
import platform

# --- Hàm xóa màn hình ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

# --- Kiểm tra mạng ---
def check_connection():
    try:
        requests.get("https://www.google.com", timeout=3)
        print("✅ Đã kết nối mạng!")
    except:
        print("❌ Không có kết nối mạng.")
        sys.exit()

check_connection()

# --- Banner ---
def banner():
    text = f"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░██╗░░░░░░█████╗░███╗░░░███╗██████╗░███████╗██╗░░░░░██╗░
░░██║░░░░░██╔══██╗████╗░████║██╔══██╗██╔════╝╚██╗░░░██╔╝░
░░██║░░░░░███████║██╔████╔██║██║░░██║█████╗░░░╚██╗░██╔╝░░
░░██║░░░░░██╔══██║██║╚██╔╝██║██║░░██║██╔══╝░░░░╚████╔╝░░░
░░███████╗██║░░██║██║░╚═╝░██║██████╔╝███████╗░░░╚██╔╝░░░░
░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝░░░░╚═╝░░░░░
Tool by: Lê Anh Minh - LAMDev              Version: 1.0.0
═════════════════════════════════════════════════════════
"""
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.001)

banner()

# --- Phát âm thanh từ URL ---
def play_sound_from_url(url):
    try:
        # Tải file âm thanh từ URL
        response = requests.get(url)
        
        # Kiểm tra nếu tải thành công
        if response.status_code == 200:
            # Lưu âm thanh vào tệp tạm thời
            temp_filename = "temp_sound.mp3"
            with open(temp_filename, "wb") as f:
                f.write(response.content)

            # Phát âm thanh từ tệp tạm
            playsound(temp_filename)

            # Xóa tệp tạm sau khi phát xong
            os.remove(temp_filename)
        else:
            print(f"❌ Không thể tải âm thanh. Mã lỗi: {response.status_code}")
    except Exception as e:
        print(f"❌ Lỗi khi tải và phát âm thanh: {e}")

# --- TTS ---
def noi(text, time_str, so_tien, noidung):
    try:
        # Phát tiếng ting
        play_sound_from_url("https://tiengdong.com/wp-content/uploads/Tieng-tinh-tinh-www_tiengdong_com.mp3")

        # Tạo file tạm TTS
        hour, minute, *_ = time_str.split()[1].split(":")
        message = f"Giao dịch thành công, bạn đã nhận {so_tien} đồng vào lúc {hour} giờ {minute} phút. Nội dung: {noidung}"
        tts = gTTS(message, lang='vi')
        tts.save("temp.mp3")
        playsound("temp.mp3")
        os.remove("temp.mp3")
    except Exception as e:
        print(f"❌ Lỗi đọc TTS: {e}")

# --- Google Sheet ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1yjfFXVNjxd6Gdady8Dk5GugA3W5cB0uXCcu7Ymoi7AE/edit#gid=0").sheet1

# --- Lấy giao dịch cũ ---
last_ma = ""
try:
    with open("LAMDev.txt", "r") as f:
        last_ma = f.read().strip()
except:
    pass

print("🔄 Đang theo dõi giao dịch mới...")

# --- Theo dõi ---
while True:
    try:
        rows = sheet.get_all_records(head=2)
        for row in reversed(rows):
            if row.get("Loại GD") == "Giao dịch đến" and row.get("Trạng thái") == "Thành công":
                ma_gd = row.get("Mã giao dịch")
                time_gd = row.get("Thời gian tạo")
                noidung = row.get("Nội dung")
                so_tien = row.get("Số tiền (VND)")

                if ma_gd != last_ma:
                    noi("Thông báo", time_gd, so_tien, noidung)
                    last_ma = ma_gd
                    with open("LAMDev.txt", "w") as f:
                        f.write(ma_gd)
                    break
        time.sleep(3)
    except Exception as e:
        print("❌ Lỗi khi kiểm tra Sheet:", e)
        time.sleep(5)
