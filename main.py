import os
import subprocess
import time


def main():
    print(" /$$$$$$$$ /$$                     /$$$$$$$  /$$                \n| $$_____/| $$                    | $$__  $$| $$                \n| $$      | $$  /$$$$$$  /$$   /$$| $$  \\ $$| $$   /$$  /$$$$$$ \n| $$$$$   | $$ /$$__  $$|  $$ /$$/| $$$$$$$/| $$  /$$/ /$$__  $$\n| $$__/   | $$| $$$$$$$$ \\  $$$$/ | $$____/ | $$$$$$/ | $$  \\ $$\n| $$      | $$| $$_____/  >$$  $$ | $$      | $$_  $$ | $$  | $$\n| $$      | $$|  $$$$$$$ /$$/\\  $$| $$      | $$ \\  $$|  $$$$$$$\n|__/      |__/ \\_______/|__/  \\__/|__/      |__/  \\__/ \\____  $$\n                                                       /$$  \\ $$\n                                                      |  $$$$$$/\n                                                       \\______/ ")
    time.sleep(1)
    file_path = "flex.pkg"

    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            if first_line == "## FLEXPKG Format Version 1 By VPeti":
                print("Valid FLEXPKG file detected")
                time.sleep(2)
                subprocess.call(['python', 'osr.py'])
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
