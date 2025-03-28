import pandas as pd 
import matplotlib . pyplot as plt

data = pd.read_csv("data_C02_emission.csv")


#a)
print("a)")
length = len(data)
print(f"DataFrame ima {length} mjerenja")

print(f"tipovi podataka:{data.dtypes}")

print(f"Redovi s izostalim vrijednostima: {data.isnull().sum()}")

print(f"Duplicirane vrijednosti: {data.duplicated().sum()}")

#b)
print("b)")
largest = data.sort_values(by='Fuel Consumption City (L/100km)', ascending=False).head(3)
print(f"Najveća gradska potrošnja:")
print(largest[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

largest = data.sort_values(by='Fuel Consumption City (L/100km)', ascending=False).tail(3)
print(f"Najmanja gradska potrošnja:")
print(largest[['Make', 'Model', 'Fuel Consumption City (L/100km)']])


#c)
print("c)")
cars = data[(data['Engine Size (L)'] > 2.5) & (data['Engine Size (L)'] < 3.5)]
print(f"Broj automobila s motorom između 2.5 i 3.5 L: {len(cars)}")
print(f"Prosječna CO2 emisija: {cars['CO2 Emissions (g/km)'].mean()}")

#d)
print("d)")
audi = data[data['Make'] == 'Audi']
print(f"Broj Audi automobila: {len(audi)}")

four_cylinder_audi = audi[audi['Cylinders'] == 4]
print(f"Prosječna CO2 emisija za Audi automobila s 4 cilindra: {four_cylinder_audi['CO2 Emissions (g/km)'].mean()}")

#e)
print("e)")
cylinder_amount = data['Cylinders'].unique()
for cylinder in cylinder_amount:
     auto_cylinders = data[data['Cylinders'] == cylinder]
     print(f"Broj automobila s {cylinder} cilindara: {len(auto_cylinders)}")
     print(f"Prosječna CO2 emisija: {auto_cylinders['CO2 Emissions (g/km)'].mean()}")

#f
print("f)")
disel = data[data["Fuel Type"] == "D"]
petrol = data[data["Fuel Type"] == "Z"]

print(f"Prosječna gradska potrošnja dizel vozila: {disel["Fuel Consumption City (L/100km)"].mean()}")
print(f"Medijalna vrijednost dizel vozila: {disel["Fuel Consumption City (L/100km)"].median()}")

print(f"Prosječna gradska potrošnja benzin vozila: {petrol["Fuel Consumption City (L/100km)"].mean()}")
print(f"Medijalna vrijednost benzin vozila: {petrol["Fuel Consumption City (L/100km)"].median()}")

#g
print("g)")

four_cylinder_diesel=data[(data["Cylinders"] == 4)&(data["Fuel Type"]=="D")].max()
print(four_cylinder_diesel)

#h
print("h)")

manual_transmission= data[data['Transmission'].str.contains('AS')]
print(f"Broj vozila s ručnim mjenjačem: {len(manual_transmission)}")

#i
print("i)")
numeric = ['Engine Size (L)', 'Cylinders', 'Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)', 'Fuel Consumption Comb (L/100km)', 'CO2 Emissions (g/km)']
corr = data[numeric].corr()
print("Korelacija numeričkih veličina:")
print(corr)
