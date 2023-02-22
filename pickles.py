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
    # returning user
    if os.path.exists(f"users/{form['From']}.pkl"):   
        with open(f"users/{form['From']}.pkl", 'rb') as p:
            act = pickle.load(p)
            #response = (CORPUS[act.state]['content'])
    # new user
    else:
        act = actor(form['From'])
        #response = (CORPUS['begin']['content'])

    # save into message history
    act.save_msg(form['Body'])
    logger.debug(f'Msgs: {act.prev_msgs}')

    # set new state
    #act.state = (CORPUS[act.state]['next_state'])
    logger.debug(f'State: {act.state}')

    return act

# save pickle/user data
def save_pickle(act):
    with open(f"users/{act.phone}.pkl", 'wb') as p:
        pickle.dump(act,p)

