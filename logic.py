"""
Contains the main logic parts of the calculator
"""

class Earthling:
	def __init__(self,name,mass,edible_percentage,serving_mass,emoji,name_plural):
		self.name = name
		self.name_plural = name_plural
		self.mass = mass # [kg]
		self.edible_percentage = edible_percentage # [0 to 1]
		self.serving_mass = serving_mass # [kg]
		self.emoji = emoji

	def set_yearly_servings(self,servings):
		self.yearly_servings = servings


def earthlings_eaten(earthling,years):
	eaten_in_a_year = (earthling.serving_mass*earthling.yearly_servings)/(earthling.mass*earthling.edible_percentage)
	return eaten_in_a_year*years

def find_yearly_servings(earthling):
	ever = input('Do you eat '+earthling.name+' (yes/no)?: ')
	if ever.lower() == 'n' or ever.lower() =='no':
		return 0
	weekly = input('How many times do you eat '+earthling.name+' a week? (0 if less often): ')
	if weekly != '0' and weekly != '':
		return int(weekly)*52
	monthy = input('How many times do you eat '+earthling.name+' a month? (0 if less often): ')
	if monthy != '0' and weekly != '':
		return int(monthy)*12
	yearly = input('How many times do you eat '+earthling.name+' a year?: ')
	return int(yearly)



def get_earthlings():
    chicken = Earthling(name='Chicken',mass=3,   edible_percentage=0.56,serving_mass=0.110,emoji='🐔',name_plural='Chickens')
    pig     = Earthling(name='Pig',    mass=105, edible_percentage=0.70,serving_mass=0.150,emoji='🐖',name_plural='Pigs')
    cattle  = Earthling(name='Cattle', mass=450, edible_percentage=0.85,serving_mass=0.3,emoji='🐄',name_plural='Cattle')
    sheep   = Earthling(name='Sheep',  mass=45,  edible_percentage=0.50,serving_mass=0.110,emoji='🐑',name_plural='Sheeps')
    goat    = Earthling(name='Goat',   mass=34,  edible_percentage=0.25,serving_mass=0.085,emoji='🐐',name_plural='Goats')
    turkey  = Earthling(name='Turkey', mass=9,   edible_percentage=0.55,serving_mass=0.57,emoji='🦃',name_plural='Turkeys')
    duck    = Earthling(name='Duck',   mass=1.35,edible_percentage=0.63,serving_mass=0.5,emoji='🦆',name_plural='Ducks')

    earthlings = []
    earthlings.append(chicken)
    earthlings.append(pig)
    earthlings.append(cattle)
    earthlings.append(sheep)
    earthlings.append(goat)
    earthlings.append(turkey)
    earthlings.append(duck)

    return earthlings


# Consumption frequencies and their year consumption frequency equivalent
consumption_frequencies = {
    "Daily": 365, 
    "Weekly (5 times)":52*5,
    "Weekly (4 times)":52*4,
    "Weekly (3 times)":52*3,
    "Twice a week":52*2,
    "Once a week":52*1,
    "Monthly (3 times)":12*3,
    "Twice a month":12*2,
    "Once a month":12,
    "Once every 2 months":6,
    "Once every 3 months":4,
    "Twice a year":2,
    "Once a year":1,
    "Never":0
}
