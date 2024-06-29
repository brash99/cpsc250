import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np

# Read in the CSV file into a pandas DataFrame
file_name = 'EmissionsData.csv'
df = pd.read_csv(file_name)

# Perform linear regression CO2 vs. Volume
X1 = sm.add_constant(df['Volume'])  # Add constant term
model1 = sm.OLS(df['CO2'], X1).fit()
df['CO2_Volume_Fit'] = model1.fittedvalues
df['CO2_Volume_Residuals'] = df['CO2'] - df['CO2_Volume_Fit']

# Perform linear regression CO2_Volume_Residuals vs. Weight
X2 = sm.add_constant(df['Weight'])  # Add constant term
model2 = sm.OLS(df['CO2_Volume_Residuals'], X2).fit()
df['CO2_Weight_Fit'] = model2.fittedvalues
df['CO2_Weight_Residuals'] = df['CO2_Volume_Residuals'] - df['CO2_Weight_Fit']

# Create a 2x2 set of plots
fig, axes = plt.subplots(2, 2, figsize=(9, 9))
fig.tight_layout(pad=2.5)
#The plots was helped with the use of ChatGpt and Github Copilot
# Top left plot: CO2 vs. Volume
axes[0, 0].scatter(df['Volume'], df['CO2'], label='Data')
axes[0, 0].set_xlabel('Volume (mL)')
axes[0, 0].set_ylabel('CO2 Emissions (g/km)')
axes[0, 0].set_title('CO2 vs. Volume')
axes[0, 0].grid(True)

# Top right plot: CO2 vs. Weight
axes[0, 1].scatter(df['Weight'], df['CO2'], label='Data')
axes[0, 1].set_xlabel('Weight (kg)')
axes[0, 1].set_ylabel('CO2 Emissions (g/km)')
axes[0, 1].set_title('CO2 vs. Weight')
axes[0, 1].grid(True)

# Bottom left plot: CO2 vs. Volume with fit
axes[1, 0].scatter(df['Volume'], df['CO2'], label='Data')
axes[1, 0].plot(df['Volume'], df['CO2_Volume_Fit'], color='red', label='Fit')
axes[1, 0].set_xlabel('Volume (mL)')
axes[1, 0].set_ylabel('CO2 Emissions (g/km)')
axes[1, 0].set_title('CO2 vs. Volume with Fit')
axes[1, 0].legend()
axes[1, 0].grid(True)

# Bottom right plot: CO2_Volume_Residuals vs. Weight with fit
axes[1, 1].scatter(df['Weight'], df['CO2_Volume_Residuals'], label='Data')
axes[1, 1].plot(df['Weight'], df['CO2_Weight_Fit'], color='red', label='Fit')
axes[1, 1].set_xlabel('Weight (kg)')
axes[1, 1].set_ylabel('CO2 Volume Residuals (g/km)')
axes[1, 1].set_title('CO2 Volume Residuals vs. Weight with Fit')
axes[1, 1].legend()
axes[1, 1].grid(True)

plt.savefig('co2_emissions_analysis.png')
plt.show()

# Print summary information for each of the two linear regression models
print("Linear regression model for CO2 vs. Volume:")
print(model1.summary())

print("\nLinear regression model for CO2_Volume_Residuals vs. Weight:")
print(model2.summary())

# Interpretation of the results
if model1.pvalues['Volume'] < 0.05:
    print("CO2 emissions significantly depend on Volume.")
else:
    print("CO2 emissions do not significantly depend on Volume.")

if model2.pvalues['Weight'] < 0.05:
    print("CO2 emissions significantly depend on Weight after accounting for Volume.")
else:
    print("CO2 emissions do not significantly depend on Weight after accounting for Volume.")
