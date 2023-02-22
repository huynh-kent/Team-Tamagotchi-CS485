from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.logging import logger

from pickles import pickling
from send_message_back import send_message, send_picture
from processing_message import process_message

from tamagotchi import get_tamagotchi # test

### Main
def handle_request():
    # user info
    #logger.debug(request.form)
    logger.debug(request.form['From'])

    # get user - pickling from pickles.py 
    user = pickling(request.form)


    # send message back/game state from send_message_back.py
    send_message(request.form, response)
    # send picture name/url from media.yml
    picture_name = 'sample-tamagotchi-image'
    send_picture(request.form, picture_name)

    # processing incoming message from processing_message.py
    sent_input = str(request.form['Body']).lower()
    response = process_message(sent_input)

    # test
    #send_message(request.form, get_tamagotchi())

    return json_response( status = "ok" )

print("main?")
