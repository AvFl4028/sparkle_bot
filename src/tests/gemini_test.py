import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.gemini import GeminiAPI
from keys import GEMINI_API_KEY
import json

test_dic_structure = {
    "user": "Curious_Platypus7",
    "reddit_history": {
        "title": "My Two-Minute Reddit Dive into the World of Coffee",
        "part1": {
            "content": "Just finished my morning cup of joe, and it got me thinking about the vast world of coffee.  I've been using the same pre-ground blend for years, but I'm starting to feel like I'm missing out.  So many different beans, roasts, brewing methods...it's overwhelming!  Saw a post earlier about pour-over techniques, and it looks pretty intricate. I'm tempted to try it, but I'm worried about making a mess. Maybe I should start with a simple French press first?  That seems less intimidating.  I'm also curious about the ethical sourcing of coffee beans.  I know there are a lot of issues with fair trade and sustainability.  Reading up on those certifications can be tricky though, so much jargon.  And then there's the whole debate about dark roast vs. light roast.  Which one actually brings out the best flavor?  I need to do some serious research before committing to a new method or bean type.  What are some good resources for learning more about coffee?  Anyone have recommendations for beginner-friendly guides?"
        },
        "part2": {
            "content": "Okay, so after spending some time on r/Coffee, I've got a much better understanding of the complexities of coffee!  I'm leaning towards trying a French press first, as it seems like a good middle ground between simplicity and quality.  I also found some great resources on ethical sourcing, and I'm planning to check out some certifications before buying new beans.  The debate about light vs. dark roast is still a bit confusing, but I think I'll start with a medium roast to see where my preferences lie.  I've also discovered the world of home roasting, which sounds incredibly interesting but potentially very messy and time-consuming.  That might be a project for a later date!  I'm really excited to experiment with different brewing methods and bean types.  It feels like I've opened up a whole new world of flavor and possibilities.  Now, the question is, what kind of grinder should I buy?  There seems to be a huge range of options and price points...This coffee rabbit hole is deeper than I anticipated!  Anyone have recommendations on a good grinder for a beginner?  I need to set a budget before I get carried away!"
        },
    },
}

history_test = {}

if __name__ == "__main__":
    gemini = GeminiAPI(GEMINI_API_KEY)

    for i in range(20):
        print(f"Test {i + 1} of 20")
        history_test[f"{i}"] = gemini.response(json_type=True)

    with open("src/api/history_test.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(history_test, ensure_ascii=False, indent=4))
        f.close()
    print("Test completed successfully.")
