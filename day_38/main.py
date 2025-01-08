import requests
from datetime import datetime
X_APP="4cb382d4"
X_APP_KEY="a385dca6f968ce27fc416eb6f941cc96"



QUERY= input("Choose your exercise: ") 
# QUERY= "swam for 1 hour"
WEIGHT= 79
HEIGHT=170
AGE=30
GENDER="male"



url="https://trackapi.nutritionix.com/v2/natural/exercise"

headers= {
    'x-app-id': X_APP,
    'x-app-key':X_APP_KEY,
}


paramameters={
    "query": QUERY ,
    "gender": GENDER,
    "weight_kg":WEIGHT ,
    "height_cm":HEIGHT ,
    "age":AGE ,
}
response= requests.post(url=url, json=paramameters,headers=headers)
result=response.json()

############################################################################
USER_NAME="GeorgeLucas"
USER_EMAIL="georgelcr@gmail.com"
email={
    "name": USER_NAME,
    "email":USER_EMAIL,
}
URL_SHEETY=f"https://api.sheety.co/phill/myWebsite/{email}"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(URL_SHEETY, json=sheet_inputs)

    print(sheet_response.text)