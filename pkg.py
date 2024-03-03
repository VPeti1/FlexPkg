import time
import os
import subprocess

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
        distro = input("What os are you using? (arch/debian/fedora/windows): ").lower()
        if distro == "arch":
            pm = "sudo pacman -S "
        elif distro == "debian":
            pm = "sudo apt install "
        elif distro == "fedora":
            pm = "sudo yum install "
        elif distro == "windows":
            pm = "choco install "
            print("Make sure you have choco installed")
            time.sleep(1.5)
        else:
            print("Unknown os. Please enter 'arch', 'debian','windows' or 'fedora'.")
            subprocess.call(['python', 'pkg.py'])
        time.sleep(1.5)
        os.system(pm + flex)



        
        

except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")