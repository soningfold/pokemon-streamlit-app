# Pokémon Lookup App

This interactive web application allows users to explore and compare Pokémon data. Built using **Streamlit**, it provides a fun and engaging way to visualize Pokémon stats and compare attributes across different Pokémon.

## Features

- **Search Pokémon by Number**:
  Enter a Pokémon's Pokédex number to fetch details such as name, height, weight, and types.

- **Pokémon Sprite**:
  Displays the official image of the selected Pokémon.

- **Stats Comparison**:
  Compare selected stats (e.g., height, weight, HP, speed) with 5 random Pokémon using interactive bar charts.
  
- **Type Average Stats**:
  Visualize the average stats for the selected Pokémon's type alongside the selected stats.

## Usage

1. Visit the live app here: [Pokémon Lookup App](https://pokemon-group-e.streamlit.app/)
2. Use the sidebar to:
   - Enter a Pokémon's Pokédex number.
   - Choose stats for comparison.
3. Explore detailed Pokémon data in the **"Pokemon Data"** tab.
4. Compare stats in the **"Stats Comparison"** tab with interactive charts.

## Installation (Optional for Local Development)

If you'd like to run the app locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pokemon-lookup-app.git
   cd pokemon-lookup-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Requirements

- Python 3.7+
- All required libraries are listed in `requirements.txt`.

## Data Source

- Pokémon data: Loaded from a CSV file (`pokemon.csv`).
- Pokémon sprites: Dynamically fetched from the [PokéAPI](https://pokeapi.co/).

## Example

![Pokémon App Screenshot](/Screenshot.png)


