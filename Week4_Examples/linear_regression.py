import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# create some data
#
# N.B.  In linear regression, there is a SINGLE y-value for each data point, but there
#       may be MULTIPLE x-values, corresponding to the multiple factors that might affect the
#       experiment, i.e. y = b_1 * x_1 + b_2 * x_2 + b_3 * x_3 + .....
#       Therefore, the x data is a TWO DIMENSIONAL array ... the columns correspond to the different
#       variables (x_1, x_2, x_3, ...), and the rows correspond to the values of those variables
#       for each data point.
#
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# print(x)
# print(y)

# Linear Regression Model from scikit-learn
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)

print(f"Correlation coefficient R^2: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")

x_low = min(x)
x_high = max(x)
x_pred = np.linspace(x_low, x_high, 100)
y_pred = model.predict(x_pred)
# print (y_pred)


# Plotting!

plt.plot(x, y, 'o', label='Data')
plt.plot(x_pred, y_pred, 'r-', label="Linear Regression Fit")
plt.title("Basic Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
