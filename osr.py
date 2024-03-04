import time



def main(os):
    os = int(os)  # Convert os to an integer
    if os == 0:
        pass  # Do nothing
    elif os == 1:
        system_type = input("Do you have Linux or Windows? ").lower()
        if system_type == "windows":
            print("Unsupported FLEXPKG file!")
            time.sleep(1.5)
            quit()
            
        elif system_type == "linux":
            print("Beginning install")
        else:
            print("Invalid input. Please enter 'Linux' or 'Windows'.")
    elif os == 2:
        # Same behavior as when os == 1
        system_type = input("Do you have Linux or Windows? ").lower()
        if system_type == "windows":
            print("Beginning install")
        elif system_type == "linux":
            print("Unsupported FLEXPKG file!")
            time.sleep(1.5)
            quit()
        else:
            pass
    else:
        print("Invalid value for 'os'. Please enter 0, 1, or 2.")

def check_osr_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if "osr = " in line:
                    # Extract the text after "osr = "
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
        print(f"ERROR READING FROM FILE!")

# Usage example:
check_osr_line("flex.pkg")
