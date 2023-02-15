from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pandas as pd

title = ''
url = ""
full_link = """"""

options = FirefoxOptions()
options.add_argument("--width=954")
options.add_argument("--height=483")
driver = Firefox(service=Service(), options=options)
driver.set_window_position(x=955, y=0)
driver.implicitly_wait(20)

driver.get("https://www.reddit.com")
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div/div[1]/a").click()
sleep(2)
driver.switch_to.frame(driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div/iframe"))
driver.find_element(By.ID, "loginUsername").send_keys("real_shit_ong")
driver.find_element(By.ID, "loginPassword").send_keys("braindamage")
sleep(1)
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(5)

# for sub in subs:
#     driver.get(f"https://www.reddit.com/r/{sub}/submit")
#     driver.find_element(
#         By.CSS_SELECTOR, "button.Z1w8VkpQ23E1Wdq_My3U4:nth-child(3)").click()
#     if sub in ["HotDesiSluts", "Desi4you"]:
#         driver.find_element(By.CSS_SELECTOR, "._1ec_Oj5SWdypd8L-VELKg-").send_keys(
#             f"{title.removesuffix('[Link in Comments ⚡]')}[Check Profile 😊]")
#     else:
#         driver.find_element(
#             By.CSS_SELECTOR, "._1ec_Oj5SWdypd8L-VELKg-").send_keys(title)
#     driver.find_element(
#         By.CSS_SELECTOR, "._3zY6b4QJpSz1067ahq73_K").send_keys(url)
#     if subs[sub] is not None:
#         try:
#             flair_button = driver.find_element(
#                 By.CSS_SELECTOR, "._1LD2Xsr3fioSkWZ13vMORC")
#             driver.execute_script(
#                 "arguments[0].scrollIntoView(true);", flair_button)
#             flair_button.click()
#             driver.find_element(
#                 By.CSS_SELECTOR, "._1nQbRaoAvb6Uy0oI-OfDtZ").send_keys(subs[sub]["flair"])
#             driver.find_element(By.CSS_SELECTOR, ".FJIE5E2gciCA8q3Jzvcyg").click()
#             apply_button = driver.find_element(
#                 By.CSS_SELECTOR, ".cF9DU_4WDAKS4gs43ct2_ > button:nth-child(1)")
#             driver.execute_script(
#                 "arguments[0].scrollIntoView(true);", apply_button)
#             apply_button.click()
#         except NoSuchElementException:
#             pass
#     try:
#         post_button = driver.find_element(
#             By.CSS_SELECTOR, "._18Bo5Wuo3tMV-RDB8-kh8Z")
#         driver.execute_script(
#             "arguments[0].scrollIntoView(true);", post_button)
#         sleep(1)
#         post_button.click()
#         if sub not in ["Desi4you", "HotDesiSluts"]:
#             comment_area = driver.find_element(
#                 By.CSS_SELECTOR, "._6Ej82J4aTDK36LLOcpFbC")
#             driver.execute_script(
#                 "arguments[0].scrollIntoView(true);", comment_area)
#             sleep(1)
#             ActionChains(driver).click(
#                 comment_area).send_keys(full_link).perform()
#             driver.find_element(
#                 By.CSS_SELECTOR, "._22S4OsoDdOqiM-hPTeOURa").click()
#         else:
#             sleep(3)
#     except NoSuchElementException:
#         print("Couldn't post to/comment in " + sub)
#         continue
#     sleep(1)






