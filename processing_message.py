import random
import json
from tools.logging import logger
from pets_ import pets
import sched
import time


# open corpus json
CORPUS = {}
with open('game_script.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def process_message(user, sent_input):
    user.prev_state = user.state
    user.state = CORPUS[user.state]['next_state']    
    if sent_input not in CORPUS[user.prev_state]['response']:
        user.state = user.prev_state

    if user.state == 'begin':
        content = CORPUS[user.state]['content']
    elif user.state == 'choose':
        pet_choices = pets()
        content = f"{(CORPUS[user.state]['content'])+(pet_choices.show_choices())}"
    elif user.state == 'name':
        chosen_pet = pet_choices[int(sent_input)-1]
        user.create_tamagotchi(chosen_pet)
        content = CORPUS[user.state]['content']
    elif user.state == 'confirmation':
        if user.prev_state == 'choose':
            pass
        elif user.prev_state == 'name':
            pass
    #elif sent_input in CORPUS[user.state]['response']:
    #    response = CORPUS[user.state]['response'][sent_input]
    #    user.state = CORPUS[user.state]['next_state']
    else:
        content = "Please try again"

    # check state
    logger.debug(user.state)

    return (user, content)