

import google.generativeai as genai

genai.configure(api_key = "<Your API key>")
model = genai.GenerativeModel("gemini-1.5-pro")


def chatGemini(msg):    
    resp = model.generate_content(msg)
    return resp.text