import logic
print("\n<-- Welcome to Graph-Creator! -->")
while True: #Loop that will keep the program going to create more graphs
    chart_type = input("What type of graph would you like to create? (Pie / Bar): ") #Getting the chart type whether it be a pie chart or bar graph
    logic.get_input(chart_type) #Running the main input function and creating the graph
    if(input("Would you like to create another graph? (Yes or No): ").lower() == 'yes'): #Asking if the user wants another chart
        print("Restarting prompts...")
    else:
        break
