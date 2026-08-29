import sys
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
from PyQt6.QtGui import QIcon
from core.gamenode import GameNode

def init_widget_details(widget: QWidget, name: str, tooltip: str):
	widget.setObjectName(name)
	widget.setToolTip(tooltip)

class SuggesterApp(QWidget):
	def __init__(self, game_nodes: list[GameNode], genres: list[str], platforms: list[str], status_options: list[str], tags: list[str]):
		super().__init__()
		self.title = 'Game Suggester'
		self.left = 200
		self.top = 100
		self.width = 400
		self.height = 200

		self._game_nodes = game_nodes
		self._genres = genres
		self._platforms = platforms
		self._status_options = status_options
		self._tags = tags

		self.init_ui()

	def init_ui(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		# Setup platform combo box
		self._platform_combobox = QComboBox()
		init_widget_details(self._platform_combobox, "platformComboBox", "Platform you want to play on")
		self._platform_combobox.addItems(self._platforms)

		platform_label = QLabel("Platform:")
		platform_label.setBuddy(self._platform_combobox)

		# Setup status combo box
		self._status_combobox = QComboBox()
		init_widget_details(self._status_combobox, "statusComboBox", "Status of game you want to play")
		self._status_combobox.addItems(self._status_options)

		status_label = QLabel("Status:")
		status_label.setBuddy(self._status_combobox)

		top_layout = QHBoxLayout()
		top_layout.addWidget(platform_label)
		top_layout.addWidget(self._platform_combobox)
		top_layout.addStretch(1)
		top_layout.addWidget(status_label)
		top_layout.addWidget(self._status_combobox)

		# Setup grid of genre checkboxes
		genre_checkbox_grid = self.create_checkbox_grid(self._genres, "Genres:")

		# Setup grid of tag checkboxes
		tag_checkbox_grid = self.create_checkbox_grid(self._tags, "Tags:")

		bottom_layout = QHBoxLayout()
		bottom_layout.addLayout(genre_checkbox_grid)
		# bottom_layout.addStretch(1)
		bottom_layout.addLayout(tag_checkbox_grid)

		main_layout = QVBoxLayout(self)
		main_layout.addLayout(top_layout)
		main_layout.addStretch(1)
		main_layout.addLayout(bottom_layout)


		self.show()

	def create_checkbox_grid(self, items: list[str], name: str) -> QGridLayout:
		grid_layout = QGridLayout()

		label = QLabel(name)
		grid_layout.addWidget(label, 0, 0)

		row = 1
		column = 0

		for item in items:
			checkbox = QCheckBox(item)
			grid_layout.addWidget(checkbox, row, column)

			if column == 2:
				row += 1
				column = 0
			else:
				column += 1

		return grid_layout

	