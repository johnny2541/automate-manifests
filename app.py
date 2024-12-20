# Pip module
import pyautogui 
import pyperclip 
import time

# Project Module
from src.constants import *

def reciveLX():
    # Get array from notepad
    with open("docs/input.txt", "r") as file:
        data = file.read().split()  # Split on spaces or newlines
    return data

def locate_to_action(image_path, confidence=0.8, sleep_time=TIMESLEEP_ZEROPOINTTWO):
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        except pyautogui.ImageNotFoundException:
            time.sleep(TIMESLEEP_ZEROPOINTFIVE)
        else:
            time.sleep(sleep_time)
            return x, y

def paste_item(item):
    pyperclip.copy(item)
    pyautogui.keyDown("ctrl")
    pyautogui.press("a")
    pyautogui.keyUp("ctrl")
    pyautogui.press("backspace")
    pyautogui.keyDown("ctrl")
    pyautogui.press("v")
    pyautogui.keyUp("ctrl")
    pyautogui.press("enter")

def close_tab():
    pyautogui.press("enter")
    pyautogui.keyDown("ctrl")
    pyautogui.press("w")
    pyautogui.keyUp("ctrl")

def print_status(item, status):
    print(f"{bcolors.OKBLUE}{item} {bcolors.OKCYAN} is {status}")


def main():
    data = reciveLX()

    for item in data:
        print_status(item, f"{bcolors.WARNING}checking...")
        time.sleep(TIMESLEEP_ZEROPOINTTWO)

        locate_to_action("assets/pack_button.PNG")
        paste_item(item)
        
        locate_to_action("assets/print_button.PNG", sleep_time=TIMESLEEP_ONESECOND)
        close_tab()

        print_status(item, f"{bcolors.OKGREEN}completed!!!")

if __name__ == "__main__":
    main()



