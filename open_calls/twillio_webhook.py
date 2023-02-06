import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

yml_configs = {}
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)


def handle_request():
    print(request.form['Body']) # prints incoming message
    ### test
    print(request.form)
    form = request.form
    for line in form:
        print(line)
    ###
    return json_response( status = "ok" )
