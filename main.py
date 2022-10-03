import time
import keyboard
from PIL import ImageGrab
import pyautogui

time.sleep(3)

x1 = 680
y1 = 341
x2 = 858
y2 = 380

pyautogui.press('space')
while not keyboard.is_pressed('ctrl'):

    px = ImageGrab.grab(bbox=[x1, y1, x2, y2]).load()
    space = False
    for x in range(x2 - x1):
        for y in range(y2 - y1):
            px_color = px[x, y]
            if px_color[0] == px_color[1] == px_color[2] < 100:
                space = True
                break
        if space:
            break
    if space:
        pyautogui.press('space')
