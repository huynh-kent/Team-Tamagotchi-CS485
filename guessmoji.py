import random

word_set = { 'π₯π₯': 'hotpotato',
             'πΆπΏ': 'babyshower',
             'π½π' : 'cornbread',
             'ππ₯§':'applepie',
             'π§ β°οΈ':'braindead',
             'π¦·π§π»':'toothfairy',
             'π¦»π':'earring',
             'π¨βπ³π§':'cookie',
             'π½π§':'alienjuice',
             'π­π²':'imaginedragons',
             'π±π ':'catfish',
             'ππ':'tulips',
             'ππ':'beliefs',
             'πΈοΈποΈ':'website',
             'πͺΆποΈββοΈ':'featherweight',
             'βοΈπ':'cutties',
             'ππ§':'seasalt',
             'β·οΈπ·':'skimask',
             'π₯ποΈ':'goldenticket',
             'πβ£οΈ':'nightclub',
             'π«ΆβοΈ':'loveletter',
             'ππ»':'ringbearer',
             'β­οΈπ ':'starfish',
             'π‘π ':'lighthouse',
             'π½π':'toiletpaper',
             '4οΈβ£ππ':'france',
             'πππ£οΈ':'beyonce',
             'π° πΈ':'newsflash',
             'ππ§':'antman',
             'ππ':'pizzahut',
             }

class Guessmoji:
    current_word = ''
    current_answer = ''

    def __init__(self):
        self.word_pool = word_set
        self.score = 0

    def select_word(self):
        self.current_word = random.choice(list(self.word_pool))
        #self.current_word = word
        #print(word)
        self.current_answer = self.word_pool.pop(self.current_word)
        #print(answer)

        return self.current_word, self.current_answer
    
    def check_guess(self, guess):
        guess = guess.replace(' ','')
        if guess.lower() == self.current_answer:
            self.score += 1
            return True
        return False
    
#game = Guessmoji()
#game.select_word()