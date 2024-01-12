version = "1.0"
creator = "Fox2099"
date = "11/01/2024"

from evdev import uinput, ecodes
import time
import pyautogui
import subprocess

def open_app(package_name):
    try:
        # Construct the adb command to start the app
        adb_command = f'am start -n {package_name}/.{package_name}.MainActivity'

        # Execute the adb command
        subprocess.run(adb_command, shell=True, check=True)

        print(f"App {package_name} opened successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example package name (replace with the actual package name of the app you want to open)
    app_package_name = "com.example.myapp"

    # Open the specified app
    open_app(app_package_name)

#897 207.3 posição do botão de pesquisa

def simulate_touch(x, y):
    pyautogui.click(x, y)
    


def simulate_keyboard_input(input_text):
    # Mapping of characters to evdev key codes
    char_to_key = {
        'a': ecodes.KEY_A,
        'b': ecodes.KEY_B,
        'c': ecodes.KEY_C,
        'd': ecodes.KEY_D,
        'e': ecodes.KEY_E,
        'f': ecodes.KEY_F,
        'g': ecodes.KEY_G,
        'h': ecodes.KEY_H,
        'i': ecodes.KEY_I,
        'j': ecodes.KEY_J,
        'k': ecodes.KEY_K,
        'l': ecodes.KEY_L,
        'm': ecodes.KEY_M,
        'n': ecodes.KEY_N,
        'o': ecodes.KEY_O,
        'p': ecodes.KEY_P,
        'q': ecodes.KEY_Q,
        'r': ecodes.KEY_R,
        's': ecodes.KEY_S,
        't': ecodes.KEY_T,
        'u': ecodes.KEY_U,
        'v': ecodes.KEY_V,
        'w': ecodes.KEY_W,
        'x': ecodes.KEY_X,
        'y': ecodes.KEY_Y,
        'z': ecodes.KEY_Z,
        '0': ecodes.KEY_0,
        '1': ecodes.KEY_1,
        '2': ecodes.KEY_2,
        '3': ecodes.KEY_3,
        '4': ecodes.KEY_4,
        '5': ecodes.KEY_5,
        '6': ecodes.KEY_6,
        '7': ecodes.KEY_7,
        '8': ecodes.KEY_8,
        '9': ecodes.KEY_9,
        
        
        # Add more mappings as needed
    }

    with uinput.UInput() as ui:
        for char in input_text.lower():
            if char in char_to_key:
                ui.write(ecodes.EV_KEY, char_to_key[char], 1)
                ui.syn()
                time.sleep(0.1)
                ui.write(ecodes.EV_KEY, char_to_key[char], 0)
                ui.syn()
                time.sleep(0.1)

        # Press Enter key
        ui.write(ecodes.EV_KEY, ecodes.KEY_ENTER, 1)
        ui.syn()
        time.sleep(0.1)
        ui.write(ecodes.EV_KEY, ecodes.KEY_ENTER, 0)
        ui.syn()
