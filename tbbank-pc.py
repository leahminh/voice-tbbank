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

# Kiểm tra kết nối mạng
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)
        if response.status_code != 200:
            raise Exception("Phản hồi không hợp lệ")
        print("Đã kết nối mạng thành công!")
    except (requests.exceptions.ReadTimeout, requests.ConnectionError, requests.exceptions.RequestException, Exception):
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print("░░██╗░░░░░░█████╗░███╗░░░███╗██████╗░███████╗██╗░░░░░██╗░")
        print("░░██║░░░░░██╔══██╗████╗░████║██╔══██╗██╔════╝╚██╗░░░██╔╝░")
        print("░░██║░░░░░███████║██╔████╔██║██║░░██║█████╗░░░╚██╗░██╔╝░░")
        print("░░██║░░░░░██╔══██║██║╚██╔╝██║██║░░██║██╔══╝░░░░╚████╔╝░░░")
        print("░░███████╗██║░░██║██║░╚═╝░██║██████╔╝███████╗░░░╚██╔╝░░░░")
        print("░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝░░░░╚═╝░░░░░")
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
        print("TOOL BY:LeAnhMinh - LAMDev              PHIÊN BẢN : 1.0.0")
        print("════════════════════════════════════════════════  ")
        print("Không có kết nối mạng hoặc kết nối mạng không ổn định")
        print("Vui lòng kiểm tra kết nối mạng rồi thử lại")
        print("════════════════════════════════════════════════  ")
        sys.exit()  # Dừng chương trình nếu không có mạng

# Kiểm tra kết nối mạng khi bắt đầu chạy
check_connection()

# Phần còn lại của tool sẽ chạy bình thường nếu có mạng
print("Tool đang chạy bình thường...")

# Hàm banner
def banner():
    banner = f"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░██╗░░░░░░█████╗░███╗░░░███╗██████╗░███████╗██╗░░░░░██╗░
░░██║░░░░░██╔══██╗████╗░████║██╔══██╗██╔════╝╚██╗░░░██╔╝░
░░██║░░░░░███████║██╔████╔██║██║░░██║█████╗░░░╚██╗░██╔╝░░
░░██║░░░░░██╔══██║██║╚██╔╝██║██║░░██║██╔══╝░░░░╚████╔╝░░░
░░███████╗██║░░██║██║░╚═╝░██║██████╔╝███████╗░░░╚██╔╝░░░░
░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝░░░░╚═╝░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

TOOL BY:LeAnhMinh - LAMDev              PHIÊN BẢN : 1.0.0
═════════════════════════════════════════════════════════
[</>] BOX ZALO : 
═════════════════════════════════════════════════════════ 
[</>] GIỚI HẠN THIẾT BỊ : 1 🚦
[</>] NGƯỜI MUA : USER.....
[</>] KEY : LAMDev*********
═════════════════════════════════════════════════════════                              
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
os.system("cls" if os.name == "nt" else "clear")
banner()

# Hàm phát âm thanh từ link
def play_sound_from_url(url):
    os.system(f"mpv --no-video {url}")

# Hàm đọc thông tin thời gian giao dịch và số tiền
def noi(text, transaction_time, so_tien, noidung):
    try:
        # Phát tiếng ting trước
        play_sound_from_url("https://tiengdong.com/wp-content/uploads/Tieng-tinh-tinh-www_tiengdong_com.mp3")

        # Chờ 1 giây
        time.sleep(0.001)

        # Lấy giờ và phút từ thời gian
        if transaction_time:
            # Tách ngày và giờ
            time_parts = transaction_time.split()  # Tách ngày và giờ
            time_str = time_parts[1] if len(time_parts) > 1 else ""  # Lấy phần giờ:phút
            hour, minute, _ = time_str.split(':')  # Tách giờ, phút, giây
            time_msg = f" {hour} giờ {minute} phút"
        else:
            time_msg = "Thời gian không xác định"

        # TTS - Thông báo "Giao dịch thành công, bạn đã nhận [so_tien] đồng vào [time_msg]"
        message = f"Giao dịch thành công, Đã nhận {so_tien} đồng vào lúc {time_msg}, nội dung {noidung}"
        tts = gTTS(text=message, lang='vi')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        temp_path = "tam.mp3"
        with open(temp_path, "wb") as f:
            f.write(mp3_fp.read())

        os.system(f"mpv --no-video {temp_path}")
        os.remove(temp_path)

    except Exception as e:
        print("❌ Lỗi đọc:", e)

# Kết nối Google Sheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

sheet_url = 'https://docs.google.com/spreadsheets/d/1yjfFXVNjxd6Gdady8Dk5GugA3W5cB0uXCcu7Ymoi7AE/edit#gid=0'
sheet = client.open_by_url(sheet_url).sheet1

# Đọc mã giao dịch cuối cùng từ file
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
        data = sheet.get_all_records(head=2)  # Dòng tiêu đề là dòng 2
        for row in reversed(data):
            if row.get('Loại GD') == 'Giao dịch đến' and row.get('Trạng thái') == 'Thành công':
                ma_gd = row.get('Mã giao dịch')
                transaction_time = row.get('Thời gian tạo')  # Lấy thời gian giao dịch từ cột 'Thời Gian Tạo'
                noidung = row.get('Nội dung')  # Lấy thời gian giao dịch từ cột 'Nội dung'
                if ma_gd and ma_gd != last_ma_gd:
                    so_tien = row.get('Số tiền (VND)')
                    if transaction_time:
                        noi("Giao dịch thành công", transaction_time, so_tien, noidung)  # Truyền thời gian vào hàm
                    else:
                        print(f"❌ Thời gian không có giá trị cho giao dịch {ma_gd}.")
                    print(f"✅ Giao dịch mới:\n- Mã Giao Dịch: {ma_gd}\n- {so_tien} VND\n- Thời gian: {transaction_time}\n- Nội dung: {noidung}")
                    last_ma_gd = ma_gd  # Lưu lại mã giao dịch đã xử lý
                    with open("LAMDev.txt", "w") as f:
                        f.write(ma_gd)  # Ghi lại mã giao dịch vào file
        sleep(10)  # Kiểm tra sau 10 giây
    except Exception as e:
        print(f"❌ Lỗi trong quá trình theo dõi giao dịch: {e}")
        sleep(10)
