import json, os, requests

#Read json(config.json)
JSON_PATH = str(os.getcwd()) + '\config.json'
def read_json():
   with open(JSON_PATH, 'r') as file:
       data = json.load(file)
       result = [data['config']['guild_id'], data['config']['token']]
   return result

#get Channel ID from REST API
def get_channel_id(guild_id: str):
    http_get = requests.get(url=f"http://gcp.4n63l.com:8000/logchannel/get/{guild_id}")
    if http_get.status_code == 200:
        return int(http_get.json()['channel_id'])
    elif http_get.status_code == 404:
        return http_get.json()['detail']
    else:
        return None