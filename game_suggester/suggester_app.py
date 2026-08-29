import sys
from PyQt6.QtCore import (QDir, Qt)
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox, QPushButton
from PyQt6.QtGui import QIcon
from core.gamenode import GameNode

def init_widget_details(widget: QWidget, name: str, tooltip: str):
	widget.setObjectName(name)
	widget.setToolTip(tooltip)

class SuggesterApp(QWidget):
	def __init__(self, game_nodes: list[GameNode], genres: list[str], platforms: list[str], status_options: list[str], tags: list[str], verbose):
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

		self._selected_genres = []
		self._selected_tags = []

		self._verbose = verbose

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
		# self._genre_checkbox_grid = self.create_checkbox_grid(self._genres, "Genres:")
		self._genre_layout = self.create_genre_adder()

		# Setup grid of tag checkboxes
		# self._tag_checkbox_grid = self.create_checkbox_grid(self._tags, "Tags:")
		self._tags_layout = self.create_tag_adder()

		filter_layout = QHBoxLayout()
		# bottom_layout.addLayout(self._genre_checkbox_grid)
		# bottom_layout.addStretch(1)
		# bottom_layout.addLayout(self._tag_checkbox_grid)
		filter_layout.addLayout(self._genre_layout)
		filter_layout.addStretch(1)
		filter_layout.addLayout(self._tags_layout)

		filter_display_layout = QHBoxLayout()

		self._genre_display_grid, self._genre_display_dict = self.create_filter_display_grid("Genres to include:", self._genres)
		self._tags_display_grid, self._tags_display_dict = self.create_filter_display_grid("Tags to include:", self._tags)

		filter_display_layout.addLayout(self._genre_display_grid)
		filter_display_layout.addLayout(self._tags_display_grid)


		main_layout = QVBoxLayout(self)
		main_layout.addLayout(top_layout)
		main_layout.addStretch(1)
		main_layout.addLayout(filter_layout)
		main_layout.addLayout(filter_display_layout)


		self.show()

	def create_filter_adder(self, items: list[str], name: str, tooltip: str, combo_func: callable) -> QHBoxLayout:
		layout = QHBoxLayout()

		label = QLabel(name)
		combobox = QComboBox()
		init_widget_details(combobox, name, tooltip)
		combobox.addItems(items)
		combobox.textActivated.connect(combo_func)

		button_add = QPushButton("Add")
		button_clear = QPushButton("Clear")

		layout.addWidget(label)
		layout.addWidget(combobox)
		layout.addWidget(button_add)
		layout.addWidget(button_clear)

		return layout

	def create_genre_adder(self) -> QHBoxLayout:
		layout = QHBoxLayout()
		
		label = QLabel("Genres:")
		combobox = QComboBox()
		label.setBuddy(combobox)
		init_widget_details(combobox, "genre_combo", "Genres interested in")
		combobox.addItems(self._genres)
		combobox.textActivated.connect(self.update_genre_combo)
		self.update_genre_combo(combobox.currentText())

		button_add = QPushButton("Add")
		button_add.pressed.connect(self.add_genre)
		button_clear = QPushButton("Clear")
		button_clear.pressed.connect(self.clear_genres)

		layout.addWidget(label)
		layout.addWidget(combobox)
		layout.addWidget(button_add)
		layout.addWidget(button_clear)

		return layout

	def create_tag_adder(self) -> QHBoxLayout:
		layout = QHBoxLayout()
				
		label = QLabel("Tags:")
		combobox = QComboBox()
		label.setBuddy(combobox)
		init_widget_details(combobox, "tag_combo", "Tags interested in")
		combobox.addItems(self._tags)
		combobox.textActivated.connect(self.update_tag_combo)
		self.update_tag_combo(combobox.currentText())

		button_add = QPushButton("Add")
		button_add.pressed.connect(self.add_tag)
		button_clear = QPushButton("Clear")
		button_clear.pressed.connect(self.clear_tags)

		layout.addWidget(label)
		layout.addWidget(combobox)
		layout.addWidget(button_add)
		layout.addWidget(button_clear)

		return layout

	def create_filter_display_grid(self, name: str, items: list[str]) -> tuple[QGridLayout, dict[str, QLabel]]:
		grid = QGridLayout()

		label = QLabel(name)
		grid.addWidget(label, 0, 0)

		display_dict = {}

		row = 1
		column = 0
		for item in items:
			item_label = QLabel(item)
			grid.addWidget(item_label, row, column)
			item_label.setEnabled(False)

			display_dict[item] = item_label

			if column == 2:
				row += 1
				column = 0
			else:
				column += 1

		return grid, display_dict

	def get_tag_combo(self) -> QComboBox:
		combobox = QComboBox()
		init_widget_details("tag_combo", "Tags interested in")
		combobox.addItems(self._tags)
		combobox.textActivated.connect(self.update_tag_combo)
		self._tag_highlighted = combobox.currentText
		return combobox

	# @Slot(str)
	def update_genre_combo(self, genre):
		self._genre_highlighted = genre
		# print(genre)

	def update_tag_combo(self, tag):
		self._tag_highlighted = tag
		# print(tag)

	def add_genre(self):
		genre = self._genre_highlighted

		if genre in self._selected_genres:
			return

		self._selected_genres.append(genre)
		self.update_display(self._genre_display_dict, genre)
		if self._verbose:
			print(f'Adding genre: {genre}')

	def add_tag(self):
		tag = self._tag_highlighted

		if tag in self._selected_tags:
			return

		self._selected_tags.append(tag)
		self.update_display(self._tags_display_dict, tag)
		if self._verbose:
			print(f'Adding tag: {tag}')

	def clear_genres(self):
		self._selected_genres = []
		self.clear_display(self._genre_display_dict)

	def clear_tags(self):
		self._selected_tags = []
		self.clear_display(self._tags_display_dict)

	def update_display(self, display_dict: dict[str, QLabel], item: str):
		label = display_dict[item]
		label.setEnabled(True)

	def clear_display(self, display_dict: dict[str, QLabel]):
		for key in display_dict:
			label = display_dict[key]
			label.setEnabled(False)
