import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

# Chatgpt was used
# Step 1: Read in the CSV file into a pandas DataFrame
file_name = 'EmissionsData.csv'
df = pd.read_csv(file_name)

# Step 2: Fit a linear regression model to explore CO2 vs. Volume relationship
model_volume = smf.ols(formula='CO2 ~ Volume', data=df).fit()

# Step 3: Fit a linear regression model to explore CO2 residuals vs. Weight relationship
# First, compute CO2 residuals from the Volume model
df['CO2_residuals_volume'] = model_volume.resid

# Fit the second model: CO2_residuals_volume vs. Weight
model_weight = smf.ols(formula='CO2_residuals_volume ~ Weight', data=df).fit()

# Step 4: Create plots to visualize the results
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.tight_layout(pad=3.0)

# Plot CO2 vs. Volume
axs[0, 0].scatter(df['Volume'], df['CO2'], alpha=0.5)
axs[0, 0].set_xlabel('Volume (mL)')
axs[0, 0].set_ylabel('CO2 Emissions')
axs[0, 0].set_title('CO2 Emissions vs. Volume')

# Plot CO2 vs. Weight
axs[0, 1].scatter(df['Weight'], df['CO2'], alpha=0.5)
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions')
axs[0, 1].set_title('CO2 Emissions vs. Weight')

# Plot CO2 vs. Volume with regression line
axs[1, 0].scatter(df['Volume'], df['CO2'], alpha=0.5)
axs[1, 0].plot(df['Volume'], model_volume.predict(df['Volume']), color='red')
axs[1, 0].set_xlabel('Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions')
axs[1, 0].set_title('CO2 Emissions vs. Volume with Fit')

# Plot CO2_residuals_volume vs. Weight with regression line
axs[1, 1].scatter(df['Weight'], df['CO2_residuals_volume'], alpha=0.5)
axs[1, 1].plot(df['Weight'], model_weight.predict(df['Weight']), color='red')
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Residuals from Volume')
axs[1, 1].set_title('CO2 Residuals vs. Weight with Fit')

# Show plots
plt.show()

print("Completed")