import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('car_emissions.csv')

# Perform linear regression of CO2 vs. Volume using statsmodels
model_volume = smf.ols(formula='CO2 ~ Volume', data=df).fit()

# Calculate residuals from CO2 vs. Volume regression
df['CO2_residuals'] = model_volume.resid

# Perform linear regression of CO2 residuals vs. Weight using statsmodels
model_weight = smf.ols(formula='CO2_residuals ~ Weight', data=df).fit()

# Create a 2x2 set of plots in a figure
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
fig.tight_layout(pad=2.5)
# Used chatgpt
# Top left plot - CO2 vs. Volume
axs[0, 0].scatter(df['Volume'], df['CO2'])
axs[0, 0].set_xlabel('Volume (mL)')
axs[0, 0].set_ylabel('CO2 Emissions')
axs[0, 0].set_title('CO2 vs. Volume')

# Top right plot - CO2 vs. Weight
axs[0, 1].scatter(df['Weight'], df['CO2'])
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions')
axs[0, 1].set_title('CO2 vs. Weight')

# Bottom left plot - CO2 vs. Volume with regression line
axs[1, 0].scatter(df['Volume'], df['CO2'])
axs[1, 0].plot(df['Volume'], model_volume.predict(), color='red', label='Linear Fit')
axs[1, 0].set_xlabel('Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions')
axs[1, 0].set_title('CO2 vs. Volume with Linear Fit')
axs[1, 0].legend()

# Bottom right plot - CO2 residuals vs. Weight with regression line
axs[1, 1].scatter(df['Weight'], df['CO2_residuals'])
axs[1, 1].plot(df['Weight'], model_weight.predict(), color='red', label='Linear Fit')
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Residuals')
axs[1, 1].set_title('CO2 Residuals vs. Weight with Linear Fit')
axs[1, 1].legend()

# Print model summaries
print("Linear Regression Summary for CO2 vs. Volume:")
print(model_volume.summary())
print("\nLinear Regression Summary for CO2 Residuals vs. Weight:")
print(model_weight.summary())

# Display the plot
plt.show()

# Print completion message
print("Completed")