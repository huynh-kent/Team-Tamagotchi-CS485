import pickle
from actors import actor
from tools.logging import logger
import os
import json

CORPUS = {}
with open('game_script.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def pickling(form):
    # pickling
    act = None
    first_time = True
    if os.path.exists(f"users/{form['From']}.pkl"):
        with open(f"users/{form['From']}.pkl", 'rb') as p:
            act = pickle.load(p)
            response = (CORPUS[act.state]['content'])
    else:
        act = actor(form['From'])
        response = (CORPUS['begin']['content'])
        first_time = False

    act.save_msg(form['Body'])
    logger.debug(act.prev_msgs)
    act.state = (CORPUS[act.state]['next_state'])
    with open(f"users/{form['From']}.pkl", 'wb') as p:
        pickle.dump(act,p)
    logger.debug('current state:')
    logger.debug(act.state)
    return response