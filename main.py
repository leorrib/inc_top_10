import matplotlib.pyplot as plt
from income_top_10_analyzer import income_top_10_analyzer

list_of_countries = [item.upper() for item in input("Enter the country/group codes: ").replace(" ","").split(',')]

dataset = income_top_10_analyzer(list_of_countries)
country_df, country_columns = dataset.selecting_countries_and_columns()
max_val = dataset.selecting_maximum_value(country_df)

country_df.plot(
    x = 'Year', y = country_columns[1:], 
    ls = '-.',
    cmap = 'gist_rainbow',
    ylim = (20, max_val + 2),
    figsize = (9, 9), 
    title = f'Income share held by top 10% from 2009 to 2018'
)
plt.ylabel('Income share held by top 10% (%)')
plt.show()