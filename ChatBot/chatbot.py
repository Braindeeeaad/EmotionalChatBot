import google.generativeai as genai
import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)



geminiModel = genai.GenerativeModel("gemini-pro")
chat = geminiModel.start_chat(history=[])



def get_gemini_response(query):
    instantResponse = chat.send_message(query,stream=True)
    return instantResponse


if __name__ == '__main__':
    print("A simple Chat Bot")

    while True:

        inputText =input("\nInput: ")
        if inputText == "quit":
            break

        
        output = get_gemini_response(inputText)
        for outputChunk in output:
            print(outputChunk.text,end=" ")




