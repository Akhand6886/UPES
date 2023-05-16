import os
import zipfile
import requests

# Determine the latest version of ChromeDriver
url = "https://chromedriver.chromium.org/downloads"
response = requests.get(url)
latest_version = response.text.split('Latest Stable Release')[1].split('Latest Release')[0].split('ChromeDriver')[1].split(' - ')[0].strip()

# Determine the OS and architecture of the system
if os.name == "nt":
    system = "win"
    architecture = "32" if os.environ.get("PROCESSOR_ARCHITECTURE").endswith("64") else "32"
elif os.name == "posix":
    system = "mac" if "darwin" in os.uname().sysname.lower() else "linux"
    architecture = "64"

# Download and extract the ChromeDriver binary
url = f"https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_{system}{architecture}.zip"
response = requests.get(url)
with open("chromedriver.zip", "wb") as f:
    f.write(response.content)
with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
    zip_ref.extractall()

# Add the directory containing the ChromeDriver binary to the PATH
chromedriver_dir = os.path.abspath(os.curdir)
os.environ["PATH"] += os.pathsep + chromedriver_dir
