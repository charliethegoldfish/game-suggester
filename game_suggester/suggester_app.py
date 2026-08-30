import sys
from PyQt6.QtCore import (QDir, Qt)
from PyQt6.QtWidgets import QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
from core.gamenode import GameNode
from core.core_config import *
from game_suggester.filtering_functions import filter_games
from game_suggester.pick_game_functions import pick_random_game
from core.gui_functions import init_widget_details

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
		game_details_layout = self.create_game_details_layout()

		main_layout = QVBoxLayout(self)
		main_layout.addLayout(top_layout)
		main_layout.addStretch(1)
		main_layout.addLayout(filter_layout)
		main_layout.addLayout(filter_display_layout)
		main_layout.addLayout(suggest_layout)
		main_layout.addLayout(game_details_layout)

		self.show()

	def create_combo_adder(self, items: list[str], name: str, tooltip: str, func: callable) -> QComboBox:
		combobox = QComboBox()
		init_widget_details(combobox, name, tooltip)
		combobox.addItems(items)
		combobox.textActivated.connect(func)
		func(combobox.currentText())
		return combobox

	def create_button(self, text: str, func: callable) -> QPushButton:
		button = QPushButton(text)
		button.pressed.connect(func)
		return button

	def create_genre_adder(self) -> QHBoxLayout:
		layout = QHBoxLayout()
		
		label = QLabel("Genres:")
		combobox = self.create_combo_adder(self._genres, "genre_combo", "Genres interested in", self.update_genre_combo)
		label.setBuddy(combobox)

		button_add = self.create_button("Add", self.add_genre)
		button_clear = self.create_button("Clear", self.clear_genres)

		layout.addWidget(label)
		layout.addWidget(combobox)
		layout.addWidget(button_add)
		layout.addWidget(button_clear)

		return layout

	def create_tag_adder(self) -> QHBoxLayout:
		layout = QHBoxLayout()
				
		label = QLabel("Tags:")
		combobox = self.create_combo_adder(self._tags, "tag_combo", "Tags interested in", self.update_tag_combo)
		label.setBuddy(combobox)

		button_add = self.create_button("Add", self.add_tag)
		button_clear = self.create_button("Clear", self.clear_tags)

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

	def create_game_detail(self, label_text: str, details_key: str) -> QHBoxLayout:
		heading = QLabel(label_text)
		detail_label = QLabel("")
		self._details_dict[details_key] = detail_label

		layout = QHBoxLayout()
		layout.addWidget(heading)
		layout.addWidget(detail_label)
		return layout

	def create_game_details_layout(self) -> QVBoxLayout:
		self._details_dict = {}

		name_layout = self.create_game_detail("Game to Play:", NAME_KEY)
		status_layout = self.create_game_detail("Status:", STATUS_KEY)
		genre_layout = self.create_game_detail("Genres:", GENRES_KEY)
		tag_layout = self.create_game_detail("Tags:", TAGS_KEY)
		store_layout = self.create_game_detail("You own it on:", STORES_KEY)

		game_details_layout = QVBoxLayout()
		game_details_layout.addLayout(name_layout)
		game_details_layout.addLayout(status_layout)
		game_details_layout.addLayout(genre_layout)
		game_details_layout.addLayout(tag_layout)
		game_details_layout.addLayout(store_layout)

		return game_details_layout

	# @Slot(str)
	def update_genre_combo(self, genre):
		self._genre_highlighted = genre

	def update_tag_combo(self, tag):
		self._tag_highlighted = tag

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

		self.update_details(game_suggestion, self._details_dict)

	def update_details(self, game: GameNode, detail_labels: dict[str, QLabel]):
		if game == None:
			for key in detail_labels:
				if key == NAME_KEY:
					detail_labels[key].setText("No suitable game!")
				else:
					detail_labels[key].setText("")
		else:
			details = game.get_csv_dict()

			for key in detail_labels:
				if key in details:
					detail_labels[key].setText(details[key])
				else:
					detail_labels[key].setText("")
