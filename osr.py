import time
import platform
import sys
import os

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "linux"
    else:
        return "windows"


def fail():
    print("Unsupported FLEXPKG file for this os!")
    time.sleep(0.5)
    sys.exit(1)

def main(osreturn):
    osreturn = int(osreturn)  # Convert osreturn to an integer
    if osreturn == 0:
        pass
    elif osreturn == 1:
        system_type = detect_os()
        if system_type == "windows":
            fail()
            
        else:
            sys.exit(0)

    elif osreturn == 7:
        system_type = detect_os()
        if system_type == "windows":
            sys.exit(0)
        else:
            fail()

    elif osreturn == 2:
        system_type = detect_os()
        if system_type == "windows":
            fail()
            
        else:
            if os.path.isfile('/usr/flex/arch.cw'):
                sys.exit(0)
            elif os.path.isfile('/usr/flex/deb.cw'):
                fail()
            elif os.path.isfile('/usr/flex/fed.cw'):
                fail()
            elif os.path.isfile('/usr/flex/suse.cw'):
                fail()
            elif os.path.isfile('/usr/flex/void.cw'):
                fail()
            else:
                print("Failed to run OSR funtion!")
                time.sleep(0.5)
                sys.exit(1)
    elif osreturn == 3:
        system_type = detect_os()
        if system_type == "windows":
            fail()
            
        else:
            if os.path.isfile('/usr/flex/arch.cw'):
                fail()
            elif os.path.isfile('/usr/flex/deb.cw'):
                sys.exit(0)
            elif os.path.isfile('/usr/flex/fed.cw'):
                fail()
            elif os.path.isfile('/usr/flex/suse.cw'):
                fail()
            elif os.path.isfile('/usr/flex/void.cw'):
                fail()
            else:
                print("Failed to run OSR funtion!")
                time.sleep(0.5)
                sys.exit(1)
    elif osreturn == 4:
        system_type = detect_os()
        if system_type == "windows":
            fail()
            
        else:
            if os.path.isfile('/usr/flex/arch.cw'):
                fail()
            elif os.path.isfile('/usr/flex/deb.cw'):
                fail()
            elif os.path.isfile('/usr/flex/fed.cw'):
                sys.exit(0)
            elif os.path.isfile('/usr/flex/suse.cw'):
                fail()
            elif os.path.isfile('/usr/flex/void.cw'):
                fail()
            else:
                print("Failed to run OSR funtion!")
                time.sleep(0.5)
                sys.exit(1)
    elif osreturn == 5:
        system_type = detect_os()
        if system_type == "windows":
            fail()
            
        else:
            if os.path.isfile('/usr/flex/arch.cw'):
                fail()
            elif os.path.isfile('/usr/flex/deb.cw'):
                fail()
            elif os.path.isfile('/usr/flex/fed.cw'):
                fail()
            elif os.path.isfile('/usr/flex/suse.cw'):
                fail()
            elif os.path.isfile('/usr/flex/void.cw'):
                sys.exit(0)
            else:
                print("Failed to run OSR funtion!")
                time.sleep(0.5)
                sys.exit(1)
    elif osreturn == 6:
        system_type = detect_os()
        if system_type == "windows":
            fail()
            
        else:
            if os.path.isfile('/usr/flex/arch.cw'):
                fail()
            elif os.path.isfile('/usr/flex/deb.cw'):
                fail()
            elif os.path.isfile('/usr/flex/fed.cw'):
                fail()
            elif os.path.isfile('/usr/flex/suse.cw'):
                sys.exit(0)
            elif os.path.isfile('/usr/flex/void.cw'):
                fail()
            else:
                print("Failed to run OSR funtion!")
                time.sleep(0.5)
                sys.exit(1)
    else:
        print("Failed to run OSR funtion!")
        time.sleep(0.5)
        sys.exit(1)

def check_osr_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if "osr = " in line:
                    # Extract the text after "osr = "
                    text_after_osr = line.split("osr = ")[1].strip()
                    if text_after_osr == "lin":
                        os = "1"
                    elif text_after_osr == "linarch":
                        os = "2"
                    elif text_after_osr == "lindeb":
                        os = "3"
                    elif text_after_osr == "linfed":
                        os = "4"
                    elif text_after_osr == "linvoid":
                        os = "5"
                    elif text_after_osr == "linsuse":
                        os = "6"
                    else:
                        os = "7"
                    break  # Stop searching after finding the first matching line
            else:
                # If no matching line is found
                os = "0"
            main(os)
    except FileNotFoundError:
        pass

check_osr_line("flex.pkg")