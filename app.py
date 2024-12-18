# Pip module
import pyscreeze
import pyautogui 
import pyperclip 
import time
import keyboard

# Project Module
from src.constants import *

#######################################################


#######################################################

#######################################################
def reciveLX():
    # Get array from notepad
    with open("docs/input.txt","r") as file:
     data = file.read().split() # Split on spaces or newlines
     return data


#######################################################


#######################################################

data = reciveLX()

for item in data :
    print(f"{bcolors.OKBLUE}{item}  {bcolors.OKCYAN}is {bcolors.WARNING}checking...")
    time.sleep(TIMESLEEP_ZEROPOINTTWO)



#######################################################
for item in data:

    #######################################################################################
    while True:
        try:
             x, y = pyautogui.locateCenterOnScreen("assets/pack_button.PNG",  confidence=0.8)
        except pyautogui.ImageNotFoundException:
            time.sleep(TIMESLEEP_ZEROPOINTFIVE)
        else:
            time.sleep(TIMESLEEP_ZEROPOINTTWO)

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

    #################################################################################
    while True:
        try:
             x, y = pyautogui.locateCenterOnScreen("assets/print_button.PNG",  confidence=0.8)
        except pyautogui.ImageNotFoundException:
            time.sleep(TIMESLEEP_ZEROPOINTFIVE)
        else:
            time.sleep(TIMESLEEP_ONESECOND)
            pyautogui.press("enter")
            pyautogui.keyDown("ctrl")
            pyautogui.press("w")
            pyautogui.keyUp("ctrl")
            break
#######################################################################################

    print(f"{bcolors.OKBLUE}{item}  is {bcolors.OKGREEN}completed")

#######################################################################################



