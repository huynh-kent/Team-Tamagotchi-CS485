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
        self.choices = {random.sample(all_pets, 3)}

    def show_choices(self):
        #for count,choice in enumerate(self.choices):
        #    print(f"{choice} --- {self.pet_hunger[count]}")
        pet_string = ''
        for choice in self.choices:
            self.pet_options.append(choice)
            pet_string += choice

        return pet_string
        
class pet:
    emoji = ''

    def __init__(self, emoji):
        self.emoji = emoji

