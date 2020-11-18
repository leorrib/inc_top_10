# Analysis of the index 'Income share held by highest 10%' in several countries
Given a file containing data downloaded from the 'The World Bank', this program allows the user to plot the behaviour of the 'Income share held by highest 10%' index (from 2008 to 2018) regarding several countries. Once the program is running, the user is prompted to enter the country code/group name (there's no limit regarding the number of entries) and then a graphic is generated. The input options are: BRA (Brazil), ARG (Argentina), COL (Colombia), CHL (Chile), PER (Peru), ECU (Ecuador), BOL (Bolivia), URY (Uruguay), PRY (Paraguay), USA (United States), GBR (Great Britain), CHN (China), JPN (Japan), DEU (Germany), IND (India), FRA (France), ITA (Italy), CAN (Canada), RUS (Russia), ZAF (South Africa), PRT (Portugal), South America, BRICS and Top 10 (Top 10 Biggest Economies in 2020).

## How to Run
### Requirements
- Python 3 (pip).
- Python packages: matplotlib and pandas.

### Setup
- Clone the project.
- If you want to install the packages locally, follow the instructions below. Otherwise, enter 'pip install matplotlib' and 'pip install pandas' in order to install these packages globally.
- Create a virtual environment on root level: 'python -m venv .venv'.
- Initialize the virtual environment (also on root level): '.venv\Scripts\activate'
- Again on root level, enter 'pip3 install -r requirements.txt' in order to install all necessary packages.

### Running the program
- On root level, enter 'python main.py' (for Windows) or 'python3 main.py' (for Mac).
- You will be prompted to enter one or more country codes/group names (separated by ","). Do so and press 'Enter'.

### References
- https://databank.worldbank.org/source/world-development-indicators