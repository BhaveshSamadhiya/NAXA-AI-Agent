import os
import time
import subprocess
import psutil
import pyautogui
from datetime import datetime

def write_log(message):
    with open("service_log.txt", "a") as file:
        file.write(f"{datetime.now()} - {message}\n")

print("Watchdog Service Started...")
write_log("Service Started")

with open("timer.txt", "r") as file:
    saved_time = file.read()

target_time = datetime.fromisoformat(saved_time)

current_time = datetime.now()

remaining = target_time - current_time

seconds = remaining.total_seconds()

print("Remaining Seconds =", seconds)

if seconds > 0:
    time.sleep(seconds)

print("TIMER COMPLETED")
print("OPENING GOOGLE")
write_log("Opening Google")

print("OPENING VSCODE")
write_log("Opening VS Code")
print("OPENING WHATSAPP")
write_log("opening whatsapp")
PROJECT_PATH = r"C:\Users\Bhavesh samadhiya\OneDrive\Desktop\hellopython"
def is_running(process_name):
    for process in psutil.process_iter():
        try:
            if process.name().lower() == process_name.lower():
                return True
        except:
            pass
    return False
    

os.system("start https://www.google.com")

os.system(
    f'start "" "C:\\Users\\Bhavesh samadhiya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" "{PROJECT_PATH}"'
)
os.system("start https://web.whatsapp.com")
print("VSCODE COMMAND FINISHED")
 

time.sleep(8)

print("OPENING TERMINAL")
pyautogui.hotkey("ctrl", "`")

time.sleep(2)

print("RUNNING TEST.PY")
pyautogui.write("python test.py", interval=0.05)
pyautogui.press("enter")
subprocess.Popen(
    f'start cmd /k python "{PROJECT_PATH}\\test.py"',
    shell=True
)
while True:

    print("LOOP RUNNING")
    print("Code Running Check =", is_running("Code.exe"))

    if not is_running("Code.exe"):
        print("INSIDE IF")

        try:
            subprocess.Popen([
                r"C:\Users\Bhavesh samadhiya\AppData\Local\Programs\Microsoft VS Code\Code.exe",
                PROJECT_PATH
            ])

            print("OPEN COMMAND EXECUTED")
            write_log("VS Code Opened")
            time.sleep(5)        
            
            pyautogui.hotkey("ctrl", "`")         
            time.sleep(2)
            pyautogui.write("python test.py", interval=0.05)
            pyautogui.press("enter")
            print("VS Code Reopened")
            write_log("VS Code Reopened")
        except Exception as e:
           print("ERROR =", e)
           write_log(f"ERROR: {e}")

    time.sleep(10)