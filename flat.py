import time
import os
file_path = 'flex.pkg'

try:
    with open(file_path, 'r') as file:
        for line in file:
            if 'flatpak =' in line:
                flatpak_line = line.strip()
                break  # Stop searching after finding the first occurrence
        else:
            flatpak_line = None

    if flatpak_line:
        flex = flatpak_line.replace("flatpak = ", "")
        print(f"Found packages: {flex}")
        pm = "flatpak install " + flex
        time.sleep(1.5)
        os.system(pm)



        
        

except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")