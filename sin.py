#See online tutorial 

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2.0 * np.pi, 2.0* np.pi, 0.1)
#Plot between -2pi and 2pi

plt.plot(x, np.sin(x), 'g.')
plt.plot(x, np.cos(x), 'b.')

plt.show()