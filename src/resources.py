####################################################################################

# Get array from notepad
with open("input.txt", "r") as file:
    data = file.read().split()  # Split on spaces or newlines
    array = [(x) for x in data]
print("Array:", array)

####################################################################################

####################################################################################

import win32api # type: ignore
import win32print # type: ignore
 # Specify the printer
printer_name = win32print.GetDefaultPrinter()
print(f"Default printer: {printer_name}")

# Specify the file to print
file_path = "example.txt"  # Replace with your text file path

# Print the file
win32api.ShellExecute(0, "print", file_path, None, ".", 0)
            
####################################################################################

#######################################################
import pyautogui # type: ignore 
# Get the current position of the mouse
x, y = pyautogui.position()
print(f"Mouse position: ({x}, {y})")

#######################################################

#######################################################

# Get screen size
width, height = pyautogui.size()
print(f"Screen size: {width}x{height}")

#######################################################

#######################################################

# Take a screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

#######################################################