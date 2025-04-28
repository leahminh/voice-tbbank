import os
import sys
import requests
from datetime import datetime
from time import sleep
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
KEY_VIP_URL = "https://raw.githubusercontent.com/leahminh/voice-tbbank/refs/heads/main/keyvip.json"
START_SCRIPT_URL = "https://raw.githubusercontent.com/leahminh/voice-tbbank/refs/heads/main/start.py"

def save_key(key):
    """Lưu chỉ key vào file"""
    with open(KEY_FILE, "w") as f:
        f.write(key.strip())

def download_and_run(url):
    """Tải và thực thi script từ URL"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            exec(response.text, globals())
        else:
            print("Không thể tải script từ link:", url)
    except Exception as e:
        print("Lỗi tải script:", str(e))
        sys.exit()

def check_vip_key():
    """Kiểm tra key VIP"""
    while True:
        key = input("Vui lòng nhập key VIP của bạn: ").strip()
        try:
            response = requests.get(KEY_VIP_URL)
            if response.status_code == 200:
                vip_keys = response.text.splitlines()
                for vip_key in vip_keys:
                    key_data, expiry = vip_key.split("|")
                    if key == key_data:
                        expiry_date = datetime.strptime(expiry, "%d/%m/%Y")
                        if expiry_date >= datetime.now():
                            print(f"\033[92mKey đúng, hạn sử dụng đến: {expiry}")
                            save_key(key)  # Chỉ lưu key, không lưu ngày hết hạn
                            download_and_run(START_SCRIPT_URL)
                            return True  # Key hợp lệ, tiếp tục chương trình
                        else:
                            print(f"\033[91mKey hết hạn, vui lòng liên hệ admin để gia hạn. Hết hạn vào ngày: {expiry}")
                            # Yêu cầu nhập lại key
                            continue
                print("\033[91mKey sai, vui lòng nhập lại!\n")
            else:
                print("\033[91mKhông thể kiểm tra key VIP. Vui lòng thử lại sau!")
                sys.exit()
        except Exception as e:
            print("\033[91mLỗi khi kiểm tra key VIP:", str(e))
            sys.exit()

def main():
    # Kiểm tra key từ file
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            key = f.read().strip()
            # Kiểm tra key hợp lệ từ URL
            response = requests.get(KEY_VIP_URL)
            if response.status_code == 200:
                vip_keys = response.text.splitlines()
                for vip_key in vip_keys:
                    key_data, expiry = vip_key.split("|")
                    if key == key_data:
                        expiry_date = datetime.strptime(expiry, "%d/%m/%Y")
                        if expiry_date >= datetime.now():
                            print(f"\033[92mKey hợp lệ, hạn sử dụng đến: {expiry}")
                            sleep(5)
                            download_and_run(START_SCRIPT_URL)
                            return
                        else:
                            print(f"\033[91mKey đã hết hạn vào ngày: {expiry}")
                            os.remove(KEY_FILE)  # Xóa file key hết hạn
                            print("\033[93mVui lòng nhập lại key mới!")
                            check_vip_key()
                            return
            print("\033[91mKey không hợp lệ trong file. Vui lòng nhập lại key!")
            check_vip_key()
    else:
        print("\033[93mBạn chưa có key, vui lòng nhập key VIP.")
        check_vip_key()

if __name__ == "__main__":
    main()
