import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DIGI_API_URL = "https://digi-api.com/api/v1/digimon/"
SAVE_API_URL = "https://localhost:7010/api/Digimon/digimon/save"

def fetch_digimon_data(digimon_id):
    try:
        response = requests.get(f"{DIGI_API_URL}{digimon_id}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch Digimon {digimon_id}. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching Digimon {digimon_id} : {e}")
        return None

def save_digimon_to_db(digimon_data):
    try:
        response = requests.post(SAVE_API_URL, json=digimon_data, verify=False)
    
        if response.status_code == 200:
            print(f"Successfully saved Digimon: {digimon_data['digiName']}")
        else:
            print(f"Failed to save Digimon. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error saving Digimon: {e}")

def automate(start_id, end_id):
    for digimon_id in range(start_id, end_id):
        data = fetch_digimon_data(digimon_id)
        if data:

            digi_type = "no_type"
            if data["types"] != []:
                digi_type = data["types"][0]['type']

            formated_data_dict = {
                "id": 0,
                "code": int(data["id"]),
                "digiName": data["name"],
                "imageUrl": data["images"][0]['href'],
                "monsterType": digi_type,
                "price": int(data["id"]) * 100
            }

            #print(formated_data_dict)

            #save into the database via API
            save_digimon_to_db(formated_data_dict)

        time.sleep(1)