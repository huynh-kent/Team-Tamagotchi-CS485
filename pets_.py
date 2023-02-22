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
        self.choices = set(random.choices(all_pets, k=3))
        #for pet in self.choices:
        #    self.pet_hunger.append(random.randint(1, 10))

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

