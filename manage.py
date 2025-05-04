import subprocess
import sys

required_packages = [
    "cryptography",
    "pycryptodome",
    "Pillow",
    "stepic"
]

def install_packages():
    for package in required_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"'{package}' installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to install '{package}'.")

if __name__ == "__main__":
    print("Installing required packages...")
    install_packages()
