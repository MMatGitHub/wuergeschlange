#!/usr/bin/env python3
import multiprocessing
import time
from roboter_ui import what_do_you_want
from roboter_ui import display_time_and_greeting
from roboter import move_mouse
#import subprocess
import sys


def main_loop(prompt_frequency, stop_event):
    while not stop_event.is_set():
        try:
            choice = what_do_you_want("Do you want to interrupt me? (yes/no)")
        except EOFError as e:
            print (f"e: Runtimefehler {e}")
        if choice.startswith('y'):
            print("You chose to interrupt.")
            stop_event.set()
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

    stop_event = multiprocessing.Event()

    process1 = multiprocessing.Process(target=main_loop, args=(prompt_frequency, stop_event))
    process2 = multiprocessing.Process(target=move_mouse, args=(stop_event,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()