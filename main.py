import time
import os
import sys
import requests
from time import sleep
from datetime import datetime, timedelta
from pystyle import Colors, Colorate
# --- Hàm xóa kí tự trên màn hình ---
os.system("cls" if os.name == "nt" else "clear")
####
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=5)        
    except (requests.exceptions.ReadTimeout, requests.ConnectionError):
        print("════════════════════════════════════════════════  ")
        print("Không có kết nối mạng hoặc kết nối mạng không ổn định")
        print("Vui lòng kiểm tra kết nối mạng rồi thử lại")
        print("════════════════════════════════════════════════  ")
        sys.exit()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Lỗi: {str(e)}")
check_connection()   

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
print("[</>] Nhập Số 0 THOÁT TOOL")
print("[</>] Nhập Số 1 Bắt đầu đọc thông báo")
print("[</>] Nhập Số 2 Để cập nhật phiên bàn mới (nếu có thông báo)")
print("[</>] Nhập Số 3 Để tải gói tài nguyên nếu lần đầu chạy tool")


print("════════════════════════════════════════════════  ")
chon = str(input('[</>] Nhập Số \033[1;37m: '))

# Bắt sự kiện Ctrl + C một cách mượt mà
try:
    # tbbank
    if chon == '1' :
        exec(requests.get('https://raw.githubusercontent.com/leahminh/voice-tbbank/refs/heads/main/tbbank.py').text)  
    if chon == '2' :
        exec(requests.get('https://raw.githubusercontent.com/leahminh/voice-tbbank/refs/heads/main/update.py').text) 
    if chon == '3' :
        exec(requests.get('https://raw.githubusercontent.com/leahminh/voice-tbbank/refs/heads/main/setup.py').text) 
    else :
        print("\nĐã dừng chương trình.\n")
        exit()
except KeyboardInterrupt:
    # Xử lý khi nhấn Ctrl + C
    print("\nĐã dừng chương trình.\n")
    sys.exit()
