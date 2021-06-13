''' https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/fe9ab7571a5e4c968d6f74caa30b371a 
TODO:
Use pandas to load and cleanse the data.
Use matplotlib to visually represent the data using the appropriate chart.
Calculate applicable statistical analytics (max, min, average).
Use iteration.
Include conditional logic.
Modularize your code with user-defined procedures.
Choose descriptive variable names.
Comment code segments or blocks of statements.
Hypothesis: The more developed countries covid cases are decreasing while the less developed countries covid cases are increasing.
'''
from matplotlib import pyplot as plt; import numpy as np; import pandas as pd;  # Imports

df = pd.read_csv("cases_and_vaccinations.csv") # Setting the data to a dataframe 
df = df.dropna(subset=['new_cases']) # Dropping any rows that do not contain new cases
df['new_cases'] = pd.to_numeric(df['new_cases']) # Not sure if this is necessary
templist = pd.date_range(start='2021-01-01', end='2021-06-01').tolist() # Generating a daterange from january 1st to june 1st
datelist = [] # Creating an empty list
for bruh_moment in templist: # for loop 
    new_moment = str(bruh_moment).rstrip(' 00:00:00') # Stripping the timestamp off of the dates
    datelist.append(new_moment) # Adding the stripped text to a new list
df = df[df['date'].isin(datelist)] # Removing all rows that are not dated 2021-01-01 -> 2021-06-01

unique_countries = df['location'].unique() # Maps all of the countries into a dataframe list
developed_countries = ['United States', 'Canada', 'United Kingdom', 'New Zealand', 'Norway', "Ireland"] # List of developed countries for comparison
developing_countries = ['India', 'Brazil', 'Colombia', 'Indonesia', 'Iraq', 'Argentina'] # List of developing countries for comparison

'''
Psuedocode:
Get total new cases per day data on the listed countries
X - Axis will be days but listed as months
Y - Axis will be total new cases averaged as a percentage of the total population
'''

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5), sharey=True, sharex=True) # Painful way of generating subplots
for c in unique_countries: # Iterating through the unique countries list
    if c in developed_countries: # Checking if the given country is developed or not
        dates = df[df['location'] == c]['date'] # Assigning that row's date to a variable
        sum_new_cases = df[df['location'] == c]['new_cases_smoothed_per_million'] # Assigning that row's cases to a variable
        # plt.plot(dates, sum_new_cases, label=c, linestyle="-")
        ax1.plot(dates, sum_new_cases, label=c) # Adding it to the developed countries plot
    elif c in developing_countries: # Checking if the given country is developing or not
        developing_dates = df[df['location'] == c]['date'] # Assigning that row's date to a variable
        developing_sum_new_cases = df[df['location'] == c]['new_cases_smoothed_per_million'] # Assigning that row's cases to a variable
        ax2.plot(developing_dates, developing_sum_new_cases, label=c) # Adding it to the developign countries plot

months = ["January","February","March","April", "May","June"] # Months used for the label
fig.suptitle('Developed vs Developing Country New Cases Over Time') # Setting the figure title
l = len(datelist) / 6 # Figuring out the intervals for the ticks
n = 6 # Used as a divider
a = (np.arange(n)) # Stupid way of doing this
x = l*a # No idea why this is needed but without it, it wont work
ax1.title.set_text('Developed Countries') # Ax1 title
ax2.title.set_text('Developing Countries') # Ax2 title
ax1.legend() # Ax1 legend
ax2.legend() # Ax2 legend
ax1.xaxis.set_ticks(x) # Setting the Ax1/Ax2 tick intervals
ax1.xaxis.set_ticklabels(months) # Setting the Ax1/Ax2 tick labels
ax1.set_xlabel("Time (Months)") # These next 4 lines are pretty self explanatory
ax2.set_xlabel("Time (Months)")
ax1.set_ylabel("New Cases (Millions)")
ax2.set_ylabel("New Cases (Millions)")
plt.show() # Showing the plot.
