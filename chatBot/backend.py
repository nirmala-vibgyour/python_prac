import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "--to-be-filled--"

    def getResponse(self, userInput):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": userInput}]
        )
        return response['choices'][0]['message']['content']


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.getResponse("Write a joke about birds.")
    print(response)

