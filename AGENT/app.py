import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Alex. You are a helpful and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity be helpful and answer in short sentences."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        print('History:', history)
        response = client.messages.create(
    model='claude-haiku-4-5-20251001',
    max_tokens=300,   # try 50, then 500
    temperature=0.7,  # try 0, then 1
    system=system_message,
    messages=history
)


        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=250,
            temperature=0.6,
            system=system_message,
            messages=history
        )
        print(response)
        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()


#the higher the tempretature the more creative the bot will be and the lower it is the less creative and it will be more factual
# the API needs a full history every time so it can remember the context of the conversation and go back to pervious messages. 
