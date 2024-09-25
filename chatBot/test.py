import openai

# Set your OpenAI API key
openai.api_key = "sk-Pi_H4cH67lvuVUBrUuk7KAqprUZUO-A6kiEIDqZ4cZT3BlbkFJ9m2cncSYaDiDMMt5M19rld2GIAHu36kehbqI4sumEA"

def list_models():
    try:
        models = openai.Model.list()  # List all models
        for model in models['data']:
            print(model['id'])  # Print model IDs
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    list_models()


""" dall-e-2
tts-1-hd-1106
tts-1-hd
whisper-1
text-embedding-3-large
text-embedding-ada-002
tts-1-1106
gpt-3.5-turbo-16k
gpt-3.5-turbo-1106
gpt-3.5-turbo-instruct-0914
gpt-3.5-turbo-0125
text-embedding-3-small
gpt-3.5-turbo-instruct
gpt-3.5-turbo
gpt-4o-mini-2024-07-18
gpt-4o-mini
babbage-002
davinci-002
dall-e-3
tts-1
"""
