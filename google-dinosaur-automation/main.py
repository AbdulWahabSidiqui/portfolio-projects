import pyautogui
from PIL import ImageGrab
import time

GAME_AREA = (300, 700,  750, 910)

time.sleep(4)

while True:
    cactus_detected = False
    screenshot = ImageGrab.grab(bbox=GAME_AREA)
    for x in range(0, screenshot.width, 3):
        dark_pixels = 0
        for y in range(0, screenshot.height, 3):

            r, g, b = screenshot.getpixel((x, y))

            if r < 100 and g < 100 and b < 100:
                dark_pixels += 1

        if dark_pixels > 15:
            cactus_detected = True
            break

    if cactus_detected:
        pyautogui.keyDown("space")
        time.sleep(0.1)
        pyautogui.keyUp("space")
        time.sleep(0.05)

    else:
        time.sleep(0.01)