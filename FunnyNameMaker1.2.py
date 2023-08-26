import random
from random import choice

first_fun = [
    "The Holy Flamming",
    "Giant Death",
    "The Unholy Freezing",
    "Anti-telaharsec",
    "Legendarly Enchanted",
    "Death Song of the Mighty",
    "Magic Flying",
    "Holy Raging Power of the",
    "Goblin-Smashing",
    "The Holy",
    "Heavy Metal",
    "Laser-shooting",
    "Thunder-Striking",
    "Wizard-Thrashing",
    "The Astral",
    "Horrific Screams of The Terror",
    "Dark Matter",
    "All-Seeing",
    "Legend of the Astral",
]
power = [
    "Laser-Powered",
    "Solar-Powered",
    "Thunder-Powered",
    "Laser-shooting",
    "Thunder-Striking",
    "Wizard-Thrashing",
    "Goblin-Smashing",
]
adj = [
    "Shining",
    "Magic",
    "Toy",
    "Invisible",
    "Quantum",
    "Universal",
    "Squeaky",
    "Crystal",
    "Glory",
    "Robotic",
    "Ancestral",
    "Epic",
    "Galactic",
    "Golden",
    "Evil",
    "Cosmic",
    "Thundering",
    "Laser",
    "Amazing",
    "Immortal",
    "Giant",
    "Doomed",
    "Healing",
    "Unholy "
    "Screaming",
    "Vorpal",
    "Anti-Matter",
    "Delicous",
    "Venganceful",
    "Terrible",
    "Crazy",
    "Ultimate",
    "Tyannical",
    "Monstrous",
    "Mighty",
    "Slashing",
    "Wise",
    "Submersable",
    "Annoying",
    "Boring",
    "Singing",
    "Tiny",
    "Fearless",
    "Overwhelming",
    "Fire",
    "Shadow",
    "Lighting",
]
second_fun = [
    "Chili Peppers",
    "the Magic Land of Nevada",
    "Scratching People",
    "Bitterness",
    "Chasing Cats",
    "Sillyness",
    "Summoning Demons",
    "Reno",
    "The Terrorvortex",
    "Fallon",
    "Fernley",
    "Smashing Goblins",
    "Thrashing Evil Wizards",
    "Chrushing Darklords",
    "the Kingdom of Fife",
    "the City of Dundee",
    "the Town of Dunkeld",
    "The Mighty River Tay",
    "Fighting Trolls",
    "Slashing Through Goblins",
    "Slashing Through Goblins on "
    "the Dark Side of The Moon",
    "Fighting Stormtroopers",
    "Driving Speeders",
    "Glory",
    "Justice",
    "Evil",
    "Chaos",
    "Crail",
    "Making Us Laugh",
    "Paris",
    "Shopping",
    "Traveling Space",
    "Fighting Space Battles",
    "Nuclear Justice",
    "Recording Information",
    "All-Seeing",
    "Sailing",
    "Unholy Cosmic Frost",
    "Glorius Hair",
    "Endless Energy",
    "Holding Picture",
    "Messyness",
    "Dispair",
    "Eat Your Face",
    "Flying High Into Space",
    "Happy Funness",
    "Egg-Lofting",
    "Blowing Up The Death Star",
    "Making Things Go Kaboom",
    "Falling over Laughing",
    "Singing Stupid Songs",
    "The Raging Storm",
    "The Goblin King",
    "The Keeper of The Stars",
    "Annoying Me When I'm Trying to Work",
    "The Master of Maddness",
    "The Prince of Fife",
    "The King of Chaos",
    "The Lord of the Wizards",
    "The Crystal Dragonfire",
    "The Path of Dooooom",
    "The Dark Prophecy",
    "The King of Dragons",
    "The King of Dundee",
    "Flame",
    "Frost",
    "Wind",
    "Stone",
    "Shadows",
    "Light",
    "Time",
    "Utter Ridiculousness",
    "The Ten Plagues of Egypt",
    "Silver Springs",
    "Furious Thunder",
    "the Realm of Carson City",
    "Madness",
    "Cleaving Castles",
    "Whacking",
    "the Magic Lake Tahoe",
    "The Truckee River",
    "the Kingdom of Calafonia",
    "Salinas",
    "Tulsa",
    "Glasgow",
    "Going Insane",
    "Astra",
    "Eating Peasants",
    "Saturn",
    "Venus",
    "Jupiter",
    "Mars",
    "Earth",
    "the Moon",
    "Uranus",
    "Nepune",
    "Triton",
    "Cutting Your Ears off",
    "Stabbing Your Eyes Out",
]

def generateName(word):
    start = choice(first_fun)
    adjee = choice(adj)
    pwr = choice(power)
    end = choice(second_fun)
    the = random.randint(1, 5)
    if the == 1:
        return("{} {} of {}".format(start, word, end))
    elif the == 2:
        return("{} {}".format(start, word))
    elif the == 3:
        return("The {} of {}".format(word, end))
    elif the == 4:
        return("{} {} {}".format(pwr, adjee, word))
    elif the == 5:
        return("{} {} {} {} of {}".format(start, pwr, adjee, word, end))
    
    return("Something went wrong.")#Shouldn't Happen

print("FunnyNameMaker version 1.2. Added new format option, and possible options for names.")
print("This a Python program written to make ridiculous names for anything you can think of. Your math book? " + generateName("Math Book") + "!")
print("Your phone? It's the " + generateName("Phone") +"! Your Keyboard? The " + generateName("Keyboard") +"! The names get ridiculous!")
print("Produces 100 names for you to pick from, so you don't have to rerun the code to find one you like.")
print("Warning: there may or may not be small amounts of funny references in here. Use at your own risk.")

wordInput = input("What do you want a name for: ")

for i in range(100):
    print(generateName(wordInput) + ".")