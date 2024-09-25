import requests
import time

DIGI_API_URL = "https://digi-api.com/api/v1/digimon/"
SAVE_API_URL = "https://localhost:7010/api/Digimon/digimon/save"

def fetch_digimon_data(digimon_id):
    try:
        response = requests.get(f"{DIGI_API_URL}{digimon_id}")
        if response.status_code == 200:
            data = response.json()
            data_dict = {
                "id": 0,
                "code": data["id"],
                "name": data["name"],
                "image": data["images"][0]['href'],
                "type": data["types"][0]['type']
            }

            return data_dict
        else:
            print(f"Failed to fetch Digimon {digimon_id}. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching Digimon {digimon_id} : {e}")
        return None

def save_digimon_to_db(digimon_data):
    try:
        response = requests.post(SAVE_API_URL, json=digimon_data)
    
        if response.status_code == 200:
            print(f"Successfully saved Digimon: {digimon_data['name']}")
        else:
            print(f"Failed to save Digimon. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error saving Digimon: {e}")