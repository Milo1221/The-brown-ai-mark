import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

n = 50
x = np.random.rand(n)
y = np.random.rand(x)
colors = np.random.rand(n)
area = (30 * np.random.rand(n)) **2

plt.scatter(x,y, s=area, c=colors, alpha=0.5)
plt.show()