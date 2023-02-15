import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

from tools.logging import logger
from things.actors import actor

import random
import json
import pickle
import os

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

# corpus 
CORPUS = {}
with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def handle_request():
    logger.debug(request.form)

    # pickling
    act = None
    if os.path.exists(f"users/{request.form['From']}.pkl"):
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            actor = pickle.load(p)
    else:
        act = actor(request.form['From'])

    act.save_msg(request.form['Body'])
    logger.debug(act.prev_msgs)
    with open(f"user/{request.form['Form']}.pkl", 'wb') as p:
        pickle.dump(act,p)

    response = 'response here'

    # checking if input in corpus
    sent_input = str(request.form['Body']).lower()
    if sent_input in CORPUS['input']:
        response = random.choice(CORPUS['input'][sent_input])
    else:
        CORPUS['input'][sent_input] = ['DID NOT FIND']
        with open('chatbot_corpus.json', 'w') as myfile:
            myfile.write(json.dumps(CORPUS, indent=4))

    logger.debug(response)

    message = g.sms_client.messages.create(
                     body=response,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])
    
    return json_response( status = "ok" )

# tamagotchi outline
tamagotchi_outline = """                     🌸🌸🌸
             🌸🌸🌸🌸🌸🌸
                             🌸🌸🌸🌸🌸🌸🌸🌸
                                       🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                                 🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                                           🌸🌸🌸🌸🌸🌸🌸🌸🌸
                                                                           🌸🌸🌸🌸🌸🌸🌸🌸
                                                                                                     🌸🌸🌸🌸🌸🌸
                                                                                                                                         🌸🌸🌸🌸"""