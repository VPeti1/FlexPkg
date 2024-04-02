import os
import time

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
        pass
    else:
        print(f"{git}")
    if git2 == None:
        pass
    else:
        print(f"{git2}")

    if git3 == None:
        pass
    else:
        print(f"{git3}")

    print("Cloning these with git")
    pm = ""
    time.sleep(1.5)
    flex = "git"
    if os.path.isfile('/usr/flex/arch.cw'):
        pm = "sudo pacman -S "
    elif os.path.isfile('/usr/flex/deb.cw'):
        pm = "sudo apt install "
    elif os.path.isfile('/usr/flex/fed.cw'):
        pm = "sudo yum install "
    elif os.path.isfile('/usr/flex/suse.cw'):
            pm = "sudo zypper install "
    elif os.path.isfile('/usr/flex/void.cw'):
            pm = "sudo xbps-install "
    else:
        pm = "choco install "
    print("Installing Git")
    time.sleep(1)
    os.system(pm + flex)
    if git == None:
        pass
    else:
        os.system("git clone " + git)
    if git2 == None:
        pass
    else:
        os.system("git clone " + git2)

    if git3 == None:
        pass
    else:
        os.system("git clone " + git3)
    print("Repos cloned successfully")

else:
    print(f"Error reading from file!")
    quit()
