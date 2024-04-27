import sys
import subprocess
import os
def check_ping():
    try:
        subprocess.run(['ping', 'www.google.com'], check=True)
        return True
    except FileNotFoundError:
        inetutils_ping='inetutils-ping.'
        print("ping is not installed.")
        antwort = input(f"q: Do you want to install {inetutils_ping}? (yes/no): ")
        if antwort.lower().startswith('y'):
            try:
                print(f"i: installing {inetutils_ping}...")
                os.system('sudo apt install inetutils-ping')
            except subprocess.CalledProcessError:
                print(f"Failed to install {inetutils_ping}.")
                sys.exit(1)
        else:
            print(f"You chose not to install {inetutils_ping}. Exiting.")
            sys.exit(1)


if __name__ == "__main__":
    check_ping()