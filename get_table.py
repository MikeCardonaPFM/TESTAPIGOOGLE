import requests
import json
#Librerias para el manejo de la API de AppSheet por Mike
##################################################################################
API_KEY = "V2-b83AN-fOPyT-KbJ3b-7eU06-JwLBC-dDy2a-YsMmL-eJMv5"

##################################################################################
class BotMike():
    def __init__(self, APP_ID, API_KEY, table, data):
        self.APP_ID = APP_ID
        self.API_KEY = API_KEY
        self.data = data
        self.API_URL = f"https://www.appsheet.com/api/v2/apps/{APP_ID}/tables/{table}/"
        
        self.headers = {
            "ApplicationAccessKey": self.API_KEY
        }

    def post_table(self):
        action = "Action"
        url = self.API_URL + action
        response = requests.post(url, json=self.data, headers=self.headers)
        return response.json()
    
    def get_table(self):
        action = "find"
        url = self.API_URL + action
        response = requests.post(url, json=self.data, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error {response.status_code}: {response.text}"
        
mike = BotMike("3fb40a22-9c08-4eff-b5ea-89e74313693b", API_KEY, "WO", {"Action": "find"})
print(mike.get_table())

##########################################################################################