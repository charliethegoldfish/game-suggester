import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon

class SuggesterApp(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'Game Suggester'
		self.left = 200
		self.top = 100
		self.width = 400
		self.height = 200
		self.init_ui()

	def init_ui(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.show()