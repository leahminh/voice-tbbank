import sys
import subprocess

# Kiểm tra phiên bản Python >= 3.12.9
REQUIRED_PYTHON = (3, 12, 9)
if sys.version_info < REQUIRED_PYTHON:
    sys.exit(f"❌ Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}.{REQUIRED_PYTHON[2]} trở lên là bắt buộc!")

# Cài pip nếu chưa có
def ensure_pip():
    try:
        import pip
    except ImportError:
        print("⚠️ pip chưa được cài, đang tiến hành cài đặt...")
        subprocess.run([sys.executable, "-m", "ensurepip", "--default-pip"], check=True)

ensure_pip()

# Cài colorama trước để in màu
try:
    import colorama
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "colorama"], check=True)

from colorama import init, Fore
init(autoreset=True)

# Danh sách các thư viện cần thiết
REQUIRED_PACKAGES = [
    "time", "os", "sys", "requests", "datetime", "pystyle", "gspread", "oauth2client", "gtts",
    "platform", "io"
]

def install_libraries():
    print(Fore.CYAN + "📦 Đang cài đặt các thư viện...")
    for lib in REQUIRED_PACKAGES:
        print(Fore.BLUE + f"🔄 Cài: {lib}...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", lib], check=True)
    print(Fore.GREEN + "✅ Tất cả thư viện đã được cài.")

if __name__ == "__main__":
    install_libraries()
    print(Fore.MAGENTA + "🎉 Setup hoàn tất!")
    sys.exit()

