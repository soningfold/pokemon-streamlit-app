import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

df = pd.read_csv('pokemon.csv')

st.title("Pokemon Lookup App")

pokemon_number = st.number_input("Pokemon Number: ", min_value=1, max_value=int(max(df['pokedex_number'])))

details = df[df['pokedex_number'] == pokemon_number]

# Display the name, height, weight and other attributes of the pokemon.

if details.iloc[0]['type_number'] == 1:
    st.write(details[['name', 'height_m', 'weight_kg', 'type_1']])
else:
    st.write(details[['name', 'height_m', 'weight_kg', 'type_1', 'type_2']])
    
# call the pokeapi to get the image of the pokemon
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}")

if response.status_code == 200:
    image_url = response.json()['sprites']['front_default']
    st.image(image_url, caption=f"{details['name'].iloc[0]}", use_container_width=True)
    
    