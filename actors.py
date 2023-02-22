import tamagotchi

class actor:

    def __init__(self, phone_number):
        self.phone = phone_number
        self.prev_msgs = []
        self.state = "begin"
        self.prev_state = ''
        print('this is created:')
        print(self.state)
        self.tamagotchi = None

    def save_msg(self, msg):
        self.prev_msgs.append(msg)

    def change_state(self, new_state):
        state = new_state

    def create_tamagotchi(self, pet):
        self.tamagotchi = tamagotchi(pet)