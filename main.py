import os
import pkg_resources
import yandexgpt
import get_screen_image


def install(packages):
    installed_packages = [str(pkg).split(" ")[0] for pkg in pkg_resources.working_set]
    for pkg in packages:
        if (pkg in installed_packages):
            continue
        os.system(f"pip install {pkg}")


packages = ["keyboard", "pynput", "pyscreenshot", "pillow", "opencv-python", "pytesseract"]
install(packages)


import keyboard
import pynput
import tkinter as tk
import pytesseract
import cv2
from PIL import Image


already_pressed = False

mouse = pynput.mouse.Controller()
root = tk.Tk()
root.wait_visibility(root)
root.wm_attributes("-fullscreen", 1)
root.attributes("-topmost", True)
root.wm_attributes("-transparentcolor", root['bg'])
frame = tk.Frame(root)
frame.pack()
canvas = tk.Canvas(frame, width=root.winfo_width(), height=root.winfo_height())
canvas.pack()

while (True):
    point1 = (0, 0)
    point2 = (0, 0)
    while (True):
        canvas.create_rectangle(point1[0], point1[1], point2[0], point2[1], outline="red")
        canvas.update()
        root.update()
        canvas.delete("all")
        if (keyboard.is_pressed("g") and keyboard.is_pressed("alt")):
            if (already_pressed == False):
                point1 = mouse.position
                already_pressed = True
            else:
                point2 = mouse.position
        elif (already_pressed == True):
            point2 = mouse.position
            already_pressed = False
            break
    canvas.delete("all")
    canvas.update()
    root.update()
    point1 = (int(point1[0] * 1920 / 1535), int(point1[1] * 1080 / 863))
    point2 = (int(point2[0] * 1920 / 1535), int(point2[1] * 1080 / 863))

    image = get_screen_image.get_image(point1, point2)
    config = ('-l rus+eng --oem 1 --psm 3')
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Student\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(image, lang="rus+eng")
    response = yandexgpt.get_answer(text)
    