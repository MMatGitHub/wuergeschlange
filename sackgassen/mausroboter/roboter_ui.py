#!/usr/bin/env python3
import multiprocessing
import time
import subprocess
import sys

def display_time_and_greeting():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"It is exactly {current_time} now. I am alive {__file__}")

def what_do_you_want(question_text):
    while True:
        try:
            print(question_text)
            choice = input("> ")
            return choice.lower()
        except EOFError:
            print("Error reading input. Please try again.")
            return "yes"

