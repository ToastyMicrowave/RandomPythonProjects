from turtle import pos
import requests
import os
import datetime
from dotenv import load_dotenv
load_dotenv()

NUTRITIONX_APP_ID = os.getenv("NUTRITIONX_APP_ID")
NUTRITIONX_API_KEY = os.getenv("NUTRITIONX_API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")


auth_header = {"x-app-id": NUTRITIONX_APP_ID, "x-app-key": NUTRITIONX_API_KEY}
activity_params = {"query": input(
    "What did you do? "), "gender": "male", "weight_kg": 77, "age": 16}
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         headers=auth_header, json=activity_params)
activities = response.json()["exercises"]

today = datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

for activity in activities:
    headers = {"Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"}
    body = {
        "workout": {
            "date": today,
            "time": current_time,
            "exercise": activity["name"],
            "duration": activity["duration_min"],
            "calories": activity["nf_calories"],
        }
    }
    post_row = requests.post(
        url=SHEETY_ENDPOINT, headers=headers, json=body)
    print(post_row.text)