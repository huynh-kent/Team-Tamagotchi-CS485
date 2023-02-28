import random

all_drinks = ['🥛','🍼','🫖','☕️','🍵','🧃','🥤','🧋','🍶',
              '🍺','🍻','🥂','🍷','🥃','🍸','🍹','🧉','🍾',
              ]

class drinks:
    drink_options = []
    choices = {}

    def __init__(self):
        pass

    def show_choices(self):
        self.choices = random.sample(all_drinks, 3)
        drink_string = ''
        self.drink_options = []
        for choice in self.choices:
            self.drink_options.append(choice)
            drink_string += choice

        return drink_string
        

    def give_drink_choices(self):
        drink_options = []
        for count,choice in enumerate(self.choices):
            drink_option = drink(choice, self.drink_thirst[count])
            drink_options.append(drink_option)
            print(drink_option.emoji, drink_option.thirst, end=' ')
        return drink_options
    
    def clear_options(self):
        self.drink_options = []
        

        
class drink:
    emoji = ''
    thirst = 0

    def __init__(self, emoji):
        self.emoji = emoji
        self.thirst = random.randint(10, 30)
