import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# import matplotlib.pyplot as plt 

df = pd.read_csv('pokemon.csv')

st.title("Pokemon Lookup App")

pokemon_number = st.number_input("Pokemon Number: ", min_value=1, max_value=int(max(df['pokedex_number'])))

details = df[df['pokedex_number'] == pokemon_number]

# Display the name, height, weight and other attributes of the pokemon.

if details.iloc[0]['type_number'] == 1:
    st.write(details[['name', 'height_m', 'weight_kg', 'type_1']])
else: 
    st.write(details[['name', 'height_m', 'weight_kg', 'type_1', 'type_2']])
    
st.markdown('---')
st.subheader('Stats Comparison')
st.caption('Select stats below; the stats for your selected Pokemon will be compared to 5 random Pokemon')

stats = st.multiselect('What stats do you want to compare?',
               ['height_m','weight_kg','total_points','hp','speed']
               )
st.write('You selected the following stats: ',stats)

for stat in stats:
    st.write(stat)
    random_pokemon = df.sample(5)
    selected_pokemon = details[['name', 'type_1', stat]]
    random_pokemon = random_pokemon[['name', 'type_1', stat]]
    data = pd.concat([selected_pokemon, random_pokemon])
    data.reset_index(drop=True, inplace=True)
    
    chart = alt.Chart(data).mark_bar().encode(
        x='name',
        y=stat,
        color='type_1',
        tooltip=['name', 'type_1', stat]
    ).properties(
        width=600,
        height=400
    )
    
    st.altair_chart(chart)
    st.write('---')

# for stat in stats:
#     st.write(stat)
#     random_pokemon = df.sample(5)
#     selected_pokemon = details[stat]
#     data = pd.concat([random_pokemon[stat], selected_pokemon])
#     st.bar_chart(data)
#     st.write('---')
    
