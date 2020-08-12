import evennia
import random

def chooseSpawnZone(caller):

	text = "Choose your spawn zone:"

	options = (
		{"desc": "Outskirts",
		 "goto": "setSpawnZone"},
		{"desc": "Farm Arrays",
		 "goto": "setSpawnZone"},
		{"desc": "Garbage Wastes",
		 "goto": "setSpawnZone"}
		)


	return text, options

def setSpawnZone(caller, raw_string):

	if raw_string == "1":
		caller.ndb.chosenSpawnZone = "outskirts"
	elif raw_string == "2":
		caller.ndb.chosenSpawnZone = "farmarrays"
	elif raw_string == "3":
		caller.ndb.chosenSpawnZone = "garbagewastes"

	spawnRoomList = evennia.search_tag(caller.ndb.chosenSpawnZone, category="locations")
	spawnRoom = random.choice(spawnRoomList)
	caller.move_to(spawnRoom)
	caller.home = spawnRoom

	text = "Processing..."

	return text