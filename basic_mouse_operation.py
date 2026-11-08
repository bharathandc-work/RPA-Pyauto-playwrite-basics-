import pyautogui
import time

# Move the mouse to a specific position
pyautogui.moveTo(100, 100, duration=1)  # Move to (100, 100) over 1 second
time.sleep(1)  # Wait   

# Click the mouse at the current position
pyautogui.click()  # Perform a left click
time.sleep(1) 

pyautogui.doubleClick()  # Perform a double click
time.sleep(1) 

pyautogui.rightClick()  # Perform a right click
