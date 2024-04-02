import subprocess
import time
import platform
import os

def check_pipe_character(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            if '|' in content:
                print("WARNNG!\n Unsafe flex.pkg file detected!")
                con = input("Do you want to continue? (yes or no)\n")
                if con == "yes":
                    pass
                else:
                    quit()
            else:
                pass
    except FileNotFoundError:
        pass

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "linux"
    else:
        return "windows"

def chococ():
    os = detect_os()
    if os == "linux":
        pass
    else:
        subprocess.run('chococ.exe', shell=True)

def shell():
    os = detect_os()
    if os == "linux":
        subprocess.call(['python', 'flat.py'])
        subprocess.call(['python', 'sh.py'])
    else:
        subprocess.call(['python', 'batch.py'])


def osr():
    
    try:
        result = subprocess.run(['python', 'osr.py'], check=True)
        if result.returncode == 10:
            pass
        else:
            pass
    except subprocess.CalledProcessError as e:
        quit()

def osys():
    chk = detect_os()
    if chk == "linux":
            if os.path.isfile('/usr/flex/arch.cw'):
                pass
            elif os.path.isfile('/usr/flex/deb.cw'):
                pass
            elif os.path.isfile('/usr/flex/fed.cw'):
                pass
            elif os.path.isfile('/usr/flex/void.cw'):
                pass
            elif os.path.isfile('/usr/flex/suse.cw'):
                pass
            else:
                distro = input("What os are you using? (arch/debian/fedora/void/opensuse): \n(Derivatives included)\n").lower()
                if distro == "arch":
                    os.system("sudo touch /usr/flex/arch.cw")
                elif distro == "debian":
                    os.system("sudo touch /usr/flex/deb.cw")
                elif distro == "fedora":
                    os.system("sudo touch /usr/flex/fed.cw")
                elif distro == "void":
                    os.system("sudo touch /usr/flex/void.cw")
                elif distro == "opensuse":
                    os.system("sudo touch /usr/flex/suse.cw")
                else:
                    print("Unknown os. Please enter 'arch', 'debian', 'void', 'opensuse' or 'fedora'.")
                    time.sleep(0.5)
                    os.system("clear")
                    osys()
    else:
        chococ()
        time.sleep(0.5)

def main():
    print(" /$$$$$$$$ /$$                     /$$$$$$$  /$$                \n| $$_____/| $$                    | $$__  $$| $$                \n| $$      | $$  /$$$$$$  /$$   /$$| $$  \\ $$| $$   /$$  /$$$$$$ \n| $$$$$   | $$ /$$__  $$|  $$ /$$/| $$$$$$$/| $$  /$$/ /$$__  $$\n| $$__/   | $$| $$$$$$$$ \\  $$$$/ | $$____/ | $$$$$$/ | $$  \\ $$\n| $$      | $$| $$_____/  >$$  $$ | $$      | $$_  $$ | $$  | $$\n| $$      | $$|  $$$$$$$ /$$/\\  $$| $$      | $$ \\  $$|  $$$$$$$\n|__/      |__/ \\_______/|__/  \\__/|__/      |__/  \\__/ \\____  $$\n                                                       /$$  \\ $$\n                                                      |  $$$$$$/\n                                                       \\______/ ")
    time.sleep(1)
    file_path = "flex.pkg"
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            if first_line == "## FLEXPKG Format Version 1 By VPeti":
                print("Valid FLEXPKG file detected")
                time.sleep(1.5)
                check_pipe_character(file_path)
                osys()
                osr()
                subprocess.call(['python', 'pkg.py'])
                subprocess.call(['python', 'git.py'])
                subprocess.call(['python', 'get.py'])
                subprocess.call(['python', 'shellcmd.py'])
                shell()
            else:
                print("The file isnt a valid FLEXPKG file!")
    except FileNotFoundError:
        print("File flex.pkg not found in current directory!")

if __name__ == "__main__":
    main()
