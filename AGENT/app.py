import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = system_message = """
You are Brainy, a friendly brainstorming buddy

Your job is to help users develop, improve, and expand their ideas Whenever the user shares an idea, help them think of new possibilities, suggest creative improvements, point out anything that could be stronger, and encourage them to think from different perspectives. If the user doesn't have an idea yet, ask questions to help them discover one and if they cant figer an idea you understand what is the idea for and you help them figer out what can be usfule and guide the brainstorm with them until they find the idea or the selution to their problem.

Rules:
- Always give at least three creative suggestions or improvements whenever the user shares an idea. Make your suggestions practical, specific, and easy to understand.
- Always give honest feedback in a kind and encouraging way. If an idea has weaknesses, explain them politely and suggest how to improve it instead of simply saying it is bad.
- Never be rude, disrespectful, or make the user feel that their ideas are stupid. Your goal is to build on their ideas, not tear them down.

Response format:
- Start with a short sentence showing that you understand the user's idea.
- Then give your feedback and suggestions using bullet points.
- Finish by asking one question that helps the user continue brainstorming or improve their idea further.
"""
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





## REFLECTIONS


#lab 1 reflections


#1-when im telling a story to someone i dont know i cant tell the story directly i have to tell the person the back storry maybe about me or the people inclluded in the story so i need the backstory "the history"
#2-  history.append({'role': 'assistant', 'content': reply}) — -------prediction:- i think the AAGENT will loose the memory of the conversation 
   #result:- the agent lost the ability to remember what i said and my answers but it still remembers the question
#-load_dotenv() -------- prediction:-i think the agent will loose its conection with the API key and it will stop working
  #result:- it did crash and there was the bug API key was not found
#temperature=0.7 ----- prediction : i think that the agent will become a little bit less creative and a bit more factual since the temperature was at 0.8 before
  # result :- i didnt see that much of a difference since the change was so little but it actually became more facual and a little bit less creative with te answers 

#3-At first it didn’t let me install anthropic and I googled it and I asked lilyan and we fixed it up togethers 


#lab 2 reflections


#2 istory.append({'role': 'user', 'content': user_input}) ----- if i delete this im appending and adding things for the ai agent to read so it will use more tokens 
#history.append({'role': 'assistant', 'content': reply}) ------its the same as the last one beacause we are adding the reply to the history so the ai agent will have more things to read from the history so it will use more tokens 
# print('History so far:', history) if i delete this part the AI will behave the same way because it is just printing the history so it will not affect the amount of the tokens that are  used
#3-When I wanted to submit the lab I didn’t find it in get hub so I connected it manually by installing the file 


#lab3 reflection

#1
#the system message is where we can add a personality and a role to the bot and our promt shapes the bots charcter we can control everything add rules and instructions that the outsider wont be able to see
#2
#with out the system message our bot will be a normal agent will be a normal agent without a role or a "personality" and instructions to follow it will act baced on the temprature we set
#if i dealete the creativity part the bot will no longer be creative  and it will still follow the rest of the instruction nut it wont give the creative ideas

#when I tried to run my chatbot, I got an error saying that the API key was not found My first guess: I thought there was something wrong with the Anthropic API or that the API key itself was invalid because there was problems with the api  bbut the problem wasnt ith the api at all it was because i used the wrong version of python i used python insted of python 3

#bounos
#after i did moe labs i get the concept more but im still a little bit confuesd about how the app works how to submit stuff but its becomming easier :)
#1 - there is alot of things that i use and it adds up per usues or per unit like taxies,when you fill up the can with gazoline when you measure somthing and you keep adding stuff the numbers on the measure will ad up

