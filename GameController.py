from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Controller:

	playerTurn = 1
	playerSymbol = {1: 'X', 2: 'O'}
	logicPlaces = []
	combinations = ['00|11|22', '02|11|20', '01|11|21', '02|12|22', '00|10|20', '10|11|12', '00|01|02', '20|21|22']

	def __init__(self):
		self.logicPlaces = [['' for x in range(3)] for y in range(3)]

	def setAValue(self, interface, elem, place):
		value = self.playerSymbol[self.playerTurn]

		x = place['x']
		y = place['y']

		if self.logicPlaces[x][y] != '':
			return 'Fail'


		self.logicPlaces[x][y] = value

		result = self.checkIfWin()

		self.playerTurn = 2 if self.playerTurn == 1 else 1
		elem.setText(value)
		interface.player_turn = self.playerTurn
		
		if result[0] == 0:
			return 'O jogador ' + str(result[1]) + ' venceu!'
		elif result[0] == 1:
			return 'Deu velha'
		else:
			return 'Next'


	def checkIfWin(self):
		hasWinner = False
		tied = False
		allFilled = False

		for i, x in enumerate(self.logicPlaces):
			try:
				self.logicPlaces[i].index('')
				allFilled = False
				break
			except ValueError:
				allFilled = True

		for seq in self.combinations:
			state = ''

			for ind in seq.split('|'):
				if self.logicPlaces[int(ind[0])][int(ind[1])] == self.playerSymbol[self.playerTurn]:
					state += 'T'
				else:
					state += 'F' 
					break 

			if state == 'TTT':
				hasWinner = True 
				break

		if not hasWinner and allFilled:
			tied = True

		if hasWinner:
			return [0, self.playerTurn]
		elif tied:
			return [1]
		else: 
			return [2]

	def showState(self):
		for i,x in enumerate(self.logicPlaces):
			for y in self.logicPlaces[i]:
				print(y, end='\t')
			print('\n')

