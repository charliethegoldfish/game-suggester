import unittest

from test_config import MD_SNIPPET_WITH_YAML, MD_SNIPPET_NO_YAML, YAML_SNIPPET
from md_to_csv.extract_functions import extract_yaml_from_md, extract_name_from_filename

class TestExtractFunctions(unittest.TestCase):
	def test_extract_yaml_from_md(self):
		md = MD_SNIPPET_WITH_YAML
		yaml = extract_yaml_from_md(md)
		self.assertEqual(yaml, YAML_SNIPPET)

	def test_extract_yaml_from_md_no_yaml(self):
		md = MD_SNIPPET_NO_YAML
		yaml = extract_yaml_from_md(md)
		self.assertEqual(yaml, "")

	def test_extract_name_from_filename(self):
		filename = "Alan Wake.md"
		name = extract_name_from_filename(filename)
		self.assertEqual(name, "Alan Wake")

if __name__ == "__main__":
	unittest.main()