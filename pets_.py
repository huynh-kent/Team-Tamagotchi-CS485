import random

all_pets = ['🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐻‍❄️','🐨','🐯','🦁','🐮','🐷','🐸','🐵','🐒',
            '🐔','🐧','🐦','🐤','🐣','🐥','🦆','🦅','🦉','🦇','🐺','🐗','🐴','🦄','🐝','🪱','🐛',
            '🦋','🐌','🪳','🪲','🪰','🐜','🐞','🦟','🦗','🕷️','🦂','🐢','🐍','🦎','🦖','🦕','🐙',
            '🦑','🦐','🦞','🦀','🐳','🐬','🐟','🐠','🐡','🐋','🦈','🦭','🐊','🐅','🦣','🦧','🦍',
            '🦓','🐆','🐘','🦛','🦏','🐪','🐫','🐂','🐃','🦬','🦘','🦒','🐄','🐎','🐖','🐏','🐑',
            '🐩','🐕','🦌','🐐','🦙','🦮','🐕‍🦺','🐈','🐈‍⬛','🦜','🦚','🦤','🦃','🐓','🦢','🦩','🕊️',
            '🦝','🐇','🦨','🦡','🦫','🦦','🦥','🦔','🐿️','🐀','🐁','🐉','🐲']


class pets:
    pet_options = []
    choices = {}
    def __init__(self):
        pass

    def show_choices(self):
        self.choices = random.sample(all_pets, 3)
        pet_string = ''
        self.pet_options = []
        for choice in self.choices:
            self.pet_options.append(choice)
            pet_string += choice

        return pet_string
        
    def clear_options(self):
        self.pet_options = []        

class pet:
    emoji = ''

    def __init__(self, emoji):
        self.emoji = emoji

