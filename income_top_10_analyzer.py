import pandas as pd

class income_top_10_analyzer():
    """This class contains 3 methods: the first one reads the csv file where data about the income share held by highest 
    10% is stored and then generates a sorted DataFrame. The second filters this object, generating another DataFrame containing 
    only the countries/groups of interest. Finally, the third method returns the highest value of the analized index."""
    
    def __init__(self, country_list):
        self.country_list = country_list
        self.df_top_10 = pd.read_csv("original_table\\inc_top_10.csv", header = None, index_col = 1)

    def _generating_dataFrame(self):
        ineq = self.df_top_10.drop(self.df_top_10.iloc[:,0:6], axis = 1)
        ineq.index.name = None
        ineq = ineq.T

        ineq = ineq.rename( columns = {'Country Code': 'Year'} )
        ineq = ineq.astype({'Year': int})
        ineq.to_csv('generated_tables\\all_countries_organized.csv')
        return ineq

    def selecting_countries_and_columns(self):
        data_frame = self._generating_dataFrame()
        self.columns_of_interest = []
        for country in self.country_list:
            if country == 'BRICS':
                self.columns_of_interest.extend(['BRA', 'RUS', 'IND', 'CHN', 'ZAF'])
            elif country == 'SOUTHAMERICA':
                self.columns_of_interest.extend(['BRA', 'ARG', 'COL', 'CHL', 'PER', 'ECU', 'BOL', 'URY', 'PRY'])
            elif country == 'TOP10':
                self.columns_of_interest.extend(['BRA', 'USA', 'GBR', 'JPN', 'DEU', 'IND', 'FRA', 'CHN', 'ITA', 'CAN'])
            elif country in list(data_frame.columns)[1:]:
                self.columns_of_interest.append(country)
            else:
                return print(f'There is no available data about the country/group {country}. Check the README.MD file for valid options')
        self.uniq_columns = list(set(self.columns_of_interest))
        self.uniq_columns.insert(0, 'Year')

        self.inequality = data_frame[self.uniq_columns].copy()
        self.inequality.loc[:, 'AVG'] = (self.inequality.sum(axis=1) - self.inequality['Year'])/(len(self.inequality.iloc[0,:])-1)
        self.uniq_columns.append('AVG')
        return (self.inequality, self.uniq_columns)

    def selecting_maximum_value(self, data_frame):
        top_lim = 0
        for label, value in data_frame.iteritems():
            if label != 'Year' and data_frame[label].max() > top_lim:
                top_lim = data_frame[label].max()
        return top_lim