from core.gamenode import GameNode

class YamlNode(GameNode):
	def __init__(self, name: str, raw_yaml: str):
		super().__init__(name)
		self.raw_yaml = raw_yaml

	def get_raw_yaml(self) -> str:
		return self.raw_yaml