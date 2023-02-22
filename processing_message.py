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

    if user.state == 'begin':
        content = f"{CORPUS[user.state]['content']}"
    elif user.state == 'choose':
        pet_choices = pets()
        content = f"{CORPUS[user.state]['content']}"
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

    user.state = CORPUS[user.state]['next_state']    
    # check state
    logger.debug(user.state)

    return (user, content)