import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read the CSV file into a pandas DataFrame
filename = 'EmissionsData.csv'
df = pd.read_csv(filename)

# Make a 2x2 set of plots in a figure
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
fig.suptitle('CO2 Emissions Analysis', fontsize=16)
fig.tight_layout(pad=2.5)

# complete linear regression and plot the answers
# Fit 1: CO2 vs. Volume
model1 = sm.OLS(df['CO2'], sm.add_constant(df['Volume']))
result1 = model1.fit()

# parameters and residuals
beta0, beta1 = result1.params
CO2_fit = beta0 + beta1 * df['Volume']
CO2_residuals = df['CO2'] - CO2_fit

# Plot 1 is CO2 vs. Volume
axs[0, 0].scatter(df['Volume'], df['CO2'], label='Data')
axs[0, 0].plot(df['Volume'], CO2_fit, color='red', label=f'Fit: CO2 = {beta0:.2f} + {beta1:.2f} * Volume')
axs[0, 0].set_xlabel('Volume (mL)')
axs[0, 0].set_ylabel('CO2 Emissions (g/km)')
axs[0, 0].legend()

# Fit 2: CO2VolumeResiduals vs. Weight
model2 = sm.OLS(CO2_residuals, sm.add_constant(df['Weight']))
result2 = model2.fit()

# Extracting parameters and residuals
beta2 = result2.params[1]
CO2_residuals_fit = beta2 * df['Weight']

# Plot 2 is CO2 vs. Weight
axs[0, 1].scatter(df['Weight'], df['CO2'], label='Data')
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions (g/km)')
axs[0, 1].legend()

# Plot 3 is CO2 vs. Volume for confirmation
axs[1, 0].scatter(df['Volume'], df['CO2'], label='Data')
axs[1, 0].plot(df['Volume'], CO2_fit, color='red', label=f'Fit: CO2 = {beta0:.2f} + {beta1:.2f} * Volume')
axs[1, 0].set_xlabel('Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions (g/km)')
axs[1, 0].legend()

# Plot 4 is CO2VolumeResiduals vs. Weight
axs[1, 1].scatter(df['Weight'], CO2_residuals, label='Data')
axs[1, 1].plot(df['Weight'], CO2_residuals_fit, color='red', label=f'Fit: CO2Residuals = {beta2:.2f} * Weight')
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Residuals')
axs[1, 1].legend()

# Print info for each regression model
print("Summary of Linear Regression Models:")
print(result1.summary())
print(result2.summary())

# Interpretation
print("\nInterpretation:")
print(f"CO2 emissions dependence on Volume: beta1 = {beta1:.2f}")
print(f"CO2 emissions dependence on Weight (after Volume effect): beta2 = {beta2:.2f}")

# show the plots
plt.show()
