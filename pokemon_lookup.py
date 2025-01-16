import streamlit as st
import pandas as pd
import numpy as np
import altair as alt # don't forget to install this package

df = pd.read_csv('pokemon.csv')

st.title("Pokemon Lookup App")

pokemon_number = st.number_input("Pokemon Number: ", min_value=1, max_value=int(max(df['pokedex_number'])))

details = df[df['pokedex_number'] == pokemon_number]

# Display the name, height, weight and other attributes of the pokemon.

if details.iloc[0]['type_number'] == 1:
    st.write(details[['name', 'height_m', 'weight_kg', 'type_1']])
else: 
    st.write(details[['name', 'height_m', 'weight_kg', 'type_1', 'type_2']])
 
 
## My part of the code starts here:    
st.markdown('---')
st.subheader('Stats Comparison')
st.caption('Select stats below - the stats for your selected Pokemon will be compared to 5 other random Pokemon:')

stats = st.multiselect('What stats do you want to compare?',
               ['height_m','weight_kg','total_points','hp','speed']
               )

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
st.caption('The stats you selected above for your selected Pokemon will be compared to the average stats of all Pokemon of the same type:')

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
