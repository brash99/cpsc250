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

# Step 1:  Identify the dependent and independent variables
y = df['y']
X = df['x']

# Step 2:  Add a constant to the independent variable
X = sm.add_constant(X)

# Step 3: Ordinary Least Squares model from statsmodels
# model is a complex object returned by the fit() method
# model contains all of the results of the regression fit
model = sm.OLS(y, X).fit()

# Step 4: View model summary
print(model.summary())

# Step 5: Create prediction
y_pred = model.predict(X)

# Step 6: Plotting!

plt.plot(df['x'], y, 'o', label='Data')
plt.plot(df['x'], y_pred, 'r-', label="Linear Regression Fit")
plt.title("Basic Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
