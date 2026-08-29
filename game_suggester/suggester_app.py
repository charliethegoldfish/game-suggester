import sys
from PyQt6.QtCore import (QDir, Qt)
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox, QPushButton
from PyQt6.QtGui import QIcon
from core.gamenode import GameNode
from core.core_config import *
from game_suggester.filtering_functions import filter_games
from game_suggester.pick_game_functions import pick_random_game

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

		# Setup genres
		self._genre_layout = self.create_genre_adder()

		# Setup tags
		self._tags_layout = self.create_tag_adder()

		filter_layout = QHBoxLayout()
		filter_layout.addLayout(self._genre_layout)
		filter_layout.addStretch(1)
		filter_layout.addLayout(self._tags_layout)

		filter_display_layout = QHBoxLayout()

		self._genre_display_grid, self._genre_display_dict = self.create_filter_display_grid("Genres to include:", self._genres)
		self._tags_display_grid, self._tags_display_dict = self.create_filter_display_grid("Tags to include:", self._tags)

		filter_display_layout.addLayout(self._genre_display_grid)
		filter_display_layout.addLayout(self._tags_display_grid)

		suggest_layout = QHBoxLayout()
		self._suggest_button = QPushButton("Suggest a Game")
		self._suggest_button.pressed.connect(self.suggest_game)
		suggest_layout.addWidget(self._suggest_button)

		# Game Details

		name_heading = QLabel("Game To Play")
		self._details_name = QLabel("")
		name_layout = QHBoxLayout()
		name_layout.addWidget(name_heading)
		name_layout.addWidget(self._details_name)

		status_heading = QLabel("Status:")
		self._details_status = QLabel("")
		status_layout = QHBoxLayout()
		status_layout.addWidget(status_heading)
		status_layout.addWidget(self._details_status)

		genre_heading = QLabel("Genres:")
		self._details_genres = QLabel("")
		genre_layout = QHBoxLayout()
		genre_layout.addWidget(genre_heading)
		genre_layout.addWidget(self._details_genres)

		tag_heading = QLabel("Tags:")
		self._details_tags = QLabel("")
		tag_layout = QHBoxLayout()
		tag_layout.addWidget(tag_heading)
		tag_layout.addWidget(self._details_tags)

		store_heading = QLabel("You own it on:")
		self._details_stores = QLabel("")
		store_layout = QHBoxLayout()
		store_layout.addWidget(store_heading)
		store_layout.addWidget(self._details_stores)

		game_details_layout = QVBoxLayout()
		game_details_layout.addLayout(name_layout)
		game_details_layout.addLayout(status_layout)
		game_details_layout.addLayout(genre_layout)
		game_details_layout.addLayout(tag_layout)
		game_details_layout.addLayout(store_layout)

		main_layout = QVBoxLayout(self)
		main_layout.addLayout(top_layout)
		main_layout.addStretch(1)
		main_layout.addLayout(filter_layout)
		main_layout.addLayout(filter_display_layout)
		main_layout.addLayout(suggest_layout)
		main_layout.addLayout(game_details_layout)


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

	def suggest_game(self):
		platform = self._platform_combobox.currentText()
		status = self._status_combobox.currentText()
		genres = self._selected_genres
		tags = self._selected_tags
		games = self._game_nodes

		filtered_games = filter_games(games, platform, status, genres, tags)
		game_suggestion = pick_random_game(filtered_games)

		if self._verbose:
			print("Suggesting game...")
			print(f"Platform {platform} with a status of {status}")
			print(f"Following genres: {genres}")
			print(f"Following tags: {tags}")
			print("Game to play:")
			if game_suggestion == None:
				print("No game meets the criteria!")
			else:
				print(game_suggestion.get_csv_dict())

		if game_suggestion == None:
			self._details_name.setText("No suitable game!")
			self._details_status.setText("")
			self._details_genres.setText("")
			self._details_tags.setText("")
			self._details_stores.setText("")
		else:
			details = game_suggestion.get_csv_dict()
			self._details_name.setText(details[NAME_KEY])
			self._details_status.setText(details[STATUS_KEY])
			self._details_genres.setText(details[GENRES_KEY])
			self._details_tags.setText(details[TAGS_KEY])
			self._details_stores.setText(details[STORES_KEY])
