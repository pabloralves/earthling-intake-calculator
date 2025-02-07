import pandas as pd
from math import ceil
import streamlit as st
from logic import get_earthlings,consumption_frequencies


# Get available earthlings and intake frequencies
earthlings = get_earthlings()
frequency_options = list(consumption_frequencies.keys())

# Users specific intake data
user_intake = {}
user_eathlings_eaten_yearly = {}
user_eathlings_eaten_total = {}


DESCRIPTION_STRING = 'This calculator estimates how many **earthlings** a human being consumes across the lifespan based on a given period length and the average intake frequency of the earthlings involved.'

st.title('Earthling intake calculator')
st.image('./img/goat-8313480_640.jpg',caption='"Think occasionally of the suffering of which you spare yourself the sight." - Albert Schweitzer')
st.page_link("https://pixabay.com/photos/goat-horns-sleeping-mammal-animal-8313480/", label="Image by Dave (Pixabay)", icon="📷")
st.write(DESCRIPTION_STRING)


# 4. Show method
see_method = st.toggle("## Method")
if see_method:
    METHOD_STRING="""
    ⚠️ This estimation is based solely on earthling mass intake, so the real earthling numbers involved will be **substantially higher**:
    
    1. Earthlings used to feed other earthlings were not considered
    2. Earthlings discarded at any point of the food production chain (production, processing, distribution...) were also not considered 
    3. Earthlings discarded in the form of "food waste" were also not considered
    """
    st.info(METHOD_STRING)
    st.write('### 1. Earthling data')

    DATA_STRING = """Every kind of earthling has, by its very nature, its own mass. 
    For the humans that decide to consume them, these earthlings also present a percentage of edible mass as well as a serving size. 
    """
    st.write(DATA_STRING)
    
    def create_df(earthlings):
        df = pd.DataFrame([
            {'Name': earthling.name, 
            'Mass (kg)': earthling.mass,
            'Edible Percentage': earthling.edible_percentage, 
            'Serving Mass (kg)': earthling.serving_mass,}
            for earthling in earthlings])
        return df

    earthlings_data = create_df(earthlings)
    st.write(earthlings_data)

    see_sources = st.toggle("#### Data sources")
    if see_sources:
        st.page_link("https://www.worldometers.info/demographics/life-expectancy/", label="Average (world) life expectancy", icon="📊")
        st.page_link("https://www.scienceagri.com/2024/02/the-10-worlds-most-consumed-of-animal.html", label="Most consumed earthlings", icon="🔪")
        st.write('##### Chicken')
        st.page_link("https://foodly.tn/es/tips/how-much-does-a-whole-chicken-usually-weigh/", label="Mass", icon="🔬")
        st.page_link("http://www.cca.org.mx/cca/cursos/nmp/gastronomia/m6/img/pdf/Anexo16_m6.pdf", label="Edible %", icon="🏭")
        st.page_link("https://estilosdevidasaludable.sanidad.gob.es/alimentacionSaludable/habilidades/compra/menus/pdf/Peso_de_raciones_por_grupos.pdf", label="Serving size", icon="🍽️")      
        st.write('##### Pig')
        st.page_link("https://guiadegranja.com/cuanto-pesa-un-cerdo/", label="Mass", icon="🔬")
        st.page_link("https://www.3tres3.com/articulos/aprovechamiento-de-subproductos-porcinos_44211/", label="Edible %", icon="🏭")
        st.page_link("https://sanidadfuenllana1d.files.wordpress.com/2014/09/raciones-caseras.pdf", label="Serving size", icon="🍽️")
        st.write('##### Cattle')
        st.page_link("https://www.solofauna.com/vacas/cuanto-pesa-una-vaca-peso-promedio-por-edad-y-raza/", label="Mass", icon="🔬")
        st.page_link("https://www.contextoganadero.com/informes/cuanto-porcentaje-del-bovino-se-obtiene-para-su-aprovechamiento", label="Edible %", icon="🏭")
        st.page_link("https://eldiariony.com/2020/10/03/aprende-a-calcular-la-cantidad-exacta-de-carne-por-persona-un-basico-para-hacer-de-tus-parrilladas-un-exito/", label="Serving size", icon="🍽️") 
        st.write('##### Sheep')
        st.page_link("https://cuantopesa.org/cuanto-pesa-una-oveja/", label="Mass", icon="🔬")
        st.page_link("https://cuantopesa.org/cuanto-pesa-una-oveja/", label="Edible %", icon="🏭")
        st.page_link("https://estilosdevidasaludable.sanidad.gob.es/alimentacionSaludable/habilidades/compra/menus/pdf/Peso_de_raciones_por_grupos.pdf", label="Serving size", icon="🍽️")
        st.write('##### Goat')
        st.page_link("https://whatthingsweigh.com/how-much-does-a-goat-weigh/", label="Mass", icon="🔬")
        st.page_link("https://www.vcalc.com/wiki/AndrewBudd/Weight+of+meat+on+a+goat", label="Edible %", icon="🏭")
        st.page_link("https://www.healthline.com/nutrition/goat-meat-benefits?c=1413489482298#Goat-meat-basics", label="Serving size", icon="🍽️")
        st.write('##### Turkey')
        st.page_link("https://bbqhost.com/average-turkey-weight/", label="Mass", icon="🔬")
        st.page_link("https://global-faq.com/what-percentage-of-a-turkey-is-edible/", label="Edible %", icon="🏭")
        st.page_link("https://www.tasteofhome.com/article/how-much-turkey-per-person/", label="Serving size", icon="🍽️")
        st.write('##### Duck')
        st.page_link("https://pangeanimales.com/aves/pato/", label="Mass", icon="🔬")
        st.page_link("https://thishappyfarm.com/how-much-meat-does-a-duck-yield/", label="Edible %", icon="🏭")
        st.page_link("https://ask.usda.gov/s/article/How-much-duck-or-goose-should-you-buy-per-person", label="Serving size", icon="🍽️")

    st.write('### 2. Formula')
    FORMULA_TEXT_STRING = """
    Using this data we can compute the number of earthlings consumed using the following formula:
    """
    st.write(FORMULA_TEXT_STRING)

    FORMULA_STRING = r"""
     N_{\text{earthlinghts}} = \lceil Y_{\text{ears}} \cdot \frac{S_{\text{erving}} \cdot F_{requency} }{ M_{\text{ass}} \cdot E_{\text{dible\%}} } \rceil     
    """
    st.latex(FORMULA_STRING)
    st.write('Notice the ceiling function (earthlings do not survive when parts of them are being consumed).')
    st.write('**Dimensional analysis**:')

    UNIT_STRING = r"""
    [\text{earthlings}] = [\text{years}] \cdot \frac{ [\frac{\text{kg}}{\text{serving}}] \cdot [\frac{\text{serving}}{\text{year}}] }{ [\frac{\text{kg}}{\text{earthling}}]}
    """
    st.latex(UNIT_STRING)

# 5. Show About section
see_credits = st.toggle("#### About")
if see_credits:
    ABOUT_STRING="""**Dedication** *This calculator is dedicated to the flourishing of all eathlings*"""
    st.info(ABOUT_STRING)
    st.write('This project was born out of compassion, and it is my wish that it remains licensed under CC0 so that all can benefit from it in the best way possible.')
    st.page_link("https://creativecommons.org/public-domain/cc0/", label="CC0 License", icon="📄")    


st.divider()


# Fill user intake with 0s by default
for i,earthling in enumerate(earthlings):
    user_intake[f"{earthling.name}"] = 0    # Yearly intake (frequency)
    user_eathlings_eaten_yearly[f"{earthling.name}"] = 0  # Yearly intake (earthlings)
    user_eathlings_eaten_total[f"{earthling.name}"] = 0

# 1. Number input for number of years to use in the computation
st.write(f'## Time period')
st.info('**Step 1**. Choose how many years do you want to consider')


years = st.number_input('How many years do you want to consider?',
                        min_value=1,
                        max_value=150,
                        value=73,
                        step=1,
                        label_visibility='collapsed')



# 2. Sliders for user to indicate their How often do you have...?
st.write('## Intake frequency ')
st.info('**Step 2**. Select the option that best represents how often you ingest these earthlings')

for i,earthling in enumerate(earthlings):
    # Go over the earthlings to get their intake frequency
    st.write(f'####  {earthling.emoji} **{earthling.name}**')
    frequency  = st.select_slider(
        f'## {earthling.emoji} **{earthling.name}**?',
        options=frequency_options[::-1],
        key=f"{earthling.name}",
        label_visibility='collapsed'
    )

    # Save the actual year intake frequency equivalent
    user_intake[f"{earthling.name}"] = consumption_frequencies[frequency]


# Compute statistics
for earthling in earthlings:

    # Save number of earthlings eaten in a year (by mass)
    eaten_in_a_year = (earthling.serving_mass*user_intake[f"{earthling.name}"])/(earthling.mass*earthling.edible_percentage)
    user_eathlings_eaten_yearly[f"{earthling.name}"] = eaten_in_a_year

    # Save number of earthlings eaten in the entire period
    total_units = ceil(eaten_in_a_year*years)
    user_eathlings_eaten_total[f"{earthling.name}"] = total_units
    #print(earthling.name.title()+':',total_units,'('+str(earthling.yearly_servings),'servings/year, '+str("{:10.2f}".format(earthlings_eaten(earthling,1))),'earthlings/year)')


total_earthlings_eaten = sum(user_eathlings_eaten_total.values())
total_earthlings_eaten_yearly = sum(user_eathlings_eaten_yearly.values())

st.divider()

# 3. Show results
st.write(f'## Earthlings')
st.info(f'**Results**. With your current intake frequency, this is the approximate number of earthlings you can expect to eat eat over {years} years')
st.metric("Total 🍴", f"{total_earthlings_eaten}", f"{round(total_earthlings_eaten_yearly,2)}/year", border=True,delta_color='inverse')
data_total = pd.DataFrame(list(user_eathlings_eaten_total.items()), columns=["Earthling", "Count"])
st.bar_chart(data_total, x="Earthling", y="Count", stack=False,horizontal=True)

# Print each earthlings as a separate emoji
# see_earthlings = st.toggle("## Display",value=True)
#if see_earthlings:
st.info(f'This is a visual representation of the {total_earthlings_eaten} earthlings expected to be eaten during the next {years} years as a result of your current intake frequencies')
for earthling in earthlings:
    st.write(earthling.emoji*user_eathlings_eaten_total[earthling.name])

