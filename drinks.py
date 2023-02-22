import random

all_drinks = ['🥛','🍼','🫖','☕️','🍵','🧃','🥤','🧋','🍶',
              '🍺','🍻','🥂','🍷','🥃','🍸','🍹','🧉','🍾',
              ]

class drinks:
    choices = {}
    drink_thirst = []

    def __init__(self):
        self.choices = random.sample(all_drinks, 3)
        for drink in self.choices:
            self.drink_thirst.append(random.randint(10, 30))

    def show_choices(self):
        for count,choice in enumerate(self.choices):
            print(f"{choice} --- {self.drink_thirst[count]}")

    def give_drink_choices(self):
        drink_options = []
        for count,choice in enumerate(self.choices):
            drink_option = drink(choice, self.drink_thirst[count])
            drink_options.append(drink_option)
            print(drink_option.emoji, drink_option.thirst, end=' ')
        return drink_options
        

        
class drink:
    emoji = ''
    thirst = 0

    def __init__(self, emoji, thirst):
        self.emoji = emoji
        self.thirst = thirst
