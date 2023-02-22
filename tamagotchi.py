class Tamagotchi:
    age = 0
    happiness: int = 100
    hunger: int = 100
    thirst: int = 100
    alive = True
    bored: int = 0
    energy: int = 100
    name = ''


    def num_limit(num, minimum=0, maximum=100):
        """Limits input 'num' between minimum and maximum values.
        Default minimum value is 1 and maximum value is 255."""
        return max(min(num, maximum), minimum)

    def __init__(self, emoji):
        self.emoji = emoji
        var_list = [self.age, self.happiness, self.hunger, self.thirst, self.bored, self.energy]
        map(self.num_limit(), var_list)

    def eating(self, food):
        self.hunger += food.hunger

    def drinking(self, drink):
        self.thirst += drink.thirst

    def activity(self, activity):
        self.energy -= activity.energy
        self.bored -= activity.bored

    def time_tick(self):
        self.age += 0.1
        self.hunger -= 5
        self.thirst -= 3
        self.bored += 2
        if self.energy <= 100: self.energy += 2

        if self.hunger < 50 or self.bored > 50 or self.thirst < 50:
            self.happiness -= 5

        if self.hunger < 0 or self.bored > 100 or self.thirst < 0 or self.happiness < 0:
            self.alive = False
        

    def get_status(self):
        status = f"""
Name: {self.name}
Age: {self.age}
Happiness: {self.happiness}
Hunger: {self.hunger}
Thirst: {self.thirst}
Bored: {self.bored}
Energy: {self.energy}
"""
        return status

    def draw(self):
        tamagotchi_outline = f"""
\n
🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                     {self.emoji}                       🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
{self.get_status()}
"""
        return tamagotchi_outline