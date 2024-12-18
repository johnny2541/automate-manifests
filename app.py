import pyscreeze
import pyautogui 
import pyperclip 
import time
import keyboard

#######################################################
TIMESLEEP = 1

#######################################################

#######################################################

# Get array from notepad
with open("docs/input.txt", "r") as file:
    data = file.read().split()  # Split on spaces or newlines
    array = [(x) for x in data]

for item in data :
    print(f"{item}   check ???")
    time.sleep(0.2)

#######################################################

for item in data:

    #######################################################################################
    while True:
        try:
             x, y = pyautogui.locateCenterOnScreen("assets/pack_button.PNG",  confidence=0.8)
        except pyautogui.ImageNotFoundException:
            time.sleep(0.5)
        else:
            time.sleep(0.2)

            # Copy the current item to the clipboard
            pyperclip.copy(item)
            
            # Simulate Ctrl + a to select all and simulate blackspace to clear area
            pyautogui.keyDown("ctrl")
            pyautogui.press("a")
            pyautogui.keyUp("ctrl")
            pyautogui.press("backspace")

            # Simulate Ctrl + V to paste
            pyautogui.keyDown("ctrl")
            pyautogui.press("v")
            pyautogui.keyUp("ctrl")
            
            # Press Enter after pasting (optional, e.g., to move to the next line)
            pyautogui.press("enter")
            break
    #################################################################################
    state = 0
    #################################################################################
    while True:
        time.sleep(0.5)
        try:
             x, y = pyautogui.locateCenterOnScreen("assets/red_text.PNG",  confidence=0.8)
        except pyautogui.ImageNotFoundException:
            break
        else:
            state = 1
            break
            
    #################################################################################
    if state == 1:
        continue

    #################################################################################

    #################################################################################
    while True:
        try:
             x, y = pyautogui.locateCenterOnScreen("assets/print_button.PNG",  confidence=0.8)
        except pyautogui.ImageNotFoundException:
            time.sleep(0.5)
        else:
            time.sleep(1)
            pyautogui.press("enter")
            pyautogui.keyDown("ctrl")
            pyautogui.press("w")
            pyautogui.keyUp("ctrl")
            break
#######################################################################################

    print(f"{item}       complete!!!")

#######################################################################################
print("All LX Complete!!!!!")



