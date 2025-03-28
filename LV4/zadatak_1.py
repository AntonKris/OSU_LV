import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

"""
a) Odaberite željene numericke veli ˇ cine speci ˇ ficiranjem liste s nazivima stupaca. Podijelite
podatke na skup za ucenje i skup za testiranje u omjeru 80%-20%. ˇ
b) Pomocu matplotlib biblioteke i dijagrama raspršenja prikažite ovisnost emisije C02 plinova ´
o jednoj numerickoj veli ˇ cini. Pri tome podatke koji pripadaju skupu za u ˇ cenje ozna ˇ cite
"""

data = pd.read_csv("data_C02_emission.csv")

X = data[["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)", "Fuel Consumption Hwy (L/100km)", "Fuel Consumption Comb (L/100km)", "Fuel Consumption Comb (mpg)"]]
y = data["CO2 Emissions (g/km)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

plt.figure()

plt.scatter(X_train["Engine Size (L)"], y_train, color='blue', label='Training set')

plt.scatter(X_test["Engine Size (L)"], y_test, color='red', label='Test set')

plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("CO2 Emissions vs Engine Size")
plt.legend()

plt.show()

"""
c) Izvršite standardizaciju ulaznih velicina skupa za u ˇ cenje. Prikažite histogram vrijednosti ˇ
jedne ulazne velicine prije i nakon skaliranja. Na temelju dobivenih parametara skaliranja ˇ
transformirajte ulazne velicine skupa podataka za testiranje.
""" 

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.fit_transform(X_test)

print(f"Mean before scaling:\n{X_train.mean()}")
print(f"Standard Deviation before scaling:\n{X_train.std()}")
print(f"Mean after scaling:\n{X_train_scaled.mean(axis=0)}")
print(f"Standard Deviation after scaling:\n{X_train_scaled.std(axis=0)}")


plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(X_train["Engine Size (L)"], bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Engine Size (L) Before Scaling")
plt.xlabel("Engine Size (L)")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(X_train_scaled[:, 0], bins=20, color='green', edgecolor='black', alpha=0.7)
plt.title("Histogram of Engine Size (L) After Scaling")
plt.xlabel("Engine Size (L) (Scaled)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


"""
d) Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i
povežite ih s izrazom 4.6.
"""

model = LinearRegression()
model.fit(X_train_scaled, y_train)

print(f"Intercept (β0): {model.intercept_}")
print(f"Coefficients (β1, β2, ..., βn): {model.coef_}")


"""
e) Izvršite procjenu izlazne velicine na temelju ulaznih veli ˇ cina skupa za testiranje. Prikažite ˇ
pomocu dijagrama raspršenja odnos izme ´ du stvarnih vrijednosti izlazne veli ¯ cine i procjene ˇ
dobivene modelom
"""
model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred, color='red', label='Predicted vs Actual')

plt.xlabel('Actual CO2 Emissions (g/km)')
plt.ylabel('Predicted CO2 Emissions (g/km)')
plt.title('Actual vs Predicted CO2 Emissions')

plt.legend()

plt.show()

"""
f) Izvršite vrednovanje modela na nacin da izra ˇ cunate vrijednosti regresijskih metrika na ˇ
skupu podataka za testiranje
"""

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R²): {r2}")