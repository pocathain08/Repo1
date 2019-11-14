#plotting two different things on the same axis

import matplotlib.pyplot as plt
import numpy as np

x =np.arange(0.0, 10.0, 0.01)
#list of integers in a range but not the last number eg np.arange (0.0, 10.0, 0.01) = list 0.0, 0.1, 0.2, ....
y = 3.0*x + 1.0
noise = np.random.normal(0.0, 1.0, len(x)) #normal distribution


plt.plot(x, y + noise, 'r.') # x vs y plotted in red dots

plt.plot(x, y, 'b-') # x vs y plotted in a blue straight line. Will remember what was previously plotted


#plt.ylabel("Some numbers")
#plt.xlabel("Another number")
plt.show() #shows figures and cleans slate, i.e. remembers if plot and plot.show commands called.


