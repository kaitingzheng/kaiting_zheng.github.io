import matplotlib.pyplot as plt
import os.path

# Naming the current directory
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'here.csv')
datafile = open(filename,'r') # 'r' means 'read-only'
data = datafile.readlines()

#Initialize aggregators
cities = []  
crimes = []
incomes = []

#Populate the lists with the data
for line in data[1:]:
    city, crime, income = line.split(',')
    
    # If the name matches...
    if income != '\n':
        # Add thevalues to the lists
        crimes.append(crime)
        cities.append(city)
        incomes.append(income)

datafile.close()

#Creates the graph
fig, ax = plt.subplots(1,1)
ax.scatter(incomes,crimes)

#Changes graph labels
ax.set_ylabel('Number of Violent Crimes')
ax.set_xlabel('Median Income (USD)')
ax.set_title('Violent Crime by Median Income')

for i, txt in enumerate(cities):
    ax.annotate(txt, (incomes[i],crimes[i]))

fig.show()


