import sys
import subprocess
from colorama import init, Fore

init(autoreset=True)

REQUIRED_PYTHON = (3, 12, 9)
if sys.version_info < REQUIRED_PYTHON:
    sys.exit(f"❌ Yêu cầu Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}.{REQUIRED_PYTHON[2]} trở lên!")

# Cài pip nếu chưa có
def ensure_pip():
    try:
        import pip
    except ImportError:
        print(Fore.YELLOW + "⚠️ pip chưa có, đang cài…")
        subprocess.run([sys.executable, "-m", "ensurepip", "--default-pip"], check=True)

# Cài các thư viện Python
def install_pip_libs():
    libs = ["colorama", "requests", "pystyle", "gspread", "oauth2client", "gtts"]
    print(Fore.CYAN + "📦 Cài thư viện pip...")
    for lib in libs:
        print(Fore.BLUE + f"🔄 pip install: {lib}")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", lib], check=True)
    print(Fore.GREEN + "✅ Đã cài xong thư viện pip.")

# Cài các gói pkg (chỉ dành cho Termux)
def install_termux_packages():
    pkgs = ["mpv"]
    print(Fore.CYAN + "📦 Cài gói pkg...")
    subprocess.run(["pkg", "update", "-y"])
    subprocess.run(["pkg", "upgrade", "-y"])
    for pkg in pkgs:
        print(Fore.BLUE + f"🔄 pkg install: {pkg}")
        subprocess.run(["pkg", "install", "-y", pkg])
    print(Fore.GREEN + "✅ Đã cài xong gói pkg.")

if __name__ == "__main__":
    ensure_pip()
    install_pip_libs()
    install_termux_packages()
    print(Fore.MAGENTA + "🎉 Hoàn tất setup!")
