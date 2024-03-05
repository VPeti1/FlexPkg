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
            if 'sh =' in line:
                sh_line = line.strip()
                break  # Stop searching after finding the first occurrence
        else:
            print(f"No sh packages detected in the flex.pkg file")
            sh_line = None

    if sh_line:
        flex = sh_line.replace("sh = ", "")
        print(f"Found found sh file: {flex}")
        pm = ""
        distro = detect_os()
        if distro == "linux":
            pm = "sh " + flex
        elif distro == "windows":
            print("Unsupported os!")
            time.sleep(1.5)
            quit()
        else:
            print("Unsupported os!")
            time.sleep(1.5)
            quit()
        time.sleep(1.5)
        os.system(pm)



        
        

except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")
    quit()