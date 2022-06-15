import pyautogui
from time import sleep
from random import randint
x = 5
def name():
    namelist = ["hi", "hey", "hello", "hmm", "by"]
    rand_name = namelist[randint(0, len(namelist) - 1)]
    return rand_name
while True:
    pyautogui.typewrite(f"I am trying to say {name()}.")
    sleep(.600)
    pyautogui.typewrite("\n")
    sleep(2)
    x = x - 1
    if x == 0:
        break