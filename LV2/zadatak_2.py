import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', delimiter=",", dtype="str")

data = np.loadtxt('data.csv', delimiter=",", dtype="str")
data = data[1:]
data = np.array(data, np.float64)
print("Amount of people measurred:",len(data))
height=data[:, 1] 
weight = data[:, 2]
plt.scatter(height, weight)
plt.show()

height=data[::50, 1] 
weight = data[::50, 2]
plt.scatter(height, weight)
plt.show()

minHeight=data[:,1].min()
meanHeight=data[:,1].mean()
maxHeight=data[:,1].max()
print("Minimal height:",minHeight,"cm")
print("Mean height:",meanHeight,"cm")
print("Maximal height:",maxHeight,"cm")


male=data[data[:,0]==1]
female=data[data[:,0]==0]

print(f"Minimal male height:{male[:,1].min()}cm")
print(f"Mean male height:{male[:,1].mean()}cm")
print(f"Maximal male height:{male[:,1].max()}cm")

print(f"Minimal female height:{female[:,1].min()}cm")
print(f"Mean female height:{female[:,1].mean()}cm")
print(f"Maximal female height:{female[:,1].max()}cm")