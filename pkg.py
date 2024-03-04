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
            print(f"No packages detected in the flex.pkg file")
            pkg_line = None

    if pkg_line:
        flex = pkg_line.replace("pkg = ", "")
        print(f"Found packages: {flex}")
        pm = ""
        chk = detect_os()
        if chk == "linux":
            distro = input("What os are you using? (arch/debian/fedora): \n(Derivatives included)\n").lower()
            if distro == "arch":
                pm = "sudo pacman -S "
            elif distro == "debian":
                pm = "sudo apt install "
            elif distro == "fedora":
                pm = "sudo yum install "
            else:
                print("Unknown os. Please enter 'arch', 'debian' or 'fedora'.")
                subprocess.call(['python', 'pkg.py'])
        elif chk == "windows":
            pm = "choco install "
            print("Make sure you have choco installed")
            time.sleep(1.5)
        else:
            print("Unsupported os detected!")
        time.sleep(1.5)
        os.system(pm + flex)
        print("Packages installed succesfully")


except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")