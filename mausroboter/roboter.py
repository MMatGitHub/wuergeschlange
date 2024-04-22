#!/usr/bin/env python3
import multiprocessing
import time
import subprocess
import sys

def check_xdotool():
    try:
        subprocess.run(['xdotool', '--version'], check=True)
        return True
    except FileNotFoundError:
        return False

def move_mouse():
    if check_xdotool():
        while True:
            subprocess.run(['xdotool', 'mousemove', '0', '0'])
            time.sleep(0.1)
            subprocess.run(['xdotool', 'mousemove_relative', '1', '1'])
            time.sleep(0.1)
    else:
        print("xdotool is not installed.")
        install_xdotool = input("Do you want to install xdotool? (yes/no): ")
        if install_xdotool.lower().startswith('y'):
            try:
                subprocess.run(['sudo', 'apt', 'install', 'xdotool'], check=True)
                print("xdotool has been successfully installed.")
            except subprocess.CalledProcessError:
                print("Failed to install xdotool.")
                sys.exit(1)
        else:
            print("You chose not to install xdotool. Exiting.")
            sys.exit(1)

def display_time_and_greeting():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"It is exactly {current_time} now. I am alive {__file__}")

def what_do_you_want(question_text):
    while True:
        try:
            print(question_text)
            sys.stdout.flush()
            choice = input("> ").lower()
            return choice
        except EOFError:
            print("Error reading input. Please try again.")

def main_loop(prompt_frequency):
    while True:
        try:
            choice = what_do_you_want("Do you want to interrupt me? (yes/no)")
        except EOFError as e:
            print (f"e: Runtimefehler {e}")
        if choice.startswith('y'):
            print("You chose to interrupt.")
            break
        elif choice.startswith('n'):
            print("You chose not to interrupt.")
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

        display_time_and_greeting()
        time.sleep(prompt_frequency * 60)

if __name__ == "__main__":
    try:
        prompt_frequency = int(input("How often do you like to be prompted (in minutes)? "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        sys.exit(1)

    process1 = multiprocessing.Process(target=main_loop, args=(prompt_frequency,))
    process2 = multiprocessing.Process(target=move_mouse)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
