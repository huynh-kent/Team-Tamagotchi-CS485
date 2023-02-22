import random
import json
from tools.logging import logger
from pets_ import pets
import sched
from send_message_back import send_message
import time
from apscheduler.schedulers.background import BackgroundScheduler


# open corpus json
CORPUS = {}
with open('game_script.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

pet_choices = pets()

scheduler = BackgroundScheduler()
def time_passed(user):
    user.tamagotchi.time_tick()
    return user

def process_message(user, sent_input):
    user.prev_state = user.state
    user.state = CORPUS[user.state]['next_state']   

    if 'response' in CORPUS[user.prev_state] and sent_input not in CORPUS[user.prev_state]['response']:
        user.state = user.prev_state

    if user.state == 'begin':
        content = CORPUS[user.state]['content']
    elif user.state == 'choose':
        content = f"{(CORPUS[user.state]['content'])+(pet_choices.show_choices())}"
    elif user.state == 'name':
        user.create_tamagotchi(pet_choices.pet_options[int(sent_input)-1])
        send_message(user.phone, user.tamagotchi.emoji)
        scheduler.add_job(lambda: time_passed(user=user), trigger="interval", seconds=10)
        scheduler.start()
        content = CORPUS[user.state]['content']
    elif user.state == 'confirmation':
        user.tamagotchi.name = sent_input
        content = f"{(user.tamagotchi.name)+(CORPUS[user.state]['content'])}"
    elif user.state == 'congratulations':
        if sent_input == 'no':
            user.state = user.prev_state
            send_message(user.phone, user.tamagotchi.emoji)
            content = CORPUS['name']['content']
        else:
            content = f"{(CORPUS[user.state]['content'])+(user.tamagotchi.name)}! 🎉🎉🎉"
            user.state = 'idle'
    else:
        content = "Please try again"
        
    if user.state == 'idle':
        send_message(user.phone, user.tamagotchi.draw())


    #elif sent_input in CORPUS[user.state]['response']:
    #    response = CORPUS[user.state]['response'][sent_input]
    #    user.state = CORPUS[user.state]['next_state']

    # check state
    logger.debug(user.state)

    return (user, content)