from keys import GEMINI_API_KEY
from api.gemini import GeminiAPI, HistoryType

def main():
    gemini = GeminiAPI(GEMINI_API_KEY)
    response = gemini.response(HistoryType.REDDIT, True)
    print(response["reddit_history"]["part1"]["content"])
    print("--------------------------------------------------------------------")
    print(response["reddit_history"]["part2"]["content"])


if __name__ == "__main__":
    main()
