import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gtts import gTTS
from io import BytesIO
import os
import time
import sys
import requests
from time import sleep
from datetime import datetime, timedelta
from pystyle import Colors, Colorate
import platform
import shutil

# --- Hàm xóa sạch màn hình trên mọi thiết bị ---
def clear_screen():
    try:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            print("\033[2J\033[H", end="")  # Xóa bằng ANSI escape trên Unix
    except:
        print("\n" * 100)  # Dự phòng

clear_screen()

# Kiểm tra kết nối mạng
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)
        if response.status_code != 200:
            raise Exception("Phản hồi không hợp lệ")
        print("Đã kết nối mạng thành công!")
    except:
        print("❌ Không có kết nối mạng hoặc kết nối không ổn định.")
        sys.exit()

# Kiểm tra đã cài mpv chưa
def check_mpv():
    if not shutil.which("mpv"):
        print("⚠️ Bạn chưa cài 'mpv'! Vui lòng cài đặt:")
        print("• Windows: https://mpv.io/installation/")
        print("• Linux (Ubuntu): sudo apt install mpv")
        sys.exit()

check_connection()
check_mpv()

# Hàm banner
def banner():
    banner_text = f"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░██╗░░░░░░█████╗░███╗░░░███╗██████╗░███████╗██╗░░░░░██╗░
░░██║░░░░░██╔══██╗████╗░████║██╔══██╗██╔════╝╚██╗░░░██╔╝░
░░██║░░░░░███████║██╔████╔██║██║░░██║█████╗░░░╚██╗░██╔╝░░
░░██║░░░░░██╔══██║██║╚██╔╝██║██║░░██║██╔══╝░░░░╚████╔╝░░░
░░███████╗██║░░██║██║░╚═╝░██║██████╔╝███████╗░░░╚██╔╝░░░░
░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝░░░░╚═╝░░░░░
TOOL BY: LeAnhMinh - LAMDev              PHIÊN BẢN : 1.0.0
═════════════════════════════════════════════════════════
    """
    for X in banner_text:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)

os.system("cls" if os.name == "nt" else "clear")
banner()

# Hàm phát âm thanh từ link
def play_sound_from_url(url):
    os.system(f"mpv --no-video {url}")

# Hàm đọc nội dung giao dịch
def noi(transaction_time, so_tien, noidung):
    try:
        play_sound_from_url("https://tiengdong.com/wp-content/uploads/Tieng-tinh-tinh-www_tiengdong_com.mp3")
        time.sleep(1)

        if transaction_time:
            time_parts = transaction_time.split()
            time_str = time_parts[1] if len(time_parts) > 1 else ""
            hour, minute, _ = time_str.split(':')
            time_msg = f"{hour} giờ {minute} phút"
        else:
            time_msg = "không xác định thời gian"

        message = f"Giao dịch thành công. Đã nhận {so_tien} đồng vào lúc {time_msg}, nội dung: {noidung}"
        tts = gTTS(text=message, lang='vi')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        with open("tam.mp3", "wb") as f:
            f.write(mp3_fp.read())

        os.system("mpv --no-video tam.mp3")
        os.remove("tam.mp3")

    except Exception as e:
        print("❌ Lỗi đọc:", e)

# Kết nối Google Sheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

sheet_url = 'https://docs.google.com/spreadsheets/d/1yjfFXVNjxd6Gdady8Dk5GugA3W5cB0uXCcu7Ymoi7AE/edit#gid=0'
sheet = client.open_by_url(sheet_url).sheet1

# Đọc mã giao dịch cuối cùng
last_ma_gd = None
try:
    with open("LAMDev.txt", "r") as f:
        last_ma_gd = f.read().strip()
except FileNotFoundError:
    print("⚠️ Không tìm thấy file LAMDev.txt, sẽ bắt đầu từ đầu.")

print("🔄 Đang theo dõi giao dịch mới...")

# Vòng lặp kiểm tra
while True:
    try:
        data = sheet.get_all_records(head=2)
        for row in reversed(data):
            if row.get('Loại GD') == 'Giao dịch đến' and row.get('Trạng thái') == 'Thành công':
                ma_gd = row.get('Mã giao dịch')
                transaction_time = row.get('Thời gian tạo')
                noidung = row.get('Nội dung')
                so_tien = row.get('Số tiền (VND)')

                if ma_gd and ma_gd != last_ma_gd:
                    print(f"🔔 Giao dịch mới: {so_tien} | {transaction_time} | Nội dung: {noidung}")
                    noi(transaction_time, so_tien, noidung)
                    last_ma_gd = ma_gd
                    with open("LAMDev.txt", "w") as f:
                        f.write(ma_gd)
        time.sleep(5)
    except Exception as e:
        print("❌ Lỗi trong quá trình kiểm tra:", e)
        time.sleep(5)
