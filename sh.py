import time
import os


file_path = 'flex.pkg'

try:
    with open(file_path, 'r') as file:
        for line in file:
            if 'sh =' in line:
                sh_line = line.strip()
                break  # Stop searching after finding the first occurrence
        else:
            sh_line = None

    if sh_line:
        flex = sh_line.replace("sh = ", "")
        print(f"Found found sh file: {flex}")
        pm = "sudo sh " + flex
        time.sleep(1.5)
        os.system(pm)



        
        

except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")
    quit()