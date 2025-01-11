import json

json_file = open('src/keys.json', "r")
json_data = json.load(json_file)

GEMINI_API_KEY = json_data["gemini_api"]
ELEVENLABS_API_KEY = json_data["elevenlabs_api"]["1"]
