from test_sending_message import send_message
from test_processing_message import process_message
from actors import actor

print('Hello, Welcome to Tamagotchi what is your #Number?')
name = input()

print(f"Alright Type anything to begin!")
user = actor(name)

while True:
    sent_input = input().lower()

    user, response = process_message(user, sent_input)
    print(f'Chatbot: {response}')