import json
from enum import Enum
from random import randint

import google.generativeai as genai

if __name__ == "__main__":
    from promps import promp_list_reddit
else:
    from api.promps import promp_list_reddit


class HistoryType(Enum):
    REDDIT = 0
    HORROR = 1
    SPACE = 2
    HOPECORE = 3
    LAUGH = 4


class GeminiAPI:
    def __init__(self, key, model="gemini-1.5-flash"):
        self.key = key
        self.model = model
        genai.configure(api_key=self.key)

    def response(self, history_type: HistoryType = HistoryType.REDDIT, json_type: bool = False):
        response = genai.GenerativeModel(self.model)
        match history_type:
            case HistoryType.REDDIT:
                response = response.generate_content(promp_list_reddit[randint(0, len(promp_list_reddit) - 1)])
            case HistoryType.HORROR:
                return "Horror History In Development"
            case HistoryType.SPACE:
                return "Space History In Development"
            case HistoryType.HOPECORE:
                return "Hopecore videos In Development"
            case HistoryType.LAUGH:
                return "Laugh clips videos In Development"
            case _:
                return "Invalid History Type"
        response = response.text.replace("```json", "").replace("```", "")
        if json_type:
            return json.loads(response)
        else:
            return response
