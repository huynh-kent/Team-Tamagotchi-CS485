import pickle
import os

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

CORPUS = {}

with open('game_script.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def handle_request():
    # user info
    #logger.debug(request.form)
    logger.debug(request.form['From'])

    # pickling
    act = None
    first_time = False
    if os.path.exists(f"users/{request.form['From']}.pkl"):
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            act = pickle.load(p)
            response = (CORPUS[act.state]['content'])
    else:
        act = actor(request.form['From'])
        response = (CORPUS['begin']['content'])
        first_time = True
    act.save_msg(request.form['Body'])
    logger.debug(act.prev_msgs)
    act.state = (CORPUS[act.state]['next_state'])
    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(act,p)
    logger.debug('current state:')
    logger.debug(act.state)

    # corpus
      #### state =
       #### response = (CORPUS[state]

    """
        sent_input = str(request.form['Body']).lower()
        if sent_input in CORPUS['input']:
            response = random.choice(CORPUS['input'][sent_input])
        else:
            CORPUS['input'][sent_input] = ['DID NOT FIND']
            with open('chatbot_corpus.json', 'w') as myfile:
                myfile.write(json.dumps(CORPUS, indent=4 ))
        """

   #  response back
   ## response = 'response here'

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

                                                                                                                                                                                                      90,0-1        Bot
                                                                                                                                                                                                      94,0-1        Bot
