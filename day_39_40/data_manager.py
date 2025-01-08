import os 
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv("day_39/.env.py")
API_ID= "sGvO5Tejm8j6N74WwqyvoZFr052f8hig"
API_KEY="jAMHFtnlaD5cnfHD"

TOKEN_ENDPOINT= "test.api.amadeus.com/v1/security/oauth2/token"
class DataManager:
    def __init__(self):
        self._user= os.environ["georgelcr@gmail.com"]
        self._password= os.environ[",WVjr@2pp@pRuk$"]
        self._authorization= HTTPBasicAuth(self._user,self._password)
        self.destination_data={}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=TOKEN_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{TOKEN_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
    