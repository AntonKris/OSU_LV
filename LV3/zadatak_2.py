import pandas as pd 
import matplotlib.pyplot as plt
#a)
data = pd.read_csv("data_C02_emission.csv")
plt.figure()
data["CO2 Emissions (g/km)"].plot(kind="hist", bins = 20)
plt.show()
# preko histrogama možemo vidjeti da u prosjeku najviše vozila proizvodi između 200 i 300 g/km CO2 emisija

#b)
colors={'Z':'brown','X':'green','E':'yellow','D':'black','N':'pink'}
data.plot.scatter(x='Fuel Consumption City (L/100km)',y='CO2 Emissions (g/km)',c=data['Fuel Type'].map(colors))
plt.show()
#iz dijagrama raspršenja možemo vidjeti kako se ističu vozila koja voze na ethanol jer proizvode znatno manje CO2 emisija

#c)

data.boxplot(column=["Fuel Consumption Hwy (L/100km)"], by="Fuel Type")
plt.show()
#Postoji gruba mjerna pogreška kod premium benzina gdje neka vozila, koja koriste premium benzin, troše znatno više u usporedbu s drugima

#d)
brojVozila=data.groupby('Fuel Type').size()
brojVozila.plot(kind ='bar', xlabel='Fuel Type', ylabel='Number of vehicles', title='Amount of vehicles by fuel type')
plt.show()

#e)
cylinder_grouped = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
cylinder_grouped.plot(kind='bar', x=cylinder_grouped.index, y=cylinder_grouped.values, xlabel='Cylinders', ylabel='CO2 emissions (g/km)', title='Mean CO2 emissions by number of cylinders')
plt.show()

