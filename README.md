# 5E-Characters


### MVP:

Users are able to create and track the progress of a 5th edition character for Dungeons and Dragons. They will be able to save the data on the server or on their own computer, and be able to load those saved files back into the system.

---

### Specific Functionality:

###### Character Sheet:
1. Flair:
 * age
 * height
 * weight
 * eye color
 * skin color (?)
 * hair color
 * personality traits
 * ideals
 * bonds
 * flaws

* Base:
 * Class(es)
 * level
 * background
 * character name
 * player name
 * race
 * alignment
 * experience points
 * ability scores
 * savings throws
 * proficiency bonus
 * inspiration points
 * armor class
 * initiative bonus
 * speed
 * skills
 * hit dice
 * hp
 * passive perception
 * languages
 * other proficiencies

###### Battle Screen:
 * ac
 * ability scores + bonuses
 * savings throws
 * proficiency bonus
 * inspiration points
 * initiative
 * speed
 * hit dice
 * death saves
 * skills
 * spells
 * abilities
 * attacks
 * equipment
 * Pictographic Health Meter
  * include major damages (broken leg)
  * Includes effects such as disease, sleep, stun

###### Other Features:

* Built in leveling up
 * Auto calculate bonuses.

* Rest tracking

* Create a character:
 * Start from template
 * Make custom

* In-app customizable dice rolling

* Spell book

* Intuitive UX with drag and drop ability and customizable windows.

---

### Data Model:

* All Character Information:
 * As outlined above for character sheets and battle screens

* Rule set for 5th edition Dungeons and Dragons
* Spells
* Feats
* Equipment

---

### Technical Components:

* Nice front-end menu magic
* Traversing screens with ease.
* Ability to save and load files from device.
 * User accounts as extension.
 * Possibly save to an online library.
* May use OCR to get rule data (tesseract)

---

### Estimated Schedule:

###### Front End:
1. Initial front end layout - 1 day
* Character Sheet Screen
* Character Flair Screen
* Battle Manager Screen

###### Backend:
1. Tesseract OCR
* Character Model

---

### Functionality beyond the MVP (Future):

* User Accounts
* Save Online and Share system
 * Rate other characters
 * Artwork sharing platform
 * User generated spells, items, other content.
* 3-D Modeling for dice rolling
* Note making, with time-stamping
* NFC Loading
