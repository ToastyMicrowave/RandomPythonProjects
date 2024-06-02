from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5

while True:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    if time.time() > timeout:
        shop = driver.find_element(By.ID, "store")
        items = reversed([item for item in shop.find_elements(By.XPATH, "./*")][:-1])
        for item in items:
            if item.get_attribute("class") != "grayed":
                item.click()
                print("bought")
                break
        timeout = time.time() + 5

