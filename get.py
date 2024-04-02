import os
import time
import subprocess
import platform

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "linux"
    else:
        return "windows"

# Define the file path
file_path = "flex.pkg"


# Check if the file exists idk why
if os.path.exists(file_path):
    # Read the contents of the file
    with open(file_path, "r") as file:
        content = file.read()

    # Extract the texts after get =, get2 =, and get3 =
    get = content.split("get =")[1].split()[0].strip() if "get =" in content else None
    get2 = content.split("get2 =")[1].split()[0].strip() if "get2 =" in content else None
    get3 = content.split("get3 =")[1].split()[0].strip() if "get3 =" in content else None

    # Print the extracted values 
    print("Downloading the files with WGET")     # Deez Nuts
    if get == None:
        pass
    else:
        print(f"{get}")
    if get2 == None:
        pass
    else:
        print(f"{get2}")

    if get3 == None:
        pass
    else:
        print(f"{get3}")

    print("Downloading files with WGET")
    time.sleep(1.5)
    flex = "wget"
    pm = ""
    time.sleep(1.5)
    pm = ""
    time.sleep(1.5)
    flex = "git"
    if os.path.isfile('/usr/flex/arch.cw'):
        pm = "sudo pacman -S "
    elif os.path.isfile('/usr/flex/deb.cw'):
        pm = "sudo apt install "
    elif os.path.isfile('/usr/flex/fed.cw'):
        pm = "sudo yum install "
    elif os.path.isfile('/usr/flex/suse.cw'):
        pm = "sudo zypper install "
    elif os.path.isfile('/usr/flex/void.cw'):
        pm = "sudo xbps-install "
    else:
        pm = "choco install "
    print("Installing get")
    time.sleep(1)
    os.system(pm + flex)
    if get == None:
        pass
    else:
        os.system("wget " + get)
    if get2 == None:
        pass
    else:
        os.system("wget " + get2)

    if get3 == None:
        pass
    else:
        os.system("wget " + get3)
    print("Files downloaded successfully")

else:
    print(f"Error reading from file!")
