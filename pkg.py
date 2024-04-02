import time
import os
import subprocess
import platform

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "linux"
    else:
        return "windows"

file_path = 'flex.pkg'

try:
    with open(file_path, 'r') as file:
        for line in file:
            if 'pkg =' in line:
                pkg_line = line.strip()
                break  # Stop searching after finding the first occurrence
        else:
            pkg_line = None

    if pkg_line:
        pm = ''
        flex = pkg_line.replace("pkg =", "").strip()  # Remove extra spaces
        print(f"Found packages: {flex}")
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
        time.sleep(1.5)
        os.system(pm + flex)
        print("Packages installed successfully")

except FileNotFoundError:
    pass
