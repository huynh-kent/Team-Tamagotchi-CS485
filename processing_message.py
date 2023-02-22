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
        content = f"{content}"
    elif user.state == 'choose':
        pet_choices = pets()
        fstring = CORPUS[user.state]['content']
        content = (f"{fstring}")
    elif user.state == 'name':
        pass
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