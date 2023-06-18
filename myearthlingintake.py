# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:49:26 2023

Earthling (Life) Intake Calculator

Description
Estimates the number of earthlings a human eats across many years based on their mass, edible percentage, and serving size.


Introduction
Eating one serving not conscious. But habit comes a long way.

Calculations cover some of the most consumed earthlings worldwide, such as: chicken, pig, cattle, sheep, goat, turkey, duck and a category for others.

Stats for the earthlings come from here:

# PIG
# 105 kg   https://guiadegranja.com/cuanto-pesa-un-cerdo/
# 70 %     https://www.3tres3.com/articulos/aprovechamiento-de-subproductos-porcinos_44211/
# 0.150 kg https://sanidadfuenllana1d.files.wordpress.com/2014/09/raciones-caseras.pdf

# VACA
# 450 kg https://www.solofauna.com/vacas/cuanto-pesa-una-vaca-peso-promedio-por-edad-y-raza/
# 0.3 kg https://eldiariony.com/2020/10/03/aprende-a-calcular-la-cantidad-exacta-de-carne-por-persona-un-basico-para-hacer-de-tus-parrilladas-un-exito/
# 89.5 % https://www.contextoganadero.com/informes/cuanto-porcentaje-del-bovino-se-obtiene-para-su-aprovechamiento
# 80 %   https://respuestasabia.com.mx/que-porcentaje-se-aprovecha-de-una-vaca/

# CHICKEN
# 3 kg    https://foodly.tn/es/tips/how-much-does-a-whole-chicken-usually-weigh/
# 56 %    http://www.cca.org.mx/cca/cursos/nmp/gastronomia/m6/img/pdf/Anexo16_m6.pdf
# 0.11 kg https://estilosdevidasaludable.sanidad.gob.es/alimentacionSaludable/habilidades/compra/menus/pdf/Peso_de_raciones_por_grupos.pdf

# OVEJA
# 45 kg   https://cuantopesa.org/cuanto-pesa-una-oveja/
# 50%     https://cuantopesa.org/cuanto-pesa-una-oveja/
# 0.11 kg https://estilosdevidasaludable.sanidad.gob.es/alimentacionSaludable/habilidades/compra/menus/pdf/Peso_de_raciones_por_grupos.pdf

# Cabra (goat)
34 kg     https://www.reference.com/pets-animals/average-weight-goat-aa2887a76452bcb8           https://whatthingsweigh.com/how-much-does-a-goat-weigh/
0.085 kg  https://www.healthline.com/nutrition/goat-meat-benefits?c=1413489482298#Goat-meat-basics
25.5%     https://www.vcalc.com/wiki/AndrewBudd/Weight+of+meat+on+a+goat
# Turkey
9 kg (20 pounds)   https://bbqhost.com/average-turkey-weight/
55%                https://global-faq.com/what-percentage-of-a-turkey-is-edible/
0.57 kg (1.25 lbs) https://www.tasteofhome.com/article/how-much-turkey-per-person/

# Duck
1.35 kg (0.7-2)  https://pangeanimales.com/aves/pato/
62.5% (60-65%)   https://thishappyfarm.com/how-much-meat-does-a-duck-yield/
0.5 (1-1.2 pounds) https://ask.usda.gov/s/article/How-much-duck-or-goose-should-you-buy-per-person

Life expectancy average comes from here:
73 https://www.worldometers.info/demographics/life-expectancy/

Common earthlings consumed:
https://scienceagri.com/the-10-worlds-most-consumed-of-animal-meat/

Model
Formula is earthling.serving_mass*earthling.yearly_servings)/(earthling.mass*earthling.edible_percentage
To get yearly_servings user is asked for its weekly, monthy or year servings, multiplying by a factor of 52 or 12 if neccesary.
Rounding to the next integer is performed on the last step to get the final earthling number.


Limitations
The model only uses the  mass eaten to calculate the final earthling number 
- Other animal products and derivatives (such as eggs, milk, leather...) are not considered
- Earthlings used to feed other earthlings are not considered
- Earthlings killed during the process and transportation are not considered
- Earthlings trashed without being consumed are not considered
- Earthlings not consumed but disposed by the human are not considered

TO-DOs
# TODO: Add fish
# TODO: Add argparse arguments: --animal --estimation --years --verbose
# TODO: Manually code ceil function to avoid dependencies

argparse: https://docs.python.org/3/library/argparse.html

import argparse
parser = argparse.ArgumentParser(
                    prog='Life creature intake calculator',
                    description='Calculates how many animals you eat across a lifespan based on how many meet servings you usually have',
                    epilog='Text at the bottom of help')
parser.add_argument('-a', '--animal', help="specifies a certain animal (default 'all')",action='store_true')
parser.add_argument('-y', '--years', help="specifies the timespan in years (default '80')", action='store_true')
parser.add_argument('-e', '--estimation', help="specifies the estimation [low,medium,high] (default 'medium')", action='store_true')
args = parser.parse_args()
print(args.params)
print(args.filename, args.count, args.verbose)

@author: Pablo
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


#print('Yearly average:')
#for earthling in earthlings:
#	print(earthling.name.title()+':',str(earthlings_eaten(earthling,1)),'('+str(earthling.yearly_servings),'servings/year)')


print('\nEarthling intake in ',years,'years')
total_earthlings = 0


for earthling in earthlings:
	total_units = ceil(earthlings_eaten(earthling,years))
	total_earthlings += total_units
	print(earthling.name.title()+':',total_units,'('+str(earthling.yearly_servings),'servings/year, '+str("{:10.2f}".format(earthlings_eaten(earthling,1))),'earthlings/year)')


print('\nTotal:',total_earthlings,'('+str(total_earthlings/years)+'/year)')
print('\nNote: this estimation is based on raw mass intake.\nReal earthling number is likely higher')


