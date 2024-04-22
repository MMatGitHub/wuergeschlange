import subprocess

script1 = "./foldermonitor.py"
script2 = "./app.py"

p1 = subprocess.Popen(["python", script1])
p2 = subprocess.Popen(["python", script2])

user_input = input("Do you want to stop a process? (y/n): ")
if user_input.lower() == 'y':
    user_choice = int(input("Welcher Prozess soll beendet werden? Enter 1 or 2: "))
    print (f"Ihre Eingabe war: {user_choice}")
    if user_choice == 1:
        p1.terminate()
    elif user_choice == 2:
        p2.terminate()