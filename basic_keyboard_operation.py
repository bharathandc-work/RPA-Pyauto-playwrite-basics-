import pyautogui
import time

pyautogui.typewrite("Hello, World!", interval=0.1)  # Type "Hello, World!" with a delay of 0.1 seconds between each character
time.sleep(1)  # Wait for 1 second      

#hot keys
pyautogui.hotkey('ctrl', 'a')  # Press Ctrl + A to select all text