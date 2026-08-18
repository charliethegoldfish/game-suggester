import unittest

from test_config import MD_SNIPPET_WITH_YAML, MD_SNIPPET_NO_YAML, YAML_SNIPPET
from extract_functions import extract_yaml_from_md

class TestExtractYamlFromMd(unittest.TestCase):
	def test_extract_yaml_from_md(self):
		md = MD_SNIPPET_WITH_YAML
		yaml = extract_yaml_from_md(md)
		self.assertEqual(yaml, YAML_SNIPPET)

	def test_extract_yaml_from_md_no_yaml(self):
		md = MD_SNIPPET_NO_YAML
		yaml = extract_yaml_from_md(md)
		self.assertEqual(yaml, "")

if __name__ == "__main__":
	unittest.main()