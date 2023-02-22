import random
import json
from tools.logging import logger
from pets_ import pets
from drinks_ import drinks, drink
from foods_ import foods, food
import sched
from send_message_back import send_message
import time


# open corpus json
CORPUS = {}
with open('game_script.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())


def process_message(user, sent_input):
    pet_choices = pets()
    drink_choices = drinks()
    food_choices = foods()

    user.prev_state = user.state
    user.state = CORPUS[user.state]['next_state']   

    if 'response' in CORPUS[user.prev_state] and sent_input not in CORPUS[user.prev_state]['response']:
        user.state = user.prev_state

    if user.state == 'begin':
        content = CORPUS[user.state]['content']

    elif user.state == 'choose':
        content = f"{(CORPUS[user.state]['content'])}"
        send_message(user.phone, pet_choices.show_choices())

    elif user.state == 'name':
        user.create_tamagotchi(pet_choices.pet_options[int(sent_input)-1])
        send_message(user.phone, user.tamagotchi.emoji)
        content = CORPUS[user.state]['content']

    elif user.state == 'confirmation':
        user.tamagotchi.name = sent_input.upper()
        content = f"{(user.tamagotchi.name)+(CORPUS[user.state]['content'])}"

    elif user.state == 'congratulations':
        if sent_input == 'no':
            user.state = user.prev_state
            send_message(user.phone, user.tamagotchi.emoji)
            content = CORPUS['name']['content']
        else:
            congrats = f"{(CORPUS[user.state]['content'])+(user.tamagotchi.name)}! 🎉🎉🎉"
            user.state = 'idle'
        
    if user.state == 'idle':
        if sent_input not in CORPUS['idle']['response']:
            send_message(user.phone, user.tamagotchi.draw())
            try: send_message(user.phone, congrats) 
            except: pass
            content = CORPUS[user.state]['content']
        else:
            user.state = sent_input
            content = CORPUS[user.state]['content']
    elif user.state == 'shop':
        if sent_input in CORPUS['shop']['response']:
            user.state = sent_input
            content = CORPUS[user.state]['content']
            if sent_input == 'drinks':
                send_message(user.phone, drink_choices.show_choices())
            elif sent_input == 'food':
                send_message(user.phone, food_choices.show_choices())

    elif user.state == 'drinks':
        if sent_input not in CORPUS['drinks']['response']:
            content = CORPUS[user.state]['content']
            send_message(user.phone, drink_choices.show_choices())
        else:
            chosen_drink = drink(drink_choices.drink_options[int(sent_input)-1])
            send_message(user.phone, chosen_drink.emoji)
            user.tamagotchi.drink(chosen_drink)
            content = f"{user.tamagotchi.name} has quenched {chosen_drink.thirst} thirst from drinking that!"
            user.state = 'idle'
            send_message(user.phone, f"{user.tamagotchi.name} is drinking...")
            send_message(user.phone, user.tamagotchi.draw())
            send_message(user.phone, content)
            content = CORPUS[user.state]['content']

    elif user.state == 'food':
        if sent_input not in CORPUS['food']['response']:
            content = CORPUS[user.state]['content']
            send_message(user.phone, food_choices.show_choices())
        else:
            chosen_food = food(food_choices.food_options[int(sent_input)-1])
            send_message(user.phone, chosen_food.emoji)
            user.tamagotchi.eat(chosen_food)
            content = f"{user.tamagotchi.name} has satisfied {chosen_food.hunger} hunger points from eating that!"
            user.state = 'idle'
            send_message(user.phone, f"{user.tamagotchi.name} is eating...")
            send_message(user.phone, user.tamagotchi.draw())
            send_message(user.phone, content)
            content = CORPUS[user.state]['content']

            


            


    #elif sent_input in CORPUS[user.state]['response']:
    #    response = CORPUS[user.state]['response'][sent_input]
    #    user.state = CORPUS[user.state]['next_state']

    # check state
    logger.debug(f'State After: {user.state}')

    return (user, content)