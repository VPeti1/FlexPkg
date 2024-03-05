import os
import time
import subprocess
import platform

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "linux"
    else:
        return "windows"

# Define the file path
file_path = "flex.pkg"

# Check if the file exists idk why
if os.path.exists(file_path):
    # Read the contents of the file
    with open(file_path, "r") as file:
        content = file.read()

    # Extract the texts after git =, git2 =, and git3 =
    git = content.split("git =")[1].split()[0].strip() if "git =" in content else None
    git2 = content.split("git2 =")[1].split()[0].strip() if "git2 =" in content else None
    git3 = content.split("git3 =")[1].split()[0].strip() if "git3 =" in content else None

    # Print the extracted values 
    print("Cloning these with git")     # Deez Nuts
    if git == None:
        u = "sless"
    else:
        print(f"{git}")
    if git2 == None:
        u = "sless"
    else:
        print(f"{git2}")

    if git3 == None:
        u = "sless"
    else:
        print(f"{git3}")

    print("Cloning these with git")
    pm = ""
    time.sleep(1.5)
    flex = "git"
    os = detect_os()
    if os == "linux":
        distro = input("What os are you using? (arch/debian/fedora/windows): ").lower()
        if distro == "arch":
            pm = "sudo pacman -S "
        elif distro == "debian":
            pm = "sudo apt install "
        elif distro == "fedora":
            pm = "sudo yum install "
        else:
            print("Unknown os. Please enter 'arch', 'debian','windows' or 'fedora'.")
            subprocess.call(['python', 'git.py'])
    else:
        pm = "choco install "
        print("Make sure you have choco installed")
        time.sleep(0.5)
    print("Installing Git")
    time.sleep(1)
    os.system(pm + flex)
    if git == None:
        u = "sless"
    else:
        os.system("git clone " + git)
    if git2 == None:
        u = "sless"
    else:
        os.system("git clone " + git2)

    if git3 == None:
        u = "sless"
    else:
        os.system("git clone " + git3)
    print("Repos cloned successfully")

else:
    print(f"Error reading from file!")
    quit()
