import time
import os
import subprocess

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
        distro = input("What os are you using? (linux/windows): ").lower()
        if distro == "linux":
            pm = "sh " + flex
        elif distro == "windows":
            pm = "echo Unsupported action!"
            time.sleep(1.5)
        else:
            print("Unknown os. Please enter 'windows' or 'linux'.")
            subprocess.call(['python', 'sh.py'])
        time.sleep(1.5)
        os.system(pm)



        
        

except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")