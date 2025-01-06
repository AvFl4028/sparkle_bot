import google.generativeai as genai

class GeminiAPI:
    def __init__(self, key, model="gemini-1.5-flash"):
        self.key = key
        self.model = model
        genai.configure(api_key=self.key)


    def response(self, promp: str = "Explain how AI works"):
        response = genai.GenerativeModel(self.model)
        response = response.generate_content(promp)
        return response.text
