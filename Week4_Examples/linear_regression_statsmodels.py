import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

# create some data
#
# N.B.  In linear regression, there is a SINGLE y-value for each data point, but there
#       may be MULTIPLE x-values, corresponding to the multiple factors that might affect the
#       experiment, i.e. y = b_1 * x_1 + b_2 * x_2 + b_3 * x_3 + .....
#       Therefore, the x data is a TWO DIMENSIONAL array ... the columns correspond to the different
#       variables (x_1, x_2, x_3, ...), and the rows correspond to the values of those variables
#       for each data point.
#

df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'y': [1.1, 2.1, 2.9, 3.9, 5.1, 5.9, 6.9, 8.05, 9.1, 9.7] } )

print(df)

y = df['y']
X = df['x']
# X = sm.add_constant(X)

# Ordinary Least Squares model from statsmodels
model = sm.OLS(y, X).fit()

# View model summary
print(model.summary())

# Create prediction
y_pred = model.predict(X)

# Plotting!

plt.plot(df['x'], y, 'o', label='Data')
plt.plot(df['x'], y_pred, 'r-', label="Linear Regression Fit")
plt.title("Basic Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
