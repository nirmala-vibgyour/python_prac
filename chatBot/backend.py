import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "sk-Pi_H4cH67lvuVUBrUuk7KAqprUZUO-A6kiEIDqZ4cZT3BlbkFJ9m2cncSYaDiDMMt5M19rld2GIAHu36kehbqI4sumEA"

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

