import time
import webbrowser

import pyautogui

import pandas as pd

import PIL

from screeninfo import get_monitors

data = pd.read_csv('C:\Python Projects\subscriptions.csv')

url_list = data['Channel URL'].to_list()

if (len(get_monitors()) > 0 and get_monitors()[0].height == 1080 and get_monitors()[0].width == 1920):
    for url in url_list:
        webbrowser.open(url)
        pyautogui.sleep(3)
        if pyautogui.locateOnScreen(r"C:\Users\kapil\Pictures\Screenshot 2022-07-08 182341.png") != None:
            pyautogui.click(pyautogui.locateOnScreen(r"C:\Users\kapil\Pictures\Screenshot 2022-07-08 182341.png"))
        pyautogui.hotkey('ctrl', 'w')

            

       

