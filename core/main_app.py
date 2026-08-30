from PyQt6.QtCore import (QDir, Qt)
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QProgressBar
from core.gui_functions import embed_into_hbox_layout
from md_to_csv.converter import converter

class MainApp(QWidget):
	def __init__(self, verbose):
		super().__init__()
		self.title = 'Game Library Tool'
		self.left = 200
		self.top = 100
		self.width = 400
		self.height = 200

		self._verbose = verbose

		self.init_ui()
		self.show()

	def init_ui(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		converter_layout = self.create_game_converter_layout()
		

		main_layout = QVBoxLayout(self)
		main_layout.addLayout(converter_layout)

	def create_folder_path_section(self) -> QHBoxLayout:
		layout = QHBoxLayout()

		# TODO: Have it remember the last used whatever
		self._folder_path = QLineEdit("")
		button = QPushButton("Browse")
		button.pressed.connect(self.browse_for_folder)

		layout.addWidget(self._folder_path)
		layout.addWidget(button)

		return layout

	def create_game_converter_layout(self) -> QVBoxLayout:
		layout = QVBoxLayout()
		heading = QLabel("Convert Obsidian Library to CSV")

		select_folder_layout = self.create_folder_path_section()

		convert_button = QPushButton("Convert to CSV")
		convert_button.pressed.connect(self.convert_to_csv)

		self._progress_bar = QProgressBar()

		layout.addWidget(heading)
		layout.setAlignment(heading, Qt.AlignmentFlag.AlignHCenter)
		layout.addLayout(select_folder_layout)
		layout.addWidget(convert_button)
		layout.addWidget(self._progress_bar)

		return layout

	def browse_for_folder(self):
		dialog = QFileDialog(self)
		dialog.setFileMode(QFileDialog.FileMode.Directory)
		if dialog.exec():
			selection = dialog.selectedFiles()
			if len(selection) > 0:
				folder = selection[0]
				self._folder_path.setText(folder)

	def convert_to_csv(self):
		folder_path = self._folder_path.text()
		if folder_path != "":
			converter(folder_path, self._verbose)
