#See 2 individual plots

import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 2, 1)
#1 row 2 cols and this is the first plot
x = np.random.normal(0.0, 1.0, 1000)
plt.hist(x, bins=20)

plt.subplot(1, 2, 2)
#want 1 row, 2 columns and select the second plot
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x)

plt.show()