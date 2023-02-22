import random

all_foods = ['🍏', '🍎','🍐','🍊','🍋','🍌','🍉','🍇','🍓','🫐','🍈',
             '🍒','🍑','🥭','🍍','🥥','🥝','🍅','🍆','🥑','🥦','🥬',
             '🥒','🌶️','🫑','🌽','🥕', '🫒','🧄','🧅','🥔','🍠','🥐',
             '🥯','🍞','🥖','🥨','🧀','🥚','🍳','🧈','🥞','🧇','🥓',
             '🥩','🍔','🌭','🦴','🍖','🍗','🍟','🍕','🫓','🥪','🥙',
             '🥗','🫔','🌯','🌮','🧆','🥘','🫕','🥫','🫙','🍝','🍱',
             '🍣','🍛','🍲','🍜','🥟','🦪','🍤','🍙','🍚','🍘','🍥',
             '🥠','🥮','🍢','🍡','🍧','🍨','🍦','🥧','🍭','🍮','🎂',
             '🍰','🧁','🍬','🍫','🍿','🍩','🍪','🍯','🫘','🥜','🌰']



class foods:
    food_options = []
    choices = {}

    def __init__(self):
        self.choices = random.sample(all_foods, 3)

    def show_choices(self):
        food_string = ''
        for choice in self.choices:
            self.food_options.append(choice)
            food_string += choice
        
        return food_string

    def give_food_choices(self):
        food_options = []
        for count,choice in enumerate(self.choices):
            food_option = food(choice, self.food_hunger[count])
            print(food_option.emoji, food_option.hunger, end=' ')
            food_options.append(food_option)
        return food_options
        

        
class food:
    emoji = ''
    hunger = 0

    def __init__(self, emoji):
        self.emoji = emoji
        self.hunger = random.randint(10, 30)
