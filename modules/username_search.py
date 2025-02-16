import subprocess
import sys
import os

# ANSI escape sequences for colors

RESET = "\033[0m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
WHITE = "\033[1;37m"


if not os.path.exists("logs/usernames"):
    os.makedirs("logs/usernames")

def search_username(username):

    if username is '':
        print(f"{RED}[-] Inter a username!{RESET}")
        return

    os.environ["TERM"] = "xterm-256color"

    # The command to launch Sherlock
    command = f"sherlock {username} -o logs/usernames/{username}.txt --nsfw"
    
    # Running Sherlock with Popen
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Reading and outputting data in real time
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            # add colors to each data type
            if '[+]' in output:
                
                sys.stdout.write(GREEN + output + RESET)
            elif '[*]' in output:
                
                sys.stdout.write(CYAN + output + RESET)
            elif '[-]' in output:
                
                sys.stdout.write(RED + output + RESET)
            else:
                
                sys.stdout.write(WHITE + output + RESET)

    # Capture errors
    stderr = process.stderr.read()
    if stderr:
        sys.stderr.write(RED + stderr + RESET)

def main():
    print("\033[1;32m╔══ Username Search ══╗\033[0m")
    print("    \033[1;32mUsing\033[0m \033[1;32mSherlock\033[0m")
    print("\033[1;32m╚═════════════════════╝\033[0m\n")
    user = input("\033[1;34mUsername: \033[0m")

    search_username(user)