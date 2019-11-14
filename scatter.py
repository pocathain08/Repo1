#see online tutorial, Plotting with keyword strings
#Plot 4 dimentional data in 2 d
import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0.0, 10.0, 100)
y = np.random.uniform(0.0, 100.0, 100)
z = np.random.normal(100.0, 40.0, 100)
c = np.random.randint(0, 20, 100)
#Can shpw 4 dimentional data, (x, y, colour, size)

plt.scatter(x, y, c=c, s=z)

plt.show()