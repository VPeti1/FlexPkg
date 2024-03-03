import time
import os

cmd = None
cmd2 = None
cmd3 = None

# Open the file in read mode
with open("flex.pkg", "r") as file:
    for line in file:
        if "cmd =" in line:
            cmd = line.strip().replace("cmd =", "").strip()
        elif "cmd2 =" in line:
            cmd2 = line.strip().replace("cmd2 =", "").strip()
        elif "cmd3 =" in line:
            cmd3 = line.strip().replace("cmd3 =", "").strip()

print("Found these commands:")
if cmd is not None:
    print(f"{cmd}")
if cmd2 is not None:
    print(f"{cmd2}")
if cmd3 is not None:
    print(f"{cmd3}")
print("Running commands")
time.sleep(1.5)
if cmd is not None:
    os.system(f"{cmd}")
if cmd2 is not None:
    os.system(f"{cmd2}")
if cmd3 is not None:
    os.system(f"{cmd3}")

