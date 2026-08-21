# General test data cond config values

YAML_SNIPPET = """
aliases:
tags:
  - "#remedy"
genre:
  - Shooter
  - Adventure
released: 2010
platform:
  - Windows - PC
store:
  - Steam
status: Completed
hours-logged: 11.5
image: "[[IMG-20260107162554393.png]]"
related-games:
"""

MD_SNIPPET_WITH_YAML = """
---
aliases:
tags:
  - "#remedy"
genre:
  - Shooter
  - Adventure
released: 2010
platform:
  - Windows - PC
store:
  - Steam
status: Completed
hours-logged: 11.5
image: "[[IMG-20260107162554393.png]]"
related-games:
---
# Alan Wake



![[IMG-20260107162554393.png]]
"""

MD_SNIPPET_NO_YAML = """
# Alan Wake



![[IMG-20260107162554393.png]]
"""