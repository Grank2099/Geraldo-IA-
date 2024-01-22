version = "1.0"
creator = "Fox2099"
date = "10/01/2024"

import pyautogui
import time
from automate_module import simulate_keyboard_input

def make_call():
    print("")

def simulate_touch(x, y):
    pyautogui.click(x, y)

# Simulate touch at coordinates (100, 200)
time.sleep(2)
simulate_touch(400, 600)

