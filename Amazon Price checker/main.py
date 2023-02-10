from bs4 import BeautifulSoup
import requests
import smtplib
import dotenv
import os

dotenv.load_dotenv()

URL = "https://www.amazon.in/OnePlus-Nord-Bahamas-128GB-Storage/dp/B09RG5R5FG/ref=pd_bxgy_sccl_1/258-8889444-8905105?pd_rd_w=ovXCa&content-id=amzn1.sym.d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_p=d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_r=SE09XJP7REN5D6T3ZAPN&pd_rd_wg=0G7E5&pd_rd_r=16e21aee-0390-49b5-8f08-139e73111e2f&pd_rd_i=B09RG5R5FG&psc=1"
MIN_PRICE = 20000
USER_EMAIL = os.getenv("EMAIL")
USER_PASS = os.getenv("PASSWORD")

headers = {
    "Accept-Language": "en-US, en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Host": "www.amazon.in",
    "Accept": "image/avif,image/webp,*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.amazon.in/OnePlus-Nord-Bahamas-128GB-Storage/dp/B09RG5R5FG/ref=pd_bxgy_sccl_1/258-8889444-8905105?pd_rd_w=ovXCa&content-id=amzn1.sym.d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_p=d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_r=SE09XJP7REN5D6T3ZAPN&pd_rd_wg=0G7E5&pd_rd_r=16e21aee-0390-49b5-8f08-139e73111e2f&pd_rd_i=B09RG5R5FG&psc=1",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
}

bypassed_captcha = False
while not bypassed_captcha:
    response = requests.get(url=URL)
    soup = BeautifulSoup(response.text, "lxml")
    if soup.prettify().split("price")[0].strip().endswith("to") or soup.prettify().split("price")[0].strip().endswith("</html>"):
        continue
    bypassed_captcha = True

price = int(
    soup.find(class_="a-price-whole").text.removesuffix(".").replace(",", ""))
title = soup.find(id="productTitle").text.strip()

if price >= MIN_PRICE:
    message = f"Subject: Price drop on the product you were interested in!\n\n{title} is now ₹{price}. Buy at {URL}".encode("utf-8")
    
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=USER_PASS)
        connection.sendmail(from_addr=USER_EMAIL, to_addrs=USER_EMAIL, msg=message)