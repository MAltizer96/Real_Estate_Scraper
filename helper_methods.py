import helper_methods

import pyautogui
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
from random import random
from random import randint

def get_short_random_delay():
    return 1 + (2 * random())

def get_long_random_delay():
    return 10 + (5 * random())

def wait_time(seconds):
    sleep(seconds)

def click_and_hold(hold_duration):
    pyautogui.mouseDown()
    wait_time(hold_duration)
    pyautogui.mouseUp()
    print(f"Clicked and held for {hold_duration:.2f} seconds.")
    random_number = randint(0, 500)
    randomX = random_number + (100 * random())
    randomY = random_number + (100 * random())

    move_mouse_to_coordinates(randomX, randomY)

def move_mouse_to_element(element=None, y_offset=0):
    print("Moving mouse to element...")
    location = element.location
    size = element.size


    center_x = location['x'] + size['width'] // 2
    center_y = location['y'] + size['height'] // 2 + y_offset

    pyautogui.moveTo(center_x, center_y, duration=1)

def move_mouse_to_coordinates(x, y):
    print(f"Moving mouse to coordinates: ({x}, {y})")
    pyautogui.moveTo(x, y, duration=1)

def click_element():
    pyautogui.click()
def double_click_element():
    pyautogui.doubleClick()