import pandas as pd
data = pd.read_csv("data_C02_emission.csv")
#a)
print(len(data))
print("------------------------------------------------------------------------------------------------------")
print(data.dtypes)
print("------------------------------------------------------------------------------------------------------")
data['Vehicle Class'] = data['Vehicle Class'].astype('category')

print(f"Redovi s izostalim vrijednostima: {data.isnull().sum()}")
print(f"Duplicirane vrijednosti: {data.duplicated().sum()}")
print("------------------------------------------------------------------------------------------------------")

#b)
najmanja = data.sort_values(by='Fuel Consumption City (L/100km)', ascending=False).tail(3)
print(f"Najmanja gradska potrošnja:")
print(najmanja[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

najveca=data.sort_values(by="Fuel Consumption City (L/100km)",ascending=False).head(3)
print(f"Najveća gradska potrošnja:")
print(najveca[["Make","Model","Fuel Consumption City (L/100km)"]])
print("------------------------------------------------------------------------------------------------------")

#c)
inBetween=data[(data["Engine Size (L)"]>=2.5) & (data["Engine Size (L)"]<=3.5)]
print(f"{len(inBetween)} vozila ima velicinu motora između 2.5 i 3.5")
print(f"prosječna CO2 emisija ovih vozila je: {inBetween['CO2 Emissions (g/km)'].mean()}")
print("------------------------------------------------------------------------------------------------------")
#d)

audiMeasurements=data[data["Make"]=="Audi"]
print(f"na {len(audiMeasurements)} audi vozila su se provela mjerenja")

fourCyliderAudis=audiMeasurements[audiMeasurements["Cylinders"]==4]
print(f"prosječna emisija CO2 plinova Audi vozila sa 4 cilindra je: {fourCyliderAudis['CO2 Emissions (g/km)'].mean()}")
print("------------------------------------------------------------------------------------------------------")

#e)

cylinderAmount=data["Cylinders"].unique()
for typeofCylinder in cylinderAmount:
    amountOfCars=data[data["Cylinders"]==typeofCylinder]
    print(f"{typeofCylinder} cyliders:{len(amountOfCars)} cars, average CO2 emissions: {amountOfCars['CO2 Emissions (g/km)'].mean()}")
print("------------------------------------------------------------------------------------------------------")   

#f)
dizel=data[data['Fuel Type']=="D"]
benzin=data[data['Fuel Type']=="X"]

print(f"prosječna gradska potrošnja dizel vozila: {dizel['Fuel Consumption City (L/100km)'].mean()}")
print(f"prosječna gradska potrošnja vozila na regularni benzin: {benzin['Fuel Consumption City (L/100km)'].mean()}")

print(f"medijalna gradska potrošnja dizel vozila: {dizel['Fuel Consumption City (L/100km)'].median()}")
print(f"medijalna gradska potrošnja vozila na regularni benzin: {benzin['Fuel Consumption City (L/100km)'].median()}")
print("------------------------------------------------------------------------------------------------------")   

#g)

fourCylinderDiesel=data[(data["Cylinders"]==4)&(data["Fuel Type"]=="D")]
maxFourCylinderDiesel=fourCylinderDiesel[fourCylinderDiesel['Fuel Consumption City (L/100km)']==fourCylinderDiesel['Fuel Consumption City (L/100km)'].max()]
print("4 cilindrični dizel automobil s najvećom gradskom potrošnjom goriva je:")
print(maxFourCylinderDiesel[['Make','Model','Fuel Consumption City (L/100km)']])
print("------------------------------------------------------------------------------------------------------")  
#h)
manuals=data[data['Transmission'].str[0]=="M"]
print(f"Broj vozila sa ručnim mjenjačom je: {(len(manuals['Make']))}")
print("------------------------------------------------------------------------------------------------------")  
#i)
print(data.corr(numeric_only=True))

#Sto je negativna korelacija blize -1 to je ona vise obrnuto proporcijalna, dok sto je blize 1, to je vise proporcijonalna. Vrijednosti oko 0
#nemaju nikakvu korelaciju s velicinom.