import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# In this example, we will use the data in testdata.csv
# to perform a basic linear regression analysis, and compare
# the results to the quadratic and exponential fits from
# the previous examples.
#
# N.B.  In linear regression, there is a SINGLE y-value for each data point, but there
#       may be MULTIPLE x-values, corresponding to the multiple factors that might affect the
#       experiment, i.e. y = b_1 * x_1 + b_2 * x_2 + b_3 * x_3 + .....
#       Therefore, the x data is a TWO DIMENSIONAL array ... the columns correspond to the different
#       variables (x_1, x_2, x_3, ...), and the rows correspond to the values of those variables
#       for each data point.
#

df = pd.read_csv("testdata.csv")
df['Pollen_Count'] = df['Pollen Count']
df['Error_in_Pollen_Count'] = df['Error in Pollen Count']
df['Error_in_Temperature'] = df['Error in Temperature']
df.info()

# Step 1:  Identify the dependent and independent variables
y = df['Pollen_Count']
X = df['Temperature']
dy = df['Error_in_Pollen_Count']
dX = df['Error_in_Temperature']

# Step 2:  Add a constant to the independent variable
X = sm.add_constant(X)

#print(y)
#print(X)

# Step 3: Fit the data
fit_type = 3

if fit_type == 1:
    # Ordinary LINEAR Least Squares model from statsmodels
    model = sm.OLS(y, X).fit()
    fit_model = 'OLS Linear' # stored for use in plot legend
elif fit_type == 2:
    model = smf.ols(formula='Pollen_Count ~ Temperature + I(Temperature**2)', data = df).fit()
    fit_model = 'OLS Quadratic'
elif fit_type == 3:
    model = smf.wls(formula = 'Pollen_Count ~ Temperature + I(Temperature**2)',data = df,weights = 1/(dy**2)).fit()
    fit_model = 'WLS Quadratic'
else:
    print("Invalid fit type")
    exit()

# Step 4: View model summary
print(model.summary())

# Step 5: Create prediction
y_pred = model.predict(X)
#print(y_pred)

# Step 6: Plotting!

do_plot = True

if do_plot:
    plt.errorbar(df['Temperature'], y, yerr=df['Error_in_Pollen_Count'],
                 xerr = df['Error_in_Temperature'], fmt='o', label='Pollen Count Data',
                 capsize=5.0)
    plt.plot(df['Temperature'], y_pred, 'r-', label=fit_model)
    plt.title("Basic Linear Regression")
    plt.xlabel("Temperature")
    plt.ylabel("Pollen Count")
    plt.legend()
    plt.show()
