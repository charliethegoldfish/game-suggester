---
aliases:
tags:
  - "#play-next"
  - "#remedy"
genre:
  - Shooter
  - Adventure
released: 2023
platform:
  - Xbox Series X
store:
  - Xbox
status: Playing
hours-logged: 1
image: "[[IMG-20260107162927686.png]]"
related-games:
  - "[[Alan Wake]]"
  - "[[Alan Wakes American Nightmare]]"
---
# Alan Wake II



![[IMG-20260107162927686.png]]

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
