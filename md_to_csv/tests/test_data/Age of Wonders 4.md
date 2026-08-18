---
aliases:
tags:
genre:
  - Strategy
  - TBS
released: 2023
platform:
  - Windows - PC
store:
  - Steam
status: Ongoing
hours-logged: 1
image: "[[IMG-20260106095229694.png]]"
related-games:
---
# Age of Wonders 4



![[IMG-20260106095229694.png]]

# Related Games
```base
filters:
  and:
    - file.inFolder("02 Library")
    - or:
	    - file.hasLink(this.file)
		- this.file.hasLink(file)
properties:
  note.status:
    displayName: Status
  note.hours-logged:
    displayName: Time
views:
  - type: cards
    name: Card View
    order:
      - file.name
      - genre
      - status
    image: note.image
    imageAspectRatio: 1.5

```
