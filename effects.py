from PyQt5 import QtGui, QtCore, QtWidgets
import time

class Effects(QtCore.QThread):

	effectType = None
	elem = None

	def __init__(self, effect, elem):
		super(Effects, self).__init__()
		self.effectType = effect
		self.elem = elem

	def warning_highlight(self):
		self.elem.setStyleSheet('color: #FF0000')
		time.sleep(0.1)
		self.elem.setStyleSheet('color: #000000')

	def run(self):
		if self.effectType == 'warning-highlight':
			self.warning_highlight()