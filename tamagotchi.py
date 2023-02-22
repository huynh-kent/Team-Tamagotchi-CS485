import os
import time
import sched
import threading

class Tamagotchi:
    age = 0
    happiness = 0
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

    def time_passed(self):
        self.age += 0.1
        self.hunger -= 5
        self.thirst -= 3
        self.bored += 2

    def get_status(self):
        status = f"""
        {self.emoji}
        Name: {self.name}
        Age: {self.age}
        Happiness: {self.happiness}
        Hunger: {self.hunger}
        Thirst: {self.thirst}
        Bored: {self.bored}
        Energy: {self.energy}
        """
        return status

def get_outline():
    # tamagotchi outline
    tamagotchi_outline = """

              🌸🌸🌸🌸🌸🌸
         🌸🌸🌸🌸🌸🌸🌸🌸
      🌸🌸🌸🌸🌸🌸🌸🌸🌸
   🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
🌸                                                  🌸
   🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
      🌸🌸🌸🌸🌸🌸🌸🌸🌸
         🌸🌸🌸🌸🌸🌸🌸🌸
              🌸🌸🌸🌸🌸🌸
"""
    return tamagotchi_outline