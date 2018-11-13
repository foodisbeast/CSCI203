#
# hw8pr2.py
#
# Name: Brian Richardson
#
import random
class master():
	def __init__(self):
		self.newGame()
	def newGame(self):
		print("Welcome to Mastermind!")
		print("----------------------")
		self.holes = int(input("How many holes per row? "))
		self.rounds = int(input("How many rounds? "))
		self.colors = int(input("How many colors shall we have? "))
		self.key = [random.randrange(self.colors) for _ in range(self.holes)]
		#DEBUG: self.key = [i for i in range(self.holes)]
		self.turns = []
		while (self.checkWin() == False and len(self.turns) < self.rounds):
			self.guess()
			self.output()
		if self.checkWin():
			self.winGame()
			self.playAgain()
		else:
			self.loseGame()
			self.playAgain()
	def guess(self):
		turn = []
		for i,_ in enumerate(self.key):
			out = ("Enter guess for hole %d: " % i)
			guess = int(input(out))
			turn.append(guess)
		self.turns.append(turn)
	def output(self):
		#score & output rounds
		out = "===START BOARD===\n"
		for rnd,turn in enumerate(self.turns):
			b = 0 #black score
			w = 0 #white score
			#calculate black score
			for i,e in enumerate(turn):
				if e == self.key[i]:
					b += 1
			#calculate white score
			cSum = 0
			for c in range(self.colors):
				cGuess = self.turns[-1].count(c)
				cKey = self.key.count(c)
				cSum += min(cGuess,cKey)
			w = cSum - b
			#Output
			out += ("Round %d %s Score: %d black and %d white\n" \
				% (rnd + 1, turn, b, w))
		out += "====END BOARD===="
		print(out)
	def checkWin(self):
		if len(self.turns) > 0:
			return self.turns[-1] == self.key
		else:
			return False
	def winGame(self):
		print("You won in %d rounds!" % len(self.turns))
	def playAgain(self):
		again = input("Would you like to play again (y/n)? ")
		if again == 'y':
			self.newGame()
		else:
			print('Bye')
	def loseGame(self):
		out = ("You lose!\nYou couldnt guess: %s in %d rounds" % (self.key,self.rounds))
		print(out)