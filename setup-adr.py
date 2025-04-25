import sys
import subprocess
import shutil
import platform

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

# ✅ Thư viện pip cần cài
REQUIRED_PACKAGES = [
    "requests", "pystyle", "gspread", "oauth2client", "gtts"
]

# ✅ Gói pkg cần cài trên Termux
TERMUX_PACKAGES = ["mpv"]

def install_libraries():
    print(Fore.CYAN + "📦 Đang cài đặt các thư viện qua pip...")
    for lib in REQUIRED_PACKAGES:
        print(Fore.BLUE + f"🔄 Cài pip: {lib}...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", lib], check=True)
    print(Fore.GREEN + "✅ Các thư viện pip đã cài xong.")

def install_termux_packages():
    if "Android" in platform.uname().release or "termux" in sys.executable.lower():
        print(Fore.CYAN + "📦 Đang cài các gói cần thiết qua pkg...")
        for pkg in TERMUX_PACKAGES:
            print(Fore.BLUE + f"🔄 Cài pkg: {pkg}...")
            subprocess.run(["pkg", "install", "-y", pkg], check=True)
        print(Fore.GREEN + "✅ Các gói pkg đã cài xong.")

if __name__ == "__main__":
    install_libraries()
    install_termux_packages()
    print(Fore.MAGENTA + "🎉 Setup hoàn tất!")
    sys.exit()
