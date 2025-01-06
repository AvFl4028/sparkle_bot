from keys import GEMINI_API_KEY
from api.gemini import GeminiAPI

def main():
    gemini = GeminiAPI(GEMINI_API_KEY)
    print(gemini.response("""
                          Make only one reddit history of 2 minutes long, then divide the history in two parts, after that, in only one json file format, without anything else.
                          In the history exclude all the images and videos, only the text is needed.
                          The json format should be like this:
                            {
                                "user": "{generate a random username}",
                                "reddit_history": {
                                "title": "{Title of the reddit history}",
                                "part1": {
                                    "content": "{Content of the post and need to be 1 minute long}"
                                },
                                "part2": {
                                    "content": "{Content of the post and need to be 1 minute long}"
                                }
                                }
                            }
                          """))


if __name__ == "__main__":
    main()
