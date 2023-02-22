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
    choices = {}
    food_hunger = []

    def __init__(self):
        self.choices = random.sample(all_foods, 3)
        for food in self.choices:
            self.food_hunger.append(random.randint(10, 30))

    def show_choices(self):
        for count,choice in enumerate(self.choices):
            print(f"{choice} --- {self.food_hunger[count]}")

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

    def __init__(self, emoji, hunger):
        self.emoji = emoji
        self.hunger = hunger
