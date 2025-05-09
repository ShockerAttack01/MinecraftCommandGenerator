import subprocess
import sys

def install_requirements():
    """
    Installs the dependencies listed in requirements.txt.
    This script:
    - Upgrades pip, setuptools, and wheel.
    - Installs all dependencies from requirements.txt.
    - Exits with an error message if any step fails.
    """
    try:
        # Upgrade pip, setuptools, and wheel
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
        
        # Install dependencies from requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        
        print("✅ All requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred while installing requirements: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
