import matplotlib.pyplot as plt

crimes_list = []
with open("violent_crimes.txt", 'r') as f:
    for l in f:
        crimes_list.append(int(l))

dates = range(2000, 2020)

plt.plot(dates, crimes_list, 'o:r')
plt.title("Violent Crimes Throughout the 21st Century")
plt.xlabel("Time (Years)")
plt.ylabel("Crimes (Millions)")
plt.show()