class Tamagotchi:
    age = 0
    happiness: int = 100
    hunger: int = 100
    thirst: int = 100
    alive = True
    bored: int = 0
    energy: int = 100
    name = ''
    in_need = False
    is_sick = False
    potty_clean = True
    potty_times: int = 0
    happiness_emoji = "🙂"

    def __init__(self, emoji):
        self.emoji = emoji
        var_list = [self.age, self.happiness, self.hunger, self.thirst, self.bored, self.energy] #'''self.is_sick, self.potty_clean, self.potty_times'''
        def num_limit(num, minimum=0, maximum=100):
            return max(min(num, maximum), minimum)
        map(num_limit, var_list)

    #'''def get_sick(self):
     #   self.is_sick = True
        
    #def check_potty(self):
     #   if self.potty_clean = False **How can i make this only turn false after a certain time tick?'''
        
    def eat(self, food):
        self.hunger += food.hunger
        self.potty_times += 1
        if self.potty_times >= 3:
            self.potty_clean = False

    def drink(self, drink):
        self.thirst += drink.thirst
        self.potty_times +=1
        if self.potty_times >= 3:
            self.potty_clean = False

    def activity(self, activity):
        self.energy -= activity.energy
        self.bored -= activity.bored

    def time_tick(self):
        self.age += 0.1
        self.hunger -= 5
        self.thirst -= 3
        self.bored += 2

        if self.hunger < 50 or self.bored > 50 or self.thirst < 50:
            self.happiness -= 5
            self.in_need = True
        else:
            self.in_need = False

        if self.hunger <= 0 or self.bored >= 100 or self.thirst <= 0 or self.happiness <= 0:
            self.alive = False
         #   if potty_clean = false for more than 5 mins
          #         self.is_sick = True
           # if self.potty_clean = False:
            #    self.is_sick = True  
             #   if is_sick *for longer than ten mins*:
              #          self.alive = False
        # how do I keep track of how long pet it sick?
        #'''

    def get_status(self):
        status = f"""
Name: {self.name}
Age: {self.age:.2f}
Happiness: {self.happiness}
Hunger: {self.hunger}
Thirst: {self.thirst}
Bored: {self.bored}
Energy: {self.energy}
"""
        return status

    def draw(self):
        emoji_space_filler="      "
        if not self.potty_clean: potty = "💩" 
        else: potty = emoji_space_filler
        tamagotchi_outline = f"""
\n
🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
🌸{self.happiness_emoji}                                            🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                     {self.emoji}{potty}                       🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
{self.get_status()}
"""
        return tamagotchi_outline