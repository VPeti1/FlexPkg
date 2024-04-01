import subprocess
import time
import platform

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

def osr():
    
    try:
        result = subprocess.run(['python', 'osr.py'], check=True)
        if result.returncode == 10:
            pass
        else:
            pass
    except subprocess.CalledProcessError as e:
        quit()

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
                chococ()
                time.sleep(0.5)
                osr()
                subprocess.call(['python', 'pkg.py'])
                subprocess.call(['python', 'git.py'])
                subprocess.call(['python', 'get.py'])
                subprocess.call(['python', 'flat.py'])
                subprocess.call(['python', 'cmd.py'])
                subprocess.call(['python', 'batch.py'])
            else:
                print("The file isnt a valid FLEXPKG file!")
    except FileNotFoundError:
        print("File flex.pkg not found in current directory!")

if __name__ == "__main__":
    main()
