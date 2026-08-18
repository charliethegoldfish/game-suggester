---
aliases:
tags:
  - "#remedy"
genre:
  - Shooter
  - Adventure
released: 2012
platform:
  - Windows - PC
store:
  - Steam
status: Completed
hours-logged: 3
image: "[[IMG-20260107162711776.png]]"
related-games:
  - "[[Alan Wake]]"
---
# Alan Wakes American Nightmare



![[IMG-20260107162711776.png]]

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
