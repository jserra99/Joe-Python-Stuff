'''The logic behind the Graph-Creator...'''
import matplotlib.pyplot as plt
import numpy as np

def create_graph(title, bar_names, bar_numbers, chart_type):
    '''Creates the graph'''
    plt.title(title) #Setting the title
    plt.xlabel(input("What would you like the horizontal label to be?: ")) #Setting the optional X Label
    plt.ylabel(input("What would you like the vertical label to be?: ")) #Setting the optional Y Label
    if (chart_type.lower() == 'pie'): #Checking the type of chart
        plt.pie(np.array(bar_numbers), labels = bar_names) #Setting the pie numbers and labels
        plt.show() #Showing the chart
    else: #If its not pie
        x = np.array(bar_names) #Setting the x value of the bar graph
        y = np.array(bar_numbers) #Setting the y value of the bar graph
        plt.bar(x,y) #Inserting the data
        plt.show() #Showing the graph

def get_input(chart_type):
    '''Gets the input for creating the graph'''
    bar_list = [] #Creating some empty lists
    bar_data = []
    if (chart_type.lower() == 'pie'): #Checking what type was chosen
        title = input("\nWhat do you want to be the title of your Pie-Chart?: ") #Pie chart title
        num_bars = int(input("How many slices of pie would you like in your chart?: ")) #Asking for the number of slices
        for i in range(num_bars): #For loop for each chosen num_bar
            bar_list.append(input(f"What do you want the label of slice number {i + 1} to be?: ")) #Getting Labels...
            bar_data.append(int(input(f"What do you want the data of {bar_list[i]} to be?: "))) #Getting Data...
    else: #If it was not 'pie':
        title = input("\nWhat do you want to be the title of your bar graph?: ") #Bar graph title
        num_bars = int(input("How many columns of data do you want in your graph?: ")) #Asking for the number of colums
        for i in range(num_bars): #For loop for each chosen num_bar
            bar_list.append(input(f"What do you want the label of bar number {i + 1} to be?: ")) #Getting Labels...
            bar_data.append(int(input(f"What do you want the data of {bar_list[i]} to be?: "))) #Getting Data...
    create_graph(title, bar_list, bar_data, chart_type) #Calling the function to create the graph
