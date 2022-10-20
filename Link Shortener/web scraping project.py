from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


oldreddit_links = ["https://old.reddit.com/user/palakkadan/m/indiannsfw/"]

driver = webdriver.Firefox(
    executable_path=r"C:\Users\kapil\Downloads\geckodriver.exe")

final_all_sub_list = []

for link in oldreddit_links:
    driver.implicitly_wait(5)
    driver.get(link)
    try:
        # Clicks continue button on the "are you over 18" screen
        driver.find_element(
            By.XPATH, "//button[@name='over18'][@value='yes']").click()
    except:
        pass
    soup = BeautifulSoup(driver.page_source, "html.parser")
    list_of_all_subs_in_website = soup.select(".subreddits > li")
    for sub in list_of_all_subs_in_website:
        print(sub.find('a').string.removeprefix("/r/"))

"""
<li><a href="/r/a:t5_2t593">/r/a:t5_2t593</a><button class="remove-sr">x</button></li>,
<li><a href="/r/AnushkaSharma">/r/AnushkaSharma</a><button class="remove-sr">x</button></li>
"""

# sorted_final_sub_list = sorted(list(set(final_all_sub_list)))
# with open("C:\Python Projects\lulw.txt", "w") as all_subs_file:
#     for subname in sorted_final_sub_list:
#         all_subs_file.writelines(subname + "\n")
