import smtplib
import time
import requests
import datetime

while True:
    MY_LAT = 31.662127
    MY_LONG = 74.852428
    MY_EMAIL = "clowndetected@gmail.com"
    PASS = "lzlrydtqpvxkugru"

    # MY AREA SUNRISE / SUNSET TIME
    response = requests.get(
        url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
    response.raise_for_status()

    sunrise = int(response.json()["results"]["sunrise"].split("T")[1][:2])
    sunset = int(response.json()["results"]["sunset"].split("T")[1][:2])

    current_time = datetime.datetime.utcnow().hour

    if current_time not in range(sunrise, sunset + 1):
        # ISS COORDS
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASS)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                    msg="Subject:Look up! The iss is overhead!\n\nThe ISS is flying overhead! Go check it out!")
                time.sleep(604800)
                continue
    print("ok")
    time.sleep(60)
