import random

word_set = { '🔥🥔': 'hotpotato',
             '👶🚿': 'babyshower',
             '🌽🍞' : 'cornbread',
             '🍎🥧':'applepie',
             '🧠⚰️':'braindead',
             '🦷🧚🏻':'toothfairy',
             '🦻💍':'earring',
             '👨‍🍳📧':'cookie',
             '👽🧃':'alienjuice',
             '💭🐲':'imaginedragons',
             '🐱🐠':'catfish',
             '👄👄':'tulips',
             '🐝🍃':'beliefs',
             '🕸️👁️':'website',
             '🪶🏋️‍♂️':'featherweight',
             '✂️👔':'cutties',
             '🌊🧂':'seasalt',
             '⛷️😷':'skimask',
             '🥇🎟️':'golden ticket',
             '🌃♣️':'nightclub',
             '🫶✉️':'loveletter',
             '💍🐻':'ringbearer',
             '⭐️🐠':'starfish',
             '💡🏠':'lighthouse',
             '🚽📝':'toiletpaper',
             '4️⃣🐜🐜':'france',
             '🐝🔛🗣️':'beyonce',
             '📰 📸':'newsflash',
             '🐜🧔':'antman',
             '🍕🛖':'pizzahut',
             }

class Guessmoji:
    current_word = ''
    current_answer = ''

    def __init__(self):
        self.word_pool = word_set
        self.score = 0

    def select_word(self):
        word = random.choice(list(self.word_pool))
        print(word)
        answer = self.word_pool.pop(word)
        print(answer)

        return word, answer
    
    def check_guess(self, guess):
        guess = guess.replace(' ','')
        if guess.lower() == self.current_answer:
            self.score += 1
            return True
        return False
    
#game = Guessmoji()
#game.select_word()