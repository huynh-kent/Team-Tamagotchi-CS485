import random

all_pets = ['🍏', '🍎','🍐','🍊','🍋','🍌','🍉','🍇','🍓','🫐','🍈',
             '🍒','🍑','🥭','🍍','🥥','🥝','🍅','🍆','🥑','🥦','🥬',
             '🥒','🌶️','🫑','🌽','🥕', '🫒','🧄','🧅','🥔','🍠','🥐',
             '🥯','🍞','🥖','🥨','🧀','🥚','🍳','🧈','🥞','🧇','🥓',
             '🥩','🍔','🌭','🦴','🍖','🍗','🍟','🍕','🫓','🥪','🥙',
             '🥗','🫔','🌯','🌮','🧆','🥘','🫕','🥫','🫙','🍝','🍱',
             '🍣','🍛','🍲','🍜','🥟','🦪','🍤','🍙','🍚','🍘','🍥',
             '🥠','🥮','🍢','🍡','🍧','🍨','🍦','🥧','🍭','🍮','🎂',
             '🍰','🧁','🍬','🍫','🍿','🍩','🍪','🍯','🫘','🥜','🌰']



class pets:
    
    def __init__(self):
        self.choices = random.choices(all_pets, k=3)
        #for pet in self.choices:
        #    self.pet_hunger.append(random.randint(1, 10))

    def show_choices(self):
        #for count,choice in enumerate(self.choices):
        #    print(f"{choice} --- {self.pet_hunger[count]}")
        pet_options = []
        for choice in self.choices:
            pet_options.append(choice)

        return pet_options

    def give_pet_choices(self):
        """pet_options = []
        for count,choice in enumerate(self.choices):
            pet_option = pet(choice, self.pet_hunger[count])
            print(pet_option.emoji, pet_option.hunger, end=' ')
            pet_options.append(pet_option)
        return pet_options"""
        
        
class pet:
    emoji = ''
    hunger = 0

    def __init__(self, emoji):
        self.emoji = emoji


test = pets()
test.give_pet_choices()
