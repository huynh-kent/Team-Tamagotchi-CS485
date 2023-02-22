import random
import json
from tools.logging import logger

# open corpus json
CORPUS = {}
with open('game_script.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def process_message(user, sent_input):
    if user.state == 'begin':
        response = 'Hi, Welcome!'
        user.state = CORPUS[user.state]['next_state']
    elif sent_input in CORPUS[user.state]['response']:
        response = CORPUS[user.state]['response'][sent_input]
        user.state = CORPUS[user.state]['next_state']
    else:
        response = "Please try again"

    # check state
    logger.debug(user.state)

    return (user, response)