import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon

def init_widget_details(widget: QWidget, name: str, tooltip: str):
	widget.setObjectName(name)
	widget.setToolTip(tooltip)

class SuggesterApp(QWidget):
	def __init__(self, genres: list[str], platforms: list[str], status_options: list[str], tags: list[str]):
		super().__init__()
		self.title = 'Game Suggester'
		self.left = 200
		self.top = 100
		self.width = 400
		self.height = 200

		self._genres = genres
		self._platforms = platforms
		self._status_options = status_options
		self._tags = tags

		self.init_ui()

	def init_ui(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		# Setup platform combo box

		# Setup status combo box

		# Setup grid of genre checkboxes

		# Setup grid of tag checkboxes

		self.show()

	