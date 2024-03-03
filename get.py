import os
import time
import subprocess

# Define the file path
file_path = "flex.pkg"


# Check if the file exists idk why
if os.path.exists(file_path):
    # Read the contents of the file
    with open(file_path, "r") as file:
        content = file.read()

    # Extract the texts after get =, get2 =, and get3 =
    get = content.split("get =")[1].split()[0].strip() if "get =" in content else None
    get2 = content.split("get2 =")[1].split()[0].strip() if "get2 =" in content else None
    get3 = content.split("get3 =")[1].split()[0].strip() if "get3 =" in content else None

    # Print the extracted values 
    print("Cloning these with get")     # Deez Nuts
    if get == None:
        u = "sless"
    else:
        print(f"{get}")
    if get2 == None:
        u = "sless"
    else:
        print(f"{get2}")

    if get3 == None:
        u = "sless"
    else:
        print(f"{get3}")

    print("Downloading files with WGET")
    time.sleep(1.5)
    flex = "wget"
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
        subprocess.call(['python', 'get.py'])
    print("Installing get")
    time.sleep(1)
    os.system(pm + flex)
    if get == None:
        u = "sless"
    else:
        os.system("wget " + get)
    if get2 == None:
        u = "sless"
    else:
        os.system("wget " + get2)

    if get3 == None:
        u = "sless"
    else:
        os.system("wget " + get3)
    print("Files downloaded successfully")

else:
    print(f"Error reading from file!")
