import evennia
import random
from evennia import DefaultRoom
from evennia import search_object
from evennia.utils import inherits_from
from evennia.utils.create import create_object
from evennia.utils.utils import list_to_string
from evennia.utils import search

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

	# Choosing room
	spawnRoomList = evennia.search_tag(caller.ndb.chosenSpawnZone, category="locations")
	spawnRoom = random.choice(spawnRoomList)
	# Creating Shelter and exits
	playerRoom = create_object(typeclass="typeclasses.rooms.shelterRoom", key="Shelter")
	exitFromPlayerRoom = create_object(typeclass="typeclasses.exits.Exit", key="out", destination=spawnRoom, location=playerRoom, home=playerRoom)
	# Saves shelter id and location to player
	caller.db.shelter = playerRoom
	caller.db.shelterId = playerRoom.id
	caller.db.shelterLocationId = spawnRoom.id
	caller.db.shelterLocation = spawnRoom.location
	if spawnRoom.search("shelter") == None:
		exitToShelter = create_object(typeclass="typeclasses.exits.shelterExit", key="shelter", destination=playerRoom, location=spawnRoom, home=spawnRoom)
	# Saving exits and owner info on shelters database
	playerRoom.db.exitFromShelter = exitFromPlayerRoom
	playerRoom.db.theOwner = caller
	# Moving player to Shelter
	caller.move_to(playerRoom)
	caller.home = playerRoom

	text = "Processing..."

	return text