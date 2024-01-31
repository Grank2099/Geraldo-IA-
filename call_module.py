version = "1.1"
creator = "Fox2099"
date = "23/01/2024"

import pyautogui
import time
from automate_module import simulate_keyboard_input, open_app

def simulate_touch(x, y):
    pyautogui.click(x, y)

def make_call(nome):
    #Abrir aplicativo do telefone
    open_app("com.samsung.android.dialer")
    time.sleep(2)
    #Simular toque na barra de pesquisa
    simulate_touch(897, 207)
    time.sleep(1)
    #Escrever o nome requisitado
    simulate_keyboard_input(nome)
    #Clicar nele (O primeiro da lista, ou seja, quem o nome for mais próximo)
    simulate_touch(430, 500)
    #Clicar em ligar
    simulate_touch(230, 770)
    