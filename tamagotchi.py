class Tamagotchi:
    age = 0
    happiness = 100
    hunger = 100
    thirst = 100
    alive = True
    bored = 0
    energy = 100
    name = ''

    def __init__(self, emoji):
        self.emoji = emoji

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
        self.energy += 2

        if self.hunger < 50 or self.bored > 50 or self.thirst < 50:
            self.happiness -= 5

        

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
🌸                   {self.emoji}                         🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
{self.get_status()}
"""
        return tamagotchi_outline