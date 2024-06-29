import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the CSV data
file_path = r'C:\Users\blake\PycharmProjects\cpsc250\Tests\EmissionsData.csv'
df = pd.read_csv(file_path)

# Extract variables
Volume = df['Volume']
Weight = df['Weight']
CO2 = df['CO2']

# Perform linear regression manually for CO2 vs. Volume
X_volume = np.column_stack((np.ones(len(Volume)), Volume))
beta_volume = np.linalg.lstsq(X_volume, CO2, rcond=None)[0]
CO2_fit_volume = np.dot(X_volume, beta_volume)
CO2_residuals_volume = CO2 - CO2_fit_volume

# Perform linear regression manually for CO2_residuals_volume vs. Weight
X_weight = np.column_stack((np.ones(len(Weight)), Weight))
beta_weight = np.linalg.lstsq(X_weight, CO2_residuals_volume, rcond=None)[0]
CO2_fit_residuals_weight = np.dot(X_weight, beta_weight)

# Create a 2x2 plot figure
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
fig.tight_layout(pad=2.5)

# Top left plot: CO2 vs. Volume
axs[0, 0].scatter(Volume, CO2, alpha=0.8)
axs[0, 0].set_xlabel('Volume (mL)')
axs[0, 0].set_ylabel('CO2 Emissions')

# Top right plot: CO2 vs. Weight
axs[0, 1].scatter(Weight, CO2, alpha=0.8)
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions')

# Bottom left plot: CO2 vs. Volume with regression line
axs[1, 0].scatter(Volume, CO2, alpha=0.8)
axs[1, 0].plot(Volume, CO2_fit_volume, color='red', linewidth=1)
axs[1, 0].set_xlabel('Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions')

# Bottom right plot: CO2_residuals_volume vs. Weight with regression line
axs[1, 1].scatter(Weight, CO2_residuals_volume, alpha=0.8)
axs[1, 1].plot(Weight, CO2_fit_residuals_weight, color='red', linewidth=1)
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Volume Residuals')

# Print regression results (coefficients)
print("=== Regression Coefficients ===")
print("CO2 vs. Volume:")
print("Intercept (beta0):", beta_volume[0])
print("Slope (beta1):", beta_volume[1])
print("\nCO2VolumeResiduals vs. Weight:")
print("Intercept (beta0):", beta_weight[0])
print("Slope (beta2):", beta_weight[1])

plt.show()
