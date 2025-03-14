import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road.jpg")
img=img[:,:,0].copy()
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap="gray",vmax=50)
plt.show()

width = len(img[0])
quarterWidth = int(width/4)
plt.imshow(img[:,quarterWidth: 2*quarterWidth],cmap="gray")
plt.show()

rotatedImage = np.rot90(img)
plt.imshow(rotatedImage,cmap="gray")
plt.show()

flippedImage = np.flip(img)
plt.imshow(flippedImage,cmap="gray")
plt.show()