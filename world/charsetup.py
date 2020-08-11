# Questions

def qRace(caller):

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

# Attribute confirmation

def confirmAtt(caller, raw_string):

	



	if caller.ndb.tempRace == "slugcat":

		if raw_string == "1":

			caller.ndb.tempStrMod += 1

		elif raw_string == "2":

			caller.ndb.tempIntMod += 1

		caller.ndb.statTotalStr = caller.ndb.tempStr + caller.ndb.tempStrMod
		caller.ndb.statTotalDex = caller.ndb.tempDex + caller.ndb.tempDexMod
		caller.ndb.statTotalInt = caller.ndb.tempInt + caller.ndb.tempIntMod
		caller.ndb.statTotalCon = caller.ndb.tempCon + caller.ndb.tempConMod

		text = "You are a " + caller.ndb.tempRace + ". Your stats are: Str " + str(caller.ndb.statTotalStr) + ", Dex " + str(caller.ndb.statTotalDex) + ", Con " + str(caller.ndb.statTotalCon) + ", Int " + str(caller.ndb.statTotalInt) + ". Are these correct?"

		options = (
			{"desc": "Confirm",
			 "goto": "setAttributes"},
			{"desc": "Restart",
			 "goto": "qRace"}
			)

	elif caller.ndb.tempRace == "scavenger":

		if raw_string == "1":

			caller.ndb.tempConMod += 1

		elif raw_string == "2":

			caller.ndb.tempStrMod += 1

		caller.ndb.statTotalStr = caller.ndb.tempStr + caller.ndb.tempStrMod
		caller.ndb.statTotalDex = caller.ndb.tempDex + caller.ndb.tempDexMod
		caller.ndb.statTotalInt = caller.ndb.tempInt + caller.ndb.tempIntMod
		caller.ndb.statTotalCon = caller.ndb.tempCon + caller.ndb.tempConMod

		text = "You are a " + caller.ndb.tempRace + ". Your stats are: Str " + str(caller.ndb.statTotalStr) + ", Dex " + str(caller.ndb.statTotalDex) + ", Con " + str(caller.ndb.statTotalCon) + ", Int " + str(caller.ndb.statTotalInt) + ". Are these correct?"

		options = (
			{"desc": "Confirm",
			 "goto": "setAttributes"},
			{"desc": "Restart",
			 "goto": "qRace"}
			)

	elif caller.ndb.tempRace == "lizard":

		if raw_string == "1":

			caller.ndb.tempConMod += 1

		elif raw_string == "2":

			caller.ndb.tempDexMod += 1

		elif raw_string == "3":

			caller.ndb.tempStrMod += 1

		caller.ndb.statTotalStr = caller.ndb.tempStr + caller.ndb.tempStrMod
		caller.ndb.statTotalDex = caller.ndb.tempDex + caller.ndb.tempDexMod
		caller.ndb.statTotalInt = caller.ndb.tempInt + caller.ndb.tempIntMod
		caller.ndb.statTotalCon = caller.ndb.tempCon + caller.ndb.tempConMod

		text = "You are a " + caller.ndb.tempRace + ". Your stats are: Str " + str(caller.ndb.statTotalStr) + ", Dex " + str(caller.ndb.statTotalDex) + ", Con " + str(caller.ndb.statTotalCon) + ", Int " + str(caller.ndb.statTotalInt) + ". Are these correct?"

		options = (
			{"desc": "Confirm",
			 "goto": "setAttributes"},
			{"desc": "Restart",
			 "goto": "qRace"}
			)

	else:

		text = "There's been some error. Contact the admin."


	return text, options

# Setting the attributes permanently

def setAttributes(caller, raw_string):

	caller.db.race = caller.ndb.tempRace

	caller.db.statStr = caller.ndb.statTotalStr
	caller.db.statDex = caller.ndb.statTotalDex
	caller.db.statCon = caller.ndb.statTotalCon
	caller.db.statInt = caller.ndb.statTotalInt

	caller.db.isCharacterSet = True

	text = "The character is now set!"

	return text


# Counting menues

def rememberRace(caller, raw_string):
	
	if raw_string == "1":

		caller.ndb.tempRace = "slugcat"

		#Stats

		caller.ndb.tempStr = 2
		caller.ndb.tempDex = 5
		caller.ndb.tempInt = 3
		caller.ndb.tempCon = 2

		caller.ndb.tempStrMod = 0
		caller.ndb.tempDexMod = 0
		caller.ndb.tempIntMod = 0
		caller.ndb.tempConMod = 0


		#text

		text = "Slugcats are agile and cunning creatures that roam around this world. Due to their nomadic lifestyle they are masters at navigating this world. Do you wish to choose this race?"

		options = (
		{"desc": "Confirm",
		 "goto": "slugcatTree1"},
		{"desc": "Back",
		 "goto": "qRace"}
		)

	elif raw_string == "2":

		caller.ndb.tempRace = "scavenger"

		#Stats

		caller.ndb.tempStr = 1
		caller.ndb.tempDex = 3
		caller.ndb.tempInt = 6
		caller.ndb.tempCon = 2

		caller.ndb.tempStrMod = 0
		caller.ndb.tempDexMod = 0
		caller.ndb.tempIntMod = 0
		caller.ndb.tempConMod = 0


		#text

		text = "Scavengers are the smartest creatures. They live in groups and are able to craft more advanced tools. Do you wish to choose this race?"

		options = (
		{"desc": "Confirm",
		 "goto": "scavengerTree1"},
		{"desc": "Back",
		 "goto": "qRace"}
		)

	elif raw_string == "3":

		caller.ndb.tempRace = "lizard"

		#Stats

		caller.ndb.tempStr = 5
		caller.ndb.tempDex = 1
		caller.ndb.tempInt = 1
		caller.ndb.tempCon = 5

		caller.ndb.tempStrMod = 0
		caller.ndb.tempDexMod = 0
		caller.ndb.tempIntMod = 0
		caller.ndb.tempConMod = 0


		#text

		text = "Lizards are natural predators that often fight each other. What they lack in intellect and agility they make up in raw strength and toughness. Do you wish to choose this race?"

		options = (
		{"desc": "Confirm",
		 "goto": "lizardTree1"},
		{"desc": "Back",
		 "goto": "qRace"}
		)

	return text, options

# Other question trees start here

# Slugcat questions

def slugcatTree1(caller, raw_string):
	
	text = "Up to now, have you been a carnivore, herbivore, or omnivore?"

	options = (
		{"desc": "Carnivore (+ 1 strength)",
		 "goto": "slugcatTree2"},
		{"desc": "Herbivore (+ 1 dexterity)",
		 "goto": "slugcatTree2"},
		{"desc": "Omnivore (+ 1 con)",
		 "goto": "slugcatTree2"}
		)

	return text, options

def slugcatTree2(caller, raw_string):

	if raw_string == "1":

		caller.ndb.tempStrMod += 1

	elif raw_string == "2":

		caller.ndb.tempDexMod += 1

	elif raw_string == "3":

		caller.ndb.tempConMod += 1

	text = "Are you a light and smart slugcat, or a strong, capable one?"

	options = (
		{"desc": "Light (+ 1 dexterity, + 1 intelligence)",
		 "goto": "slugcatTree3"},
		{"desc": "Strong (+ 1 strength, + 1 con)",
		 "goto": "slugcatTree3"}
		)

	return text, options

def slugcatTree3(caller, raw_string):

	if raw_string == "1":

		caller.ndb.tempDexMod += 1
		caller.ndb.tempIntMod += 1

	elif raw_string == "2":

		caller.ndb.tempStrMod += 1
		caller.ndb.tempConMod += 1

	text = "Do you spend your time observing other creatures, or training?"

	options = (
		{"desc": "Training (+ 1 strength)",
		 "goto": "confirmAtt"},
		{"desc": "Observing (+ 1 intelligence)",
		 "goto": "confirmAtt"}
		)

	return text, options

# Scavenger questions

def scavengerTree1(caller, raw_string):

	text = "Are you a tribal warrior, traveller, merchant, or diplomat?"

	options = (
		{"desc": "Warrior (+1 strength)",
		 "goto": "scavengerTree2"},
		{"desc": "Traveller (+1 dexterity)",
		 "goto": "scavengerTree2"},
		{"desc": "Merchant (+1 constitution)",
		 "goto": "scavengerTree2"},
		{"desc": "Diplomat (+1 intelligence)",
		 "goto": "scavengerTree2"}
		)

	return text, options

def scavengerTree2(caller, raw_string):

	if raw_string == "1":

		caller.ndb.tempStrMod += 1;

	elif raw_string == "2":

		caller.ndb.tempDexMod += 1;

	elif raw_string == "3":

		caller.ndb.tempConMod += 1;

	elif raw_string == "4":

		caller.ndb.tempIntMod += 1;

	text = "A vulture attacks another tribe’s toll, do you help them or run?"

	options = (
		{"desc": "Warrior (+1 strength)",
		 "goto": "scavengerTree3"},
		{"desc": "Traveller (+1 dexterity)",
		 "goto": "scavengerTree3"}
		)

	return text, options

def scavengerTree3(caller, raw_string):

	if raw_string == "1":

		caller.ndb.tempConMod += 1;

	elif raw_string == "2":

		caller.ndb.tempStrMod += 1;


	text = "Do you earn your own pearls, or steal them?"

	options = (
		{"desc": "Earn (+1 constitution)",
		 "goto": "confirmAtt"},
		{"desc": "Steal (+1 strength)",
		 "goto": "confirmAtt"}
		)

	return text, options

# Lizard questions

def lizardTree1(caller, raw_string):

	text = "Do you like quarreling, or would you rather just watch other lizards fight?"

	options = (
		{"desc": "Quarrel (+ 1 strength)",
		 "goto": "lizardTree2"},
		{"desc": "Watch (+ 1 intelligence)",
		 "goto": "lizardTree2"}
		)

	return text, options


def lizardTree2(caller, raw_string):

	if raw_string == "1":

		caller.ndb.tempStrMod += 1;

	elif raw_string == "2":

		caller.ndb.tempIntMod += 1;


	text = "Are you the kind of lizard that rests in the sun and thinks about life, or the one that spins around wildly?"

	options = (
		{"desc": "Spin (+ 1 dexterity)",
		 "goto": "lizardTree3"},
		{"desc": "Rest (+ 1 intelligence)",
		 "goto": "lizardTree3"}
		)

	return text, options


def lizardTree3(caller, raw_string):

	if raw_string == "1":

		caller.ndb.tempStrMod += 1;

	elif raw_string == "2":

		caller.ndb.tempIntMod += 1;


	text = "Would you rather eat slugcat, scavenger, or lantern mice meat?"

	options = (
		{"desc": "Slugcat (+ 1 constitution)",
		 "goto": "confirmAtt"},
		{"desc": "Scavenger (+ 1 dexterity)",
		 "goto": "confirmAtt"},
		{"desc": "Lantern mice (+ 1 strength)",
		 "goto": "confirmAtt"}
		)

	return text, options