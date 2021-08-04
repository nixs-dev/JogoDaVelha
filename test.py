from GameController import Controller

c = Controller()

while True:
	param = {'x': int(input('X:')), 'y': int(input('Y:'))}
	c.setAValue(param)
	c.showState()