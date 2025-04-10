from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn . metrics import confusion_matrix , ConfusionMatrixDisplay
from sklearn . linear_model import LogisticRegression
from sklearn . metrics import accuracy_score, precision_score, recall_score,classification_report
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np



X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#a)



plt.scatter(X_train[:, 0], X_train[:,1], label="trening", cmap="PiYG", c=y_train)
plt.scatter(X_test[:, 0], X_test[:, 1], label="test", cmap="PiYG", c=y_test,marker="*")

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Prikaz podataka u x1-x2 ravnini')
plt.legend()
plt.show()

#b)
# inicijalizacija i ucenje modela logisticke regresije
LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)
# predikcija na skupu podataka za testiranje
y_test_p = LogRegression_model.predict(X_test)

#c
w = LogRegression_model.coef_[0] #theta 1 i theta2
a = -w[0] / w[1]
xx = np.linspace(-4, 4)
yy = a * xx - (LogRegression_model.intercept_[0]) / w[1] 
print(LogRegression_model.intercept_[0])
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='PiYG')
plt.plot(xx, yy, 'k-')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Logistic Regression Decision Boundary')
plt.show()

#d
disp = ConfusionMatrixDisplay(confusion_matrix(y_test , y_test_p))
disp.plot()
plt.show()
print (" Tocnost : " , accuracy_score (y_test , y_test_p))
print(" Preciznost : ", precision_score(y_test, y_test_p))
print(" Odziv: ", recall_score(y_test, y_test_p))

#e
y1 = (y_test==y_test_p)
y0 = (y_test!=y_test_p)

X_false = []

for i in range(len(y_test)):
    if y_test[i] != y_test_p[i]:
        X_false.append([X_test[i, 0], X_test[i, 1]])

X_false = np.array(X_false)
print(X_false)

plt.scatter(X_test[:,0], X_test[:, 1],color='green')
plt.scatter(X_false[:,0], X_false[:,1], color='black')
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()






