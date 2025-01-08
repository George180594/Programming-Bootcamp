import requests
from datetime import datetime

MY_LAT= -15.826691
MY_LONG= -47.921822


parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data= response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]




time_now=datetime.now()