import time
import os
file_path = 'flex.pkg'

try:
    with open(file_path, 'r') as file:
        for line in file:
            if 'batch =' in line:
                batch_line = line.strip()
                break  # Stop searching after finding the first occurrence
        else:
            batch_line = None

    if batch_line:
        flex = batch_line.replace("batch = ", "")
        print(f"Found found batch file invoke: {flex}")
        pm = ""
        pm = "cmd /c " + flex
        time.sleep(1.5)
        os.system(pm)



        
        

except FileNotFoundError:
    print(f"An error occured while trying to read from the FLEXPKG file")