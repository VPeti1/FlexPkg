import time
import os
import subprocess

file_path = 'flex.pkg'

try:
    with open(file_path, 'r') as file:
        for line in file:
            if 'flatpak =' in line:
                flatpak_line = line.strip()
                break  # Stop searching after finding the first occurrence
        else:
            print(f"No flatpak packages detected in the flex.pkg file")
            flatpak_line = None

    if flatpak_line:
        flex = flatpak_line.replace("flatpak = ", "")
        print(f"Found packages: {flex}")
        pm = ""
        distro = input("What os are you using? (linux/windows): ").lower()
        if distro == "linux":
            pm = "flatpak install " + flex
        elif distro == "windows":
            pm = "echo Unsupported action!"
            time.sleep(1.5)
        else:
            print("Unknown os. Please enter 'windows' or 'linux'.")
            subprocess.call(['python', 'flat.py'])
        time.sleep(1.5)
        os.system(pm)



        
        

except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")