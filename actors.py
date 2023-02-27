from tamagotchi import Tamagotchi
from guessmoji import Guessmoji

class actor:

    def __init__(self, phone_number):
        self.phone = phone_number
        self.prev_msgs = []
        self.state = "begin"
        self.prev_state = ''
        self.tamagotchi = None
        self.game = None

    def save_msg(self, msg):
        self.prev_msgs.append(msg)

    def change_state(self, new_state):
        self.state = new_state

    def create_tamagotchi(self, pet):
        self.tamagotchi = Tamagotchi(pet)

    def clear_game(self):
        self.game = None