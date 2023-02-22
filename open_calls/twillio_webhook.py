from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.logging import logger

from pickles import pickling, save_pickle
from send_message_back import send_message, send_picture
from processing_message import process_message

### Main
def handle_request():
    # user info
    #logger.debug(request.form)
    logger.debug(request.form['From'])

    # get user - pickling from pickles.py 
    user = pickling(request.form)
    # get user - state
    state = user.state
    # processing incoming message from processing_message.py
    sent_input = str(request.form['Body']).lower()
    user, response = process_message(user, sent_input)

    # send message back/game state from send_message_back.py
    send_message(user.phone, response)
    # send picture name/url from media.yml
    #picture_name = 'sample-tamagotchi-image'
    #send_picture(request.form, picture_name)

    # test
    #send_message(request.form, get_tamagotchi())

    # save pickle/user
    save_pickle(request.form, user)

    return json_response( status = "ok" )
