import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import altair as alt



df = pd.read_csv('pokemon.csv')

st.title("Pokemon Lookup App")

tab1, tab2 = st.tabs(["Pokemon Data", "Stats Comparison"])

st.sidebar.title('Pokemon Options')
st.sidebar.header('Choose Options:')

pokemon_number = st.sidebar.number_input("Pokemon Number: ", min_value=1, max_value=int(max(df['pokedex_number'])))

details = df[df['pokedex_number'] == pokemon_number]

st.sidebar.caption(f"Select stats below - the stats for {details.iloc[0]['name']} will be compared to 5 other random Pokemon:")
stats = st.sidebar.multiselect('What stats do you want to compare?',
                ['height_m','weight_kg','total_points','hp','speed']
                )

with tab1:
    # Creating columns with custom width ratios
    col1, col2, col3 = st.columns([5, 0.1, 2])

    with col1:
        # Display the name, height, weight and other attributes of the pokemon.
        if details.iloc[0]['type_number'] == 1:
            st.write(details[['name', 'height_m', 'weight_kg', 'type_1']])
        else:
            st.write(details[['name', 'height_m', 'weight_kg', 'type_1', 'type_2']])

    # Adding vertical space
    st.write("") 

    # Adding elements to the third column
    with col3:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}")
        if response.status_code == 200:
            image_url = response.json()['sprites']['front_default']
            st.image(image_url, width=200) #, use_container_width=True
        else:
            st.error('Pokemon image not found.')
          
    st.subheader('Description') 

    st.write(f"{details['name'].iloc[0]} is a {details['type_1'].iloc[0]} type Pokemon. Its species is {details['species'].iloc[0]} and its status is {details['status'].iloc[0]}.")
    if details['abilities_number'].iloc[0] >= 1:
        st.write(f"Its main ability is {details['ability_1'].iloc[0]}.")      

    
with tab2:
    st.subheader('Stats Comparison')
    


    for stat in stats:
        st.write(stat.title())
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
    
    # Now compare these stats to the averages for each Pokemon type

    st.subheader('Average Stats for this Pokemon\'s Type')
    st.caption(f"The stats you selected above for {details.iloc[0]['name']} will be compared to the average stats of all Pokemon of the same type:")

    for stat in stats:
        st.write(stat.title())
        selected_pokemon = details[['name', 'type_1', stat]]
        selected_type = selected_pokemon['type_1'].iloc[0]
        avg_stats = df[df['type_1'] == selected_type].groupby('type_1')[stat].mean().reset_index()
        avg_stats = avg_stats.rename(columns={stat: 'average_' + stat})
        avg_stats['name'] = f'Average {stat.title()} - {selected_type.title()}'
        avg_stats = avg_stats[['name', 'type_1', 'average_' + stat]]
        selected_pokemon = selected_pokemon.rename(columns={stat: 'average_' + stat})
        combined_data = pd.concat([selected_pokemon, avg_stats])
    
        chart = alt.Chart(combined_data).mark_bar().encode(
            x=alt.X('name', axis=alt.Axis(labelAngle=-45)),
            y=alt.Y('average_' + stat, title='Stat Value'),
            #color='type_1',
            tooltip=['name', 'type_1', 'average_' + stat]
        ).properties(
            width=600,
            height=400
        )
    
        st.altair_chart(chart)
        st.write('---')
