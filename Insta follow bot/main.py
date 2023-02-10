import dotenv, os, time
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

dotenv.load_dotenv()

INSTA_USER = os.getenv("INSTA_USER")
INSTA_PASS = os.getenv("INSTA_PASS")
TARGET_USER = "cristiano"

class InstaFollower:
    def __init__(self) -> None:
        options = FirefoxOptions()
        options.add_argument("--width=954")
        options.add_argument("--height=483")
        self.driver = Firefox(service=Service(), options=options)
        self.driver.set_window_position(x=955, y=0)
        self.driver.implicitly_wait(20)
        
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/login/")
        driver.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)").send_keys(INSTA_USER)
        driver.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)").send_keys(INSTA_PASS)
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(5)

    def find_followers(self):
        driver = self.driver
        driver.get(f"https://www.instagram.com/{TARGET_USER}")
        driver.find_element(By.CSS_SELECTOR, "li.xl565be:nth-child(2) > a:nth-child(1) > div:nth-child(1)").click()
        time.sleep(3)
        self.followers = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div")
        
    def follow(self):
        for follower in self.followers:
            if follower.is_displayed():
                follower.find_element(By.XPATH, "./div[3]/button/div/div").click()
            else:
                print(follower.text)
            time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()