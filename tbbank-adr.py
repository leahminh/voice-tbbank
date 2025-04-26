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
import os
import platform

# --- Hàm xóa sạch màn hình trên mọi thiết bị ---
def clear_screen():
    try:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            print("\033[2J\033[H", end="")  # Xóa bằng ANSI escape trên Unix
    except:
        print("\n" * 100)  # Dự phòng

# --- Gọi xóa màn hình khi khởi động ---
clear_screen()

# Ma mau ANSI
do = "\033[91m"        # Ma mau do
xanh_la = "\033[92m"    # Ma mau xanh la sang nhat
vang = "\033[93m"      # Ma mau vang
vang_cam = "\033[38;5;220m"       # Ma vang cam 
xanh_duong = "\033[94m" # Ma mau xanh duong
tim = "\033[95m"       # Ma mau tim
xanh_lam = "\033[38;2;51;153;255m"   # Ma mau xanh lam nhat
trang = "\033[97m"     # Ma mau trang
den = "\033[90m"       # Ma mau den
xanh_nuocbien = "\033[34m"  # Ma mau xanh nuoc bien
cam = "\033[38;5;214m"  # Ma mau cam sang
hong = "\033[38;5;206m"   # Ma mau hong
xanh_2 = "\033[38;5;82m"  # Ma mau xanh 2
xanh_la_nhat = "\033[38;5;34m"  # Ma mau xanh la nhat
tieng_xanh = "\033[38;5;39m"  # Ma mau xanh tieu
baner_nen = "\033[38;2;0;0;255m"
baner_chu = "\033[38;2;0;255;255m"
baner_bong = "\033[38;2;255;255;153m"

reset = "\033[0m"       # Dat lai ma mau ban dau

# Kiểm tra kết nối mạng
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)
        if response.status_code != 200:
            raise Exception("{do}Phản hồi không hợp lệ")
        print("{xanh_la}Đã kết nối mạng thành công!")
    except (requests.exceptions.ReadTimeout, requests.ConnectionError, requests.exceptions.RequestException, Exception):
        def banner():
            # --- Hàm xóa sạch màn hình trên mọi thiết bị ---
            def clear_screen():
                try:
                    if platform.system() == "Windows":
                        os.system("cls")
                    else:
                        print("\033[2J\033[H", end="")  # Xóa bằng ANSI escape trên Unix
                except:
                    print("\n" * 100)  # Dự phòng

            # --- Gọi xóa màn hình khi khởi động ---
            clear_screen()
            b = f"""
        {baner_nen}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        {baner_nen}░░{baner_chu}██{baner_bong}╗{baner_nen}░░░░░░{baner_chu}█████{baner_bong}╗{baner_nen}░{baner_chu}███{baner_bong}╗{baner_nen}░░░{baner_chu}███{baner_bong}╗{baner_chu}██████{baner_bong}╗{baner_nen}░{baner_chu}███████{baner_bong}╗{baner_chu}██{baner_bong}╗{baner_nen}░░░░░{baner_chu}██{baner_bong}╗{baner_nen}░
        {baner_nen}░░{baner_chu}██{baner_bong}║{baner_nen}░░░░░{baner_chu}██{baner_bong}╔══{baner_chu}██{baner_bong}╗{baner_chu}████{baner_bong}╗{baner_nen}░{baner_chu}████{baner_bong}║{baner_chu}██{baner_bong}╔══{baner_chu}██{baner_bong}╗{baner_chu}██{baner_bong}╔════╝╚{baner_chu}██{baner_bong}╗{baner_nen}░░░{baner_chu}██{baner_bong}╔╝{baner_nen}░
        {baner_nen}░░{baner_chu}██{baner_bong}║{baner_nen}░░░░░{baner_chu}███████{baner_bong}║{baner_chu}██{baner_bong}╔{baner_chu}████{baner_bong}╔{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}║{baner_nen}░░{baner_chu}██{baner_bong}║{baner_chu}█████{baner_bong}╗{baner_nen}░░░{baner_bong}╚{baner_chu}██{baner_bong}╗{baner_nen}░{baner_chu}██{baner_bong}╔╝{baner_nen}░░
        {baner_nen}░░{baner_chu}██{baner_bong}║{baner_nen}░░░░░{baner_chu}██{baner_bong}╔══{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}║╚{baner_chu}██{baner_bong}╔╝{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}║{baner_nen}░░{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}╔══╝{baner_nen}░░░░{baner_bong}╚{baner_chu}████{baner_bong}╔╝{baner_nen}░░░
        {baner_nen}░░{baner_chu}███████{baner_bong}╗{baner_chu}██{baner_bong}{baner_bong}║{baner_nen}░░{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}║{baner_nen}░{baner_bong}╚═╝{baner_nen}░{baner_chu}██{baner_bong}║{baner_chu}██████{baner_bong}╔╝{baner_chu}███████{baner_bong}╗{baner_nen}░░░{baner_bong}╚{baner_chu}██{baner_bong}╔╝{baner_nen}░░░░
        {baner_nen}░░{baner_bong}╚══════╝╚═╝{baner_nen}░░{baner_bong}╚═╝╚═╝{baner_nen}░░░░░{baner_bong}╚═╝╚═════╝{baner_nen}░{baner_bong}╚══════╝{baner_nen}░░░░{baner_bong}╚═╝{baner_nen}░░░░░
        {baner_nen}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        
        {tieng_xanh}╔═══════════════════════════════════════════════════════╗
        {tieng_xanh}║       {hong}TOOL THÔNG BÁO GIAO DỊCH BẰNG GIỌNG NÓI         {tieng_xanh}║
        {tieng_xanh}╠═══════════════════════════════════════════════════════╣
        {tieng_xanh}║ {cam}TOOL BY: {vang_cam}LeAnhMinh - LAMDev          {cam}PHIÊN BẢN: {vang_cam}1.0.0 {tieng_xanh}║
        {tieng_xanh}║ {cam}BOX ZALO SUPPORT: {vang_cam}https://zalo.me/g/boiqoq426         {tieng_xanh}║
        {tieng_xanh}║ {cam}PROFILE ADMIN: {vang_cam}https://leanhminh.io.vn                {tieng_xanh}║
        {tieng_xanh}║ {cam}WEDSITE: {vang_cam}https://dichvusale.io.vn                     {tieng_xanh}║
        {tieng_xanh}║ {cam}GIỚI HẠN THIẾT BỊ: {vang_cam}1 Thiết bị{cam}   KEY: {vang_cam}LAMDev**********{tieng_xanh} ║
        {tieng_xanh}╚═══════════════════════════════════════════════════════╝
        
        {tieng_xanh}╔═══════════════════════════════════════════════════════╗
        {tieng_xanh}║ {do}Không có kết nối mạng hoặc kết nối mạng không ổn định {tieng_xanh}║
        {tieng_xanh}║ {do}Vui lòng kiểm tra kết nối mạng rồi thử lại            {tieng_xanh}║
        {tieng_xanh}╚═══════════════════════════════════════════════════════╝
        """
            for x in b:
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(0.000012)

        banner()
        sys.exit()  # Dừng chương trình nếu không có mạng

# Kiểm tra kết nối mạng khi bắt đầu chạy
check_connection()

# Phần còn lại của tool sẽ chạy bình thường nếu có mạng
print("{xanh_la}Tool đang chạy bình thường...")

# Hàm banner
def banner():
    # --- Hàm xóa sạch màn hình trên mọi thiết bị ---
    def clear_screen():
        try:
            if platform.system() == "Windows":
                os.system("cls")
            else:
                print("\033[2J\033[H", end="")  # Xóa bằng ANSI escape trên Unix
        except:
            print("\n" * 100)  # Dự phòng

    # --- Gọi xóa màn hình khi khởi động ---
    clear_screen()
    b = f"""
{baner_nen}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{baner_nen}░░{baner_chu}██{baner_bong}╗{baner_nen}░░░░░░{baner_chu}█████{baner_bong}╗{baner_nen}░{baner_chu}███{baner_bong}╗{baner_nen}░░░{baner_chu}███{baner_bong}╗{baner_chu}██████{baner_bong}╗{baner_nen}░{baner_chu}███████{baner_bong}╗{baner_chu}██{baner_bong}╗{baner_nen}░░░░░{baner_chu}██{baner_bong}╗{baner_nen}░
{baner_nen}░░{baner_chu}██{baner_bong}║{baner_nen}░░░░░{baner_chu}██{baner_bong}╔══{baner_chu}██{baner_bong}╗{baner_chu}████{baner_bong}╗{baner_nen}░{baner_chu}████{baner_bong}║{baner_chu}██{baner_bong}╔══{baner_chu}██{baner_bong}╗{baner_chu}██{baner_bong}╔════╝╚{baner_chu}██{baner_bong}╗{baner_nen}░░░{baner_chu}██{baner_bong}╔╝{baner_nen}░
{baner_nen}░░{baner_chu}██{baner_bong}║{baner_nen}░░░░░{baner_chu}███████{baner_bong}║{baner_chu}██{baner_bong}╔{baner_chu}████{baner_bong}╔{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}║{baner_nen}░░{baner_chu}██{baner_bong}║{baner_chu}█████{baner_bong}╗{baner_nen}░░░{baner_bong}╚{baner_chu}██{baner_bong}╗{baner_nen}░{baner_chu}██{baner_bong}╔╝{baner_nen}░░
{baner_nen}░░{baner_chu}██{baner_bong}║{baner_nen}░░░░░{baner_chu}██{baner_bong}╔══{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}║╚{baner_chu}██{baner_bong}╔╝{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}║{baner_nen}░░{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}╔══╝{baner_nen}░░░░{baner_bong}╚{baner_chu}████{baner_bong}╔╝{baner_nen}░░░
{baner_nen}░░{baner_chu}███████{baner_bong}╗{baner_chu}██{baner_bong}{baner_bong}║{baner_nen}░░{baner_chu}██{baner_bong}║{baner_chu}██{baner_bong}║{baner_nen}░{baner_bong}╚═╝{baner_nen}░{baner_chu}██{baner_bong}║{baner_chu}██████{baner_bong}╔╝{baner_chu}███████{baner_bong}╗{baner_nen}░░░{baner_bong}╚{baner_chu}██{baner_bong}╔╝{baner_nen}░░░░
{baner_nen}░░{baner_bong}╚══════╝╚═╝{baner_nen}░░{baner_bong}╚═╝╚═╝{baner_nen}░░░░░{baner_bong}╚═╝╚═════╝{baner_nen}░{baner_bong}╚══════╝{baner_nen}░░░░{baner_bong}╚═╝{baner_nen}░░░░░
{baner_nen}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

{tieng_xanh}╔═══════════════════════════════════════════════════════╗
{tieng_xanh}║       {hong}TOOL THÔNG BÁO GIAO DỊCH BẰNG GIỌNG NÓI         {tieng_xanh}║
{tieng_xanh}╠═══════════════════════════════════════════════════════╣
{tieng_xanh}║ {cam}TOOL BY: {vang_cam}LeAnhMinh - LAMDev          {cam}PHIÊN BẢN: {vang_cam}1.0.0 {tieng_xanh}║
{tieng_xanh}║ {cam}BOX ZALO SUPPORT: {vang_cam}https://zalo.me/g/boiqoq426         {tieng_xanh}║
{tieng_xanh}║ {cam}PROFILE ADMIN: {vang_cam}https://leanhminh.io.vn                {tieng_xanh}║
{tieng_xanh}║ {cam}WEDSITE: {vang_cam}https://dichvusale.io.vn                     {tieng_xanh}║
{tieng_xanh}║ {cam}GIỚI HẠN THIẾT BỊ: {vang_cam}1 Thiết bị{cam}   KEY: {vang_cam}LAMDev**********{tieng_xanh} ║
{tieng_xanh}╚═══════════════════════════════════════════════════════╝

"""
    for x in b:
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(0.000012)

banner()

# Hàm phát âm thanh từ link (ẩn mọi log)
def play_sound_from_url(url):
    subprocess.run(
        ["mpv", "--no-video", url],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

# Hàm đọc thông tin thời gian giao dịch và số tiền
def noi(text, transaction_time, so_tien):
    try:
        play_sound_from_url("https://tiengdong.com/wp-content/uploads/Tieng-tinh-tinh-www_tiengdong_com.mp3")
        time.sleep(0.1)
        if transaction_time:
            parts = transaction_time.split()
            hour, minute, _ = parts[1].split(':')
            time_msg = f"{hour} giờ {minute} phút"
        else:
            time_msg = "Thời gian không xác định"
        message = f"Giao dịch thành công, Đã nhận {so_tien} đồng vào lúc {time_msg}"
        tts = gTTS(text=message, lang='vi')
        buf = BytesIO(); tts.write_to_fp(buf); buf.seek(0)
        with open("tam.mp3", "wb") as f: f.write(buf.read())
        subprocess.run(
            ["mpv", "--no-video", "tam.mp3"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        os.remove("tam.mp3")
    except Exception as e:
        print(f"{do}❌ Lỗi đọc: {e}{reset}")

# Kết nối Google Sheet
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(
    'https://docs.google.com/spreadsheets/d/1yjfFXVNjxd6Gdady8Dk5GugA3W5cB0uXCcu7Ymoi7AE/edit#gid=0'
).sheet1

# Đọc mã giao dịch cuối cùng
last_ma_gd = None
try:
    with open("LAMDev.txt","r") as f:
        last_ma_gd = f.read().strip()
except FileNotFoundError:
    pass

print(f"{tieng_xanh}🔄 Đang theo dõi giao dịch mới...{reset}")

# Vòng lặp kiểm tra
while True:
    try:
        data = sheet.get_all_records(head=2)
        for row in reversed(data):
            if row.get('Loại GD')=='Giao dịch đến' and row.get('Trạng thái')=='Thành công':
                ma_gd = row.get('Mã giao dịch')
                transaction_time = row.get('Thời gian tạo')
                noidung = row.get('Nội dung')
                taikhoan = row.get('Tài khoản nhận')
                if ma_gd and ma_gd!=last_ma_gd:
                    so_tien = row.get('Số tiền (VND)')
                    noi("Giao dịch thành công", transaction_time, so_tien)
                    print(
                        f"{trang}-----------------------{reset}\n"
                        f"{xanh_la}✅ Giao dịch đến mới:\n"
                        f"{vang}- STK - Ngân Hàng Nhận: {taikhoan}\n"
                        f"- Mã Giao Dịch: {ma_gd}\n"
                        f"- Số tiền: {so_tien} VND\n"
                        f"- Thời gian: {transaction_time}\n"
                        f"- Nội Dung: {noidung}{reset}"
                    )
                    last_ma_gd = ma_gd
                    with open("LAMDev.txt","w") as f:
                        f.write(ma_gd)
                break
    except Exception as e:
        time.sleep(10)
    time.sleep(5)
