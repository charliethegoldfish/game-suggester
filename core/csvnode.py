from core.gamenode import GameNode

class CsvNode(GameNode):
	def __init__(self, name: str, csv_dict: dict):
		super().__init__(name)
		self.csv_dict = csv_dict

	def get_csv_dict(self):
		return self.csv_dict