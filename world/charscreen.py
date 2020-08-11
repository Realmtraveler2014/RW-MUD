# Questions

def qRace(caller)

	text = "Choose your race:"

	options = (
		{"desc": "Slugcat",
		 "goto": "rememberRace"},
		{"desc": "Scavenger",
		 "goto": "rememberRace"},
		{"desc": "Lizard",
		 "goto": "rememberRace"}
		)


	return text, options

def setAtt(caller)
	
	


# Counting menues

def rememberRace(caller, raw_string)
	
	if raw_string == "1":

		caller.ndb.tempRace = "Slugcat"

		#Stats

		caller.ndb.tempStr = 2
		caller.ndb.tempDex = 5
		caller.ndb.tempInt = 3
		caller.ndb.tempCon = 2


		#text

		text = "Slugcats are agile and cunning creatures that roam around this world. Due to their nomadic lifestyle they are masters at navigating this world. Do you wish to choose this race?"

	elif raw_string == "2":

		caller.ndb.tempRace = "Scavenger"

		#Stats

		caller.ndb.tempStr = 1
		caller.ndb.tempDex = 3
		caller.ndb.tempInt = 6
		caller.ndb.tempCon = 2


		#text

		text = "Scavengers are the smartest creatures. They live in groups and are able to craft more advanced tools. Do you wish to choose this race?"

	elif raw_string == "3":

		caller.ndb.tempRace = "Lizard"

		#Stats

		caller.ndb.tempStr = 5
		caller.ndb.tempDex = 1
		caller.ndb.tempInt = 1
		caller.ndb.tempCon = 5


		#text

		text = "Lizards are natural predators that often fight each other. What they lack in intellect and agility they make up in raw strength and toughness. Do you wish to choose this race?"

	opinions = (
		{"desc": = "Confirm",
		 "goto": = "setAtt"},
		{"desc": = "Back",
		 "goto": = "qRace"}
		)

	return text, options
