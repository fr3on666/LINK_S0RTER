import sys
import time
import pyshorteners
import getpass

def animated(text):
    """Print text with a typing animation effect."""
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)

def end():
    """Exit the program after user input."""
    input("Press Enter to exit...")
    sys.exit()

def authenticate():
    """Authenticate user with username and password."""
    username = "R3D.DEV"
    password = "SUDO SU"

    given_username = input(f"{RED}Enter your username: {RESET}")
    if given_username == username:
        given_password = getpass.getpass(f"{RED}Enter password: {RESET}")
        if given_password == password:
            return True
        else:
            print(f"{RED}Wrong password{RESET}")
    else:
        print(f"{RED}Wrong username{RESET}")
    return False

def display_logo():
    """Display the logo with animation."""
    logo = '''
 /$$       /$$$$$$ /$$   /$$ /$$   /$$        /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$       
| $$      |_  $$_/| $$$ | $$| $$  /$$/       /$$__  $$| $$  | $$ /$$__  $$| $$__  $$|__  $$__/| $$_____/| $$__  $$      
| $$        | $$  | $$$$| $$| $$ /$$/       | $$  \__/| $$  | $$| $$  \ $$| $$  \ $$   | $$   | $$      | $$  \ $$      
| $$        | $$  | $$ $$ $$| $$$$$/        |  $$$$$$ | $$$$$$$$| $$  | $$| $$$$$$$/   | $$   | $$$$$   | $$$$$$$/      
| $$        | $$  | $$  $$$$| $$  $$         \____  $$| $$__  $$| $$  | $$| $$__  $$   | $$   | $$__/   | $$__  $$      
| $$        | $$  | $$\  $$$| $$\  $$        /$$  \ $$| $$  | $$| $$  | $$| $$  \ $$   | $$   | $$      | $$  \ $$      
| $$$$$$$$ /$$$$$$| $$ \  $$| $$ \  $$      |  $$$$$$/| $$  | $$|  $$$$$$/| $$  | $$   | $$   | $$$$$$$$| $$  | $$      
|________/|______/|__/  \__/|__/  \__/       \______/ |__/  |__/ \______/ |__/  |__/   |__/   |________/|__/  |__/  by R3D
                                        
    '''
    animated(logo)

def shorten_link():
    """Shorten a URL using pyshorteners."""
    link = input("Enter your link here:  ")
    s = pyshorteners.Shortener()
    try:
        short_link = s.tinyurl.short(link)
        print(f"Your short link is: {short_link}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the program."""
    if authenticate():
        print("Welcome TO LINK SHORTER")
        display_logo()
        shorten_link()
    else:
        time.sleep(1)
        print("Press Enter to exit")
        end()

# ANSI color codes
RED = "\033[31m"
RESET = "\033[0m"

if __name__ == "__main__":
    main()


