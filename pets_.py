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
    choices = {random.choices(all_pets, k=3)}
    def __init__(self):
        #self.choices = {random.choices(all_pets, k=3)}
        pass

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

