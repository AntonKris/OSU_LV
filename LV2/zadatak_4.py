import numpy as np
import matplotlib.pyplot as plt

ones=np.ones((50,50))
zeros=np.zeros((50,50))

blackAndWhite=np.hstack((zeros,ones))
whiteAndBlack=np.hstack((ones,zeros))
combined=np.vstack((blackAndWhite,whiteAndBlack))
plt.figure()
plt.imshow(combined,cmap="gray")
plt.show()