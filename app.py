import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon.csv')

st.title("Pokemon Lookup App")

#Consider pokedex number somehow - for now using id to lookup
pokemon_number = st.number_input("Pokemon Number: ", min_value=0, max_value=int(max(df['id'])))

details = df[df['id'] == pokemon_number]

# Display the name, height, weight and other attributes of the pokemon.

if details.iloc[0]['type_number'] == 1:
    st.write(details[['name', 'height_m', 'weight_kg', 'type_1']])
else:
    st.write(details[['name', 'height_m', 'weight_kg', 'type_1', 'type_2']])