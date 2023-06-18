# -*- coding: utf-8 -*-
"""
Earthling intake calculator

Estimates the number of earthlings a human eats across many years based on their mass, edible percentage, and serving size.
"""


from math import ceil

class Earthling:
	def __init__(self,name,mass,edible_percentage,serving_mass):
		self.name = name
		self.mass = mass # [kg]
		self.edible_percentage = edible_percentage # [0 to 1]
		self.serving_mass = serving_mass # [kg]

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


chicken = Earthling(name='chicken',mass=3,   edible_percentage=0.56,serving_mass=0.110)
pig     = Earthling(name='pig',    mass=105, edible_percentage=0.70,serving_mass=0.150)
cattle  = Earthling(name='cattle', mass=450, edible_percentage=0.85,serving_mass=0.3)
sheep   = Earthling(name='sheep',  mass=45,  edible_percentage=0.50,serving_mass=0.110)
goat    = Earthling(name='goat',   mass=34,  edible_percentage=0.25,serving_mass=0.085)
turkey  = Earthling(name='turkey', mass=9,   edible_percentage=0.55,serving_mass=0.57)
duck    = Earthling(name='duck',   mass=1.35,edible_percentage=0.63,serving_mass=0.5)

earthlings = []
earthlings.append(chicken)
earthlings.append(pig)
earthlings.append(cattle)
earthlings.append(sheep)
earthlings.append(goat)
earthlings.append(turkey)
earthlings.append(duck)


years = int(input('How many years do you want to take into account? (average life expectancy: 73 years): '))
print('')


for earthling in earthlings:
	yearly_servings = find_yearly_servings(earthling)
	earthling.set_yearly_servings(yearly_servings)
	#print('')


print('\nEarthling intake in ',years,'years')
total_earthlings = 0


for earthling in earthlings:
	total_units = ceil(earthlings_eaten(earthling,years))
	total_earthlings += total_units
	print(earthling.name.title()+':',total_units,'('+str(earthling.yearly_servings),'servings/year, '+str("{:10.2f}".format(earthlings_eaten(earthling,1))),'earthlings/year)')


print('\nTotal:',total_earthlings,'('+str(total_earthlings/years)+'/year)')
print('\nNote: this estimation is based on raw mass intake.\nReal earthling number is likely higher')
