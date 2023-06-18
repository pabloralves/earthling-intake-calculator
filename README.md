# Earthling intake calculator
Estimates how many earthlings a human eats across time based on earthling mass, edible percentage, serving size and consumption frequency.


## Use
Just run it from the console:
> python myearthlingintake.py

## License
Creative Commons Zero v1.0 Universal

This project was made for fun and to help raise awareness:
- Feel free to use, share, improve, fix or build upon this code. 
- No credit is needed

## Dependencies
- math (ceil function)

## Model

1. The user first specifies the time period in years
2. The program then estimates how many servings of each kind the user has per year by asking the user for each intake frequency on a weekly, monthy or yearly basis, multiplying by a factor of 52 or 12 if neccesary.
3. Thirdly, the program estimates how many earthlings of each kind the user eats per year (with decimals) using the following formula: **(Earthling serving mass * Yearly servings) / (Earthling mass * Earthling edible fraction )**
4. To get the total number of earthlings of each kind the user eats on the time period, the previous number is multiplied by the number of years and rounded to the next integer
5. Finally, the total number of earthlings is finally aggregated


### Earthling values

| Animal  | mass [kg] | edible % | serving [g] |
|---------|-----------|----------|-------------|
| Chicken | 3         | 56       | 110         |
| Pig     | 105       | 70       | 150         |
| Cattle  | 450       | 85       | 300         |
| Sheep   | 45        | 50       | 110         |
| Goat    | 34        | 25       | 85          |
| Turkey  | 9         | 55       | 570         |
| Duck    | 1.35      | 63       | 500         |

### Limitations
As the estimation is based on earthling mass intake alone, the earthling number is likely higher.
- Other animal products and derivatives (such as eggs, milk, leather...) were not considered
- Earthlings used to feed other earthlings were not considered
- Earthlings who were discarded during production and transportation were not considered
- Earthlings discarded by the consumer once purchased were are not considered

#### Data sources
- Most consumed earthlings: https://scienceagri.com/the-10-worlds-most-consumed-of-animal-meat/
- Average world life expectancy: https://www.worldometers.info/demographics/life-expectancy/

Chicken
-  mass:   https://foodly.tn/es/tips/how-much-does-a-whole-chicken-usually-weigh/
-  %:      http://www.cca.org.mx/cca/cursos/nmp/gastronomia/m6/img/pdf/Anexo16_m6.pdf
- serving: https://estilosdevidasaludable.sanidad.gob.es/alimentacionSaludable/habilidades/compra/menus/pdf/Peso_de_raciones_por_grupos.pdf

Pig
-  mass:   https://guiadegranja.com/cuanto-pesa-un-cerdo/
-  %:      https://www.3tres3.com/articulos/aprovechamiento-de-subproductos-porcinos_44211/
- serving: https://sanidadfuenllana1d.files.wordpress.com/2014/09/raciones-caseras.pdf

Cattle
-  mass:   https://www.solofauna.com/vacas/cuanto-pesa-una-vaca-peso-promedio-por-edad-y-raza/
-  %:      https://www.contextoganadero.com/informes/cuanto-porcentaje-del-bovino-se-obtiene-para-su-aprovechamiento and https://respuestasabia.com.mx/que-porcentaje-se-aprovecha-de-una-vaca/
- serving: https://eldiariony.com/2020/10/03/aprende-a-calcular-la-cantidad-exacta-de-carne-por-persona-un-basico-para-hacer-de-tus-parrilladas-un-exito/

Sheep
-  mass:   https://cuantopesa.org/cuanto-pesa-una-oveja/
-  %:      https://cuantopesa.org/cuanto-pesa-una-oveja/
- serving: https://estilosdevidasaludable.sanidad.gob.es/alimentacionSaludable/habilidades/compra/menus/pdf/Peso_de_raciones_por_grupos.pdf

Goat
-  mass:   https://www.reference.com/pets-animals/average-weight-goat-aa2887a76452bcb8 and https://whatthingsweigh.com/how-much-does-a-goat-weigh/
-  %:      https://www.vcalc.com/wiki/AndrewBudd/Weight+of+meat+on+a+goat
- serving: https://www.healthline.com/nutrition/goat-meat-benefits?c=1413489482298#Goat-meat-basics

Turkey
-  mass:   https://bbqhost.com/average-turkey-weight/
-  %:      https://global-faq.com/what-percentage-of-a-turkey-is-edible/
- serving: https://www.tasteofhome.com/article/how-much-turkey-per-person/

Duck
-  mass:   https://pangeanimales.com/aves/pato/
-  %:      https://thishappyfarm.com/how-much-meat-does-a-duck-yield/
- serving: https://ask.usda.gov/s/article/How-much-duck-or-goose-should-you-buy-per-person


## TO-DOs
- Add more earthlings such as fish
- Add argparse arguments such as --animal --estimation --years --verbose
- Manually code ceil function to free code from dependencies
