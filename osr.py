import time
import platform
import sys

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "linux"
    else:
        return "windows"


def main(os):
    os = int(os)  # Convert os to an integer
    if os == 0:
        pass
    elif os == 1:
        system_type = detect_os()
        if system_type == "windows":
            print("Unsupported FLEXPKG file for this os!")
            time.sleep(1.5)
            sys.exit(1)
            
        elif system_type == "linux":
            sys.exit(0)

        else:
            pass
    elif os == 2:
        system_type = detect_os()
        if system_type == "windows":
            sys.exit(0)
        elif system_type == "linux":
            print("Unsupported FLEXPKG file for this os!")
            time.sleep(1.5)
            sys.exit(1)
        else:
            pass
    else:
        pass

def check_osr_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if "osr = " in line:
                    # Extract the text after "osr = "gn
                    text_after_osr = line.split("osr = ")[1].strip()
                    if text_after_osr == "lin":
                        os = "1"
                    else:
                        os = "2"
                    break  # Stop searching after finding the first matching line
            else:
                # If no matching line is found
                os = "0"
            a = os
            main(a)
    except FileNotFoundError:
        pass


check_osr_line("flex.pkg")
