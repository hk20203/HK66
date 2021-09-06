# -*- coding: utf8 -*-
import pyautogui
from pyautogui import position
from pyautogui import moveTo
import time

print('''                                             HK出品
''')
m=input('鼠标到查询位置并键入任意按键定位坐标')
currentMouseX4, currentMouseY4 = position()
print(currentMouseX4, currentMouseY4)
n=input('鼠标到选课位置并键入任意按键定位坐标')
currentMouseX5, currentMouseY5 = position()
print(currentMouseX5, currentMouseY5)
v=input('鼠标到确定位置并键入任意按键定位坐标')
currentMouseX6, currentMouseY6 = position()
print(currentMouseX6, currentMouseY6)


q=input('键入任意键开始')
moveTo (currentMouseX6, currentMouseY6, duration=0.1)
while True:

    currentMouseX, currentMouseY = position()
    u=currentMouseX

    pyautogui.click (x=currentMouseX4, y=currentMouseY4, clicks=1, button='left')
    pyautogui.click(currentMouseX, currentMouseY)
    time.sleep(0.3)

    pyautogui.click(x=currentMouseX5, y=currentMouseY5, clicks=1, button='left')
    pyautogui.click(currentMouseX, currentMouseY)
    time.sleep(0.18)

    pyautogui.click(x=currentMouseX6, y=currentMouseY6, clicks=1, button='left')
    pyautogui.click(currentMouseX, currentMouseY)
    time.sleep(0.1)
    currentMouseX1, currentMouseY1 = position()
    o = currentMouseX1
    if o!=u:
        exit()
