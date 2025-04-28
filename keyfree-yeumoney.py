import os
import sys
import time
import hashlib
import requests
from datetime import datetime, timedelta
######
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
from playsound import playsound  # Thêm thư viện playsound


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
        {tieng_xanh}║ {cam}GIỚI HẠN THIẾT BỊ: {vang_cam}none      {cam}   KEY: {vang_cam}none            {tieng_xanh} ║
        {tieng_xanh}╚═══════════════════════════════════════════════════════╝
        
        {tieng_xanh}╔═══════════════════════════════════════════════════════╗
        {tieng_xanh}║ {do}Không có kết nối mạng hoặc kết nối mạng không ổn định {tieng_xanh}║
        {tieng_xanh}║ {do}Vui lòng kiểm tra kết nối mạng rồi thử lại            {tieng_xanh}║
        {tieng_xanh}╚═══════════════════════════════════════════════════════╝
        """
            for x in b:
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(0.000012000012)

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
        sleep(0.00012)

banner()
######

KEY_FILE = "Key-kich-hoat-tool-by-LAMDev.txt"
START_SCRIPT_URL = "https://raw.githubusercontent.com/leahminh/voice-tbbank/refs/heads/main/start.py"
YEUMONEY_TOKEN = "56489910cde0777fbe31a6af660956c76c7fc1e18d09e9b5f19ee9da745231fe"

def save_key(key):
    """Lưu key vào file mà không lưu ngày tháng hết hạn"""
    with open(KEY_FILE, "w") as f:
        f.write(f"{key}")
    print(f"\n\033[92m✔ Key đã lưu: {key}\033[0m\n")

def load_key():
    """Đọc key từ file"""
    if not os.path.exists(KEY_FILE):
        return None
    try:
        key = open(KEY_FILE).read().strip()
        return key
    except:
        return None

def run_start():
    """Tải và chạy script start.py"""
    code = requests.get(START_SCRIPT_URL).text
    exec(code, globals())
    sys.exit(0)

def generate_free_key():
    """Tạo key Free ngẫu nhiên 10 ký tự kèm tiền tố LAMDev"""
    raw = str(time.time()) + os.urandom(16).hex()
    return "LAMDev" + hashlib.sha256(raw.encode()).hexdigest()[:10]

def shorten_with_yeumoney(long_url):
    """Gọi API Yeumoney để rút gọn URL"""
    params = {"token": YEUMONEY_TOKEN, "format": "json", "url": long_url}
    try:
        r = requests.get("https://yeumoney.com/QL_api.php", params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        if data.get("status") == "success":
            return data.get("shortenedUrl")
    except Exception as e:
        print(f"\033[91m✘ Lỗi rút gọn URL: {e}\033[0m")
    return None

def free_flow():
    """Luồng lấy key Free qua Yeumoney"""
    key = generate_free_key()

    # Tạo URL chờ rút gọn
    long_url = f"https://keyfree.amteam.x10.mx?key={key}"
    short = shorten_with_yeumoney(long_url)
    if not short:
        print("\033[91m✘ Không rút gọn được link!\033[0m")
        sys.exit(1)

    # Hiển thị link
    print(f"\n\033[92mLink lấy key của bạn: {short}\033[0m\n")

    # Yêu cầu nhập lại key
    while True:
        inp = input("🔑 Nhập lại key vừa nhận: ").strip()
        if inp == key:
            save_key(key)
            run_start()
        else:
            print("\033[91m✘ Key sai, thử lại!\033[0m")

def main():
    # Bước 1: Kiểm tra key đã lưu
    key = load_key()
    if key:
        print(f"\033[92m✔ Đã có key hợp lệ: {key}\033[0m")
        run_start()
    else:
        print("\033[93mBạn chưa có key hoặc file key không tồn tại, sẽ lấy key mới...\033[0m")

    # Bước 2: Nếu không có key hợp lệ, vào luồng Free
    free_flow()

if __name__ == "__main__":
    main()
