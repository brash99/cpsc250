import matplotlib.pyplot as plt

# main point!!!
# We need a list of x-values and a list of y-values to plot


# Create a list of x values
x = [1, 2, 3, 4, 5]

# Create a list of y values
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# Create a plot of x and y values
plt.plot(x, y1, 'bo-', label='y = x^2')
plt.plot(x, y2, 'r^-', label='y = x')
plt.legend()
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Brash Requirements for Plots by Students')




plt.show()
