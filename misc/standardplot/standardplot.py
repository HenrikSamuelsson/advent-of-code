"""
Test program that uses imported packages to plot a sine graph.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers.
plt.plot(x, np.sin(x))       # Plot the sine of each number in the list.
plt.show()                   # Display the plot.
