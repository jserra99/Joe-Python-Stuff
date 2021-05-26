# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
my_countries = ['United States', 'Zimbabwe','Cuba', 'Caribbean small states', "Cameroon", "Burundi"]
ns_countries = ['United States', 'Canada', 'Venezuela', 'Peru', 'Mexico', 'Brazil']
eu_countries = ['Germany', 'Greece', 'Italy', 'Poland', 'Turkey', 'Sweden']
african_countries = ['Zimbabwe', 'Egypt', 'South Africa', 'Morocco', 'Chad', 'Niger']
asian_countries = ['China', 'North Korea', 'South Korea', 'Japan', 'India', 'Russia']

# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

# Plot the data on a line graph
countries = []
countries.append(ns_countries)
countries.append(eu_countries)
countries.append(african_countries)
countries.append(asian_countries)
for i in range (4):
  for c in unique_countries:
    if c in countries[i]:
      
      # match country to one of our we want to look at and get a list of years
      years = df[df['Entity'] == c]['Year']

      # match country to one of our we want to look at and get a list of electriciy values
      sum_elec = df[df['Entity'] == c]['Access']

      plt.plot(years, sum_elec, label=c, marker="8", linestyle="-")
  plt.ylabel('Percentage of Country Population')
  plt.xlabel('Year')
  plt.title('Percent of Population with Access to Electricity')
  plt.legend()
  plt.show()
