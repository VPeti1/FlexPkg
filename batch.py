import time
import os
import subprocess

file_path = 'flex.pkg'

try:
    with open(file_path, 'r') as file:
        for line in file:
            if 'batch =' in line:
                batch_line = line.strip()
                break  # Stop searching after finding the first occurrence
        else:
            print(f"No batch packages detected in the flex.pkg file")
            batch_line = None

    if batch_line:
        flex = batch_line.replace("batch = ", "")
        print(f"Found found batch file: {flex}")
        pm = ""
        distro = input("What os are you using? (linux/windows): ").lower()
        if distro == "linux":
            pm = "echo Unsupported action!"
            time.sleep(1.5)
        elif distro == "windows":
            pm = "cmd /c " + flex
        else:
            print("Unknown os. Please enter 'windows' or 'linux'.")
            subprocess.call(['python', 'batch.py'])
        time.sleep(1.5)
        os.system(pm)



        
        

except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")