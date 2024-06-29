import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np


# Load the CSV file
df = pd.read_csv('EmissionsData.csv')


# Create the 2x2 plot grid
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
plt.tight_layout(pad=2.5)
fig.suptitle('Dependency of CO2 Emissions on Car Engine Volume and Weight', y=1.05)


# Top left plot: CO2 emissions vs. Engine Volume
axs[0, 0].scatter(df['Engine Volume'], df['CO2 Emissions'])
axs[0, 0].set_xlabel('Engine Volume (mL)')
axs[0, 0].set_ylabel('CO2 Emissions')


# Top right plot: CO2 emissions vs. Weight
axs[0, 1].scatter(df['Weight'], df['CO2 Emissions'])
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions')


# Linear regression for CO2 vs. Volume
X = df[['Engine Volume']]
y = df['CO2 Emissions']
X = sm.add_constant(X)  # Adds a constant term to the predictor


model = sm.OLS(y, X).fit()
df['Volume_Predicted'] = model.predict(X)
df['Volume_Residuals'] = df['CO2 Emissions'] - df['Volume_Predicted']


# Lower left plot: CO2 vs. Volume with regression line
axs[1, 0].scatter(df['Engine Volume'], df['CO2 Emissions'], label='Data')
axs[1, 0].plot(df['Engine Volume'], df['Volume_Predicted'], color='orange', label='Prediction')
axs[1, 0].set_xlabel('Engine Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions')
axs[1, 0].legend()


# Linear regression for CO2VolumeResiduals vs. Weight
X_res = df[['Weight']]
y_res = df['Volume_Residuals']
X_res = sm.add_constant(X_res)  # Adds a constant term to the predictor


model_res = sm.OLS(y_res, X_res).fit()
df['Weight_Predicted_Residuals'] = model_res.predict(X_res)
df['Weight_Residuals'] = df['Volume_Residuals'] - df['Weight_Predicted_Residuals']


# Lower right plot: CO2VolumeResiduals vs. Weight with regression line
axs[1, 1].scatter(df['Weight'], df['Volume_Residuals'], label='Data')
axs[1, 1].plot(df['Weight'], df['Weight_Predicted_Residuals'], color='orange', label='Prediction')
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Emissions vs. Volume Residuals')
axs[1, 1].legend()


# Print summary information
print("Linear Regression CO2 vs. Volume")
print(model.summary())
print("\nLinear Regression CO2VolumeResiduals vs. Weight")
print(model_res.summary())


plt.show()

