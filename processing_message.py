import random
import json
from tools.logging import logger
from pets_ import pets
from drinks_ import drinks, drink
from foods_ import foods, food
import sched
from send_message_back import send_message
from guessmoji import Guessmoji
import time

# open corpus json
CORPUS = {}
with open('game_script.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())


def process_message(user, sent_input):
    logger.debug(f'State Before: {user.state}')

    user.prev_state = user.state
    user.state = CORPUS[user.state]['next_state']   

    if 'response' in CORPUS[user.prev_state] and sent_input not in CORPUS[user.prev_state]['response']:
        user.state = user.prev_state

    if user.state == 'begin':
        content = CORPUS[user.state]['content']

    elif user.state == 'choose':
        content = f"{(CORPUS[user.state]['content'])}"
        send_message(user.phone, user.pet_choices.show_choices())

    elif user.state == 'name':
        user.create_tamagotchi(user.pet_choices.pet_options[int(sent_input)-1])
        send_message(user.phone, user.tamagotchi.emoji)
        content = CORPUS[user.state]['content']
        user.recreate_choices()

    elif user.state == 'confirmation':
        user.tamagotchi.name = sent_input.upper()
        content = f"{(user.tamagotchi.name)+(CORPUS[user.state]['content'])}"

    elif user.state == 'congratulations':
        if sent_input == 'no':
            user.state = user.prev_state
            send_message(user.phone, user.tamagotchi.emoji)
            content = CORPUS['name']['content']
        else:
            send_message(user.phone, """LOADING...
████████████]99% 
""")
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
                user.recreate_choices()
                send_message(user.phone, user.drink_choices.show_choices())
            elif sent_input == 'food':
                user.recreate_choices()
                send_message(user.phone, user.food_choices.show_choices())
        else:
            content = CORPUS[user.state]['content']

    elif user.state == 'drinks':
        if sent_input not in CORPUS['drinks']['response']:
            content = CORPUS[user.state]['content']
            send_message(user.phone, user.drink_choices.show_choices())
        else:
            chosen_drink = drink(user.drink_choices.drink_options[int(sent_input)-1])
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
            send_message(user.phone, user.food_choices.show_choices())
        else:
            chosen_food = food(user.food_choices.food_options[int(sent_input)-1])
            send_message(user.phone, chosen_food.emoji)
            user.tamagotchi.eat(chosen_food)
            content = f"{user.tamagotchi.name} has satisfied {chosen_food.hunger} hunger points from eating that!"
            user.state = 'idle'
            send_message(user.phone, f"{user.tamagotchi.name} is eating...")
            send_message(user.phone, user.tamagotchi.draw())
            send_message(user.phone, content)
            content = CORPUS[user.state]['content']

    elif user.state == 'play':
        if sent_input not in CORPUS['play']['response']:
            content = CORPUS[user.state]['content']
            if user.game:
                if user.game.check_guess(sent_input):
                    send_message(user.phone, f"Correct! Your Score is now {user.game.score}!")
                    user.game.select_word()
                else:
                    send_message(user.phone, "Incorrect Answer, Try Again!")
                content = user.game.current_word
        elif sent_input == 'start':
            if user.tamagotchi.energy < 10:
                send_message(user.phone, "Not enough energy to play! Try sleeping!")
                user.state = 'idle'
                send_message(user.phone, user.tamagotchi.draw())
                content = CORPUS[user.state]['content']

            elif not user.game:
                send_message(user.phone, "Starting a game of Guessmoji")
                user.game = Guessmoji()
                user.game.select_word()
                user.tamagotchi.play()
                content = user.game.current_word
            else:
                send_message(user.phone, "Incorrect Answer, Try Again!")
                content = user.game.current_word
        elif sent_input == 'finish':
            user.state = 'idle'
            send_message(user.phone, "Ending game, thank you for playing Guessmoji!")
            send_message(user.phone, user.tamagotchi.draw())
            user.clear_game()
            content = CORPUS[user.state]['content']

    elif user.state == 'sleep':
        if sent_input not in CORPUS['sleep']['response']:
            content = CORPUS[user.state]['content']
        else:
            send_message(user.phone, f"{user.tamagotchi.name} is now asleep!")
            content = CORPUS[user.state]['content']
            t = 10
            def countdown(t):

                while t:
                    mins, secs = divmod(t,60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    time.sleep(1)
                    t -= 1

            countdown(int(t))
            send_message(user.phone, f"{user.tamagotchi.name} has woken up!")
            user.tamagotchi.sleep()
            user.state = 'idle'
            send_message(user.phone, user.tamagotchi.draw())
            send_message(user.phone, content)
            content = CORPUS[user.state]['content']
            send_message(user.phone, content)    

    elif user.state == 'clean':
        if sent_input not in CORPUS['clean']['response']:
            content = CORPUS[user.state]['content']
        elif sent_input == 'yes':
            if user.tamagotchi.potty_clean:
                send_message(user.phone, "There is no mess to clean right now!")
            else:
                send_message(user.phone, "Cleaning up after your pets mess!")
                user.tamagotchi.potty_clean = True
                user.tamagotchi.potty_times = 0
            user.state = 'idle'
            send_message(user.phone, user.tamagotchi.draw())
            content = CORPUS[user.state]['content']

        elif sent_input == 'no':
            send_message(user.phone, "input = no")
            user.state = 'idle'
            send_message(user.phone, user.tamagotchi.draw())
            content = CORPUS[user.state]['content']
            

    # check state
    logger.debug(f'State After: {user.state}')

    return (user, content)
