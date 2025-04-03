import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import max_error
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv('data_C02_emission.csv')
 
ohe = OneHotEncoder()
encoder_df = pd.DataFrame(ohe.fit_transform(data[['Fuel Type']]).toarray()) 
data = data.join(encoder_df)

data.columns = ['Make','Model','Vehicle Class','Engine Size (L)','Cylinders','Transmission','Fuel Type','Fuel Consumption City (L/100km)','Fuel Consumption Hwy (L/100km)','Fuel Consumption Comb (L/100km)','Fuel Consumption Comb (mpg)','CO2 Emissions (g/km)','Fuel0', 'Fuel1', 'Fuel2', 'Fuel3']
y = data['CO2 Emissions (g/km)'].copy()
X = data.drop('CO2 Emissions (g/km)', axis=1)
X_train_all , X_test_all , y_train , y_test = train_test_split (X, y, test_size = 0.2, random_state =1)
 
X_train = X_train_all[['Engine Size (L)','Cylinders','Fuel Consumption City (L/100km)','Fuel Consumption Hwy (L/100km)','Fuel Consumption Comb (L/100km)','Fuel Consumption Comb (mpg)']]
X_test = X_test_all[['Engine Size (L)','Cylinders','Fuel Consumption City (L/100km)','Fuel Consumption Hwy (L/100km)','Fuel Consumption Comb (L/100km)','Fuel Consumption Comb (mpg)']]

linearModel = lm.LinearRegression()
linearModel.fit(X_train,y_train)
y_prediction = linearModel.predict(X_test)
 
plt.scatter(X_test['Fuel Consumption City (L/100km)'],y_test, c='b',label='Prave vrijednosti', s=5, alpha=0.5)
plt.scatter(X_test['Fuel Consumption City (L/100km)'],y_prediction, c='r',label='Predvidanja', s=5, alpha=0.5)
plt.xlabel('Fuel Consumption City (L/100km)')
plt.ylabel('CO2 Emissions (g/km)')
plt.legend()
plt.show()

maxError = max_error(y_test,y_prediction)
print(f"Maksimalna pogreška u procjeni: {maxError}")
vozilo_s_najvecom_greskom=X_test_all[abs(y_test-y_prediction) == maxError]['Model'].iloc[0]
print(f"Model vozila s maksimalnom pogreškom u procjeni: {vozilo_s_najvecom_greskom}")
