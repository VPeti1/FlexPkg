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
            if 'batch =' in line:
                batch_line = line.strip()
                break  # Stop searching after finding the first occurrence
        else:
            print(f"No batch invokes detected in the flex.pkg file")
            batch_line = None

    if batch_line:
        flex = batch_line.replace("batch = ", "")
        print(f"Found found batch file: {flex}")
        pm = ""
        distro = detect_os()
        if distro == "linux":
            print("Unsupported os")
            time.sleep(1.5)
            quit()
        elif distro == "windows":
            pm = "cmd /c " + flex
        else:
            quit()
        time.sleep(1.5)
        os.system(pm)



        
        

except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")