"""The following program is intended to read in the data from EmissionsData.csv,
which should contain the make, mode, engine volume (mL), engine weight (kg), and CO2 emissions of various cars.
The program then carries out linear regression fits for CO2 vs. Volume and CO2vsVolumeResiduals vs. Weight,
plots the data and the linear regression fits, outputs the summary information for each of the two linear regression
models, and interprets their results.
The program was created with the help of ChatGPT and with substantial references to
linear_regression_statsmodels_multifactor.py."""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# Step 1: Read in the CSV file into a pandas DataFrame
df = pd.read_csv('EmissionsData.csv')

# Step 2: Create a 2x2 set of plots in a 9x9 inches figure
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
# with tight layout padding of 2.5 around each plot
plt.tight_layout(pad=2.5)
# and a super title matching the example figure
fig.suptitle("Dependency of CO2 Emissions on Car Volume and Weight")

# Step 3A: Plot CO2 emissions vs. Volume in top left plot
axs[0, 0].scatter(df['Volume'], df['CO2'])
# The independent variable and therefore the x-axis for this graph is the engine volume in mL
axs[0, 0].set_xlabel('Engine Volume (mL)')
# The dependent variable and therefore the y-axis for this graph and all others is CO2 Emissions (no unit given)
axs[0, 0].set_ylabel('CO2 Emissions')

# Step 3B: Plot CO2 emissions vs. Weight in top right plot
axs[0, 1].scatter(df['Weight'], df['CO2'])
# The independent variable and therefore the x-axis for this graph is the engine weight in kg
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions')

# Step 4A: Carry out a linear regression fit of CO2 vs. Volume
model_volume = smf.ols('CO2 ~ Volume', data=df).fit()
# Step 4B: Store the results of this fit in the data frame
df['CO2_predicted_volume'] = model_volume.predict(df['Volume'])
# Step 4C: Store the residuals of the fit in the data frame
df['CO2_residuals_volume'] = df['CO2'] - df['CO2_predicted_volume']

# Step 5: In the lower left plot, display the data for CO2 vs. Volume and the linear regression fit
# Display the data (label as 'Data' in legend)
axs[1, 0].scatter(df['Volume'], df['CO2'], label='Data')
# Display the linear regression line (label as 'Prediction' in legend and color orange)
axs[1, 0].plot(df['Volume'], df['CO2_predicted_volume'], color='orange', label='Prediction')
# The independent variable and therefore the x-axis for this graph is the engine volume in mL
axs[1, 0].set_xlabel('Engine Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions')
# Display the legend (In the example figure the legend is in the upper right.
# For this graph that is the best place and therefore the default, so no extra parameters need to be given.)
axs[1, 0].legend()

# Step 6A: Carry out a linear regression fit to the CO2vsVolumeResiduals vs. Weight
model_weight = smf.ols('CO2_residuals_volume ~ Weight', data=df).fit()
#  Step 6B: Store the results of this fit in the data frame
df['CO2_residuals_predicted_weight'] = model_weight.predict(df['Weight'])
# Step 6C: Store the new residuals in the data frame
df['CO2_residuals_volume_weight'] = df['CO2_residuals_volume'] - df['CO2_residuals_predicted_weight']

# Step 7: In the lower right plot, display the data for C02vsVolumeResiduals vs. Weight
# and the second linear regression fit
# Display the data (label as 'Data' in legend)
axs[1, 1].scatter(df['Weight'], df['CO2_residuals_volume'], label='Data')
# Display the linear regression line (label as 'Prediction' in legend and color orange)
axs[1, 1].plot(df['Weight'], df['CO2_residuals_predicted_weight'], color='orange', label='Prediction')
# The independent variable and therefore the x-axis for this graph is the engine weight in kg
axs[1, 1].set_xlabel('Weight (kg)')
# The dependent variable and therefore the y-axis for this graph is the CO2 Residuals (from the engine volume)
axs[1, 1].set_ylabel('CO2 Emissions vs. Volume Residuals')
# Display the legend (In the example figure the legend is in the upper center.
# For this graph that is the best place and therefore the default, so no extra parameters need to be given.)
axs[1, 1].legend()

# Display plots
plt.show()

# Step 8A: Print summary information for each linear regression model
print("Summary of CO2 vs. Volume Regression:")
print(model_volume.summary())
print("\nSummary of CO2_Residuals_Volume vs. Weight Regression:")
print(model_weight.summary())

#  Step 8B: Report on your interpretation of the results from these two models
# Step 8B1: For CO2 vs. Volume, is the intercept / baseline level of CO2 significant?
print(f"\nThe p-value for Intercept in CO2 vs. Volume regression is approximately "
      f"{model_volume.pvalues['Intercept']:.6f},")
if model_volume.pvalues['Intercept'] < 0.05:
    print(f"which is less than 0.05, which is statistically significant.\n"
          f"This indicates that there is a baseline level of CO2 emissions, \n"
          f"which is approximately {model_volume.params['Intercept']:.6f}.")
else:
    print(f"which is greater than or equal to 0.05, which is not statistically significant.\n"
          f"This indicates that there is not a baseline level of CO2 emissions.")

# Step 8B2: For CO2 vs. Volume, is the CO2-volume relationship significant?
print(f"\nThe p-value for Volume in CO2 vs. Volume regression is approximately "
      f"{model_volume.pvalues['Volume']:.6f},")
if model_volume.pvalues['Volume'] < 0.05:
    print(f"which is less than 0.05, which is statistically significant.\n"
          f"This indicates that CO2 emissions are dependent on engine volume.\n"
          f"For every mL of engine volume, CO2 emissions increase by approximately "
          f"{model_volume.params['Volume']:.6f}.")
else:
    print(f"which is greater than or equal to 0.05, which is not statistically significant.\n"
          f"This indicates that CO2 emissions are not dependent on engine volume.")

# Step 8B3: For CO2 residuals of volume vs. Weight, is the intercept / baseline level of CO2 significant?
print(f"\nThe p-value for Intercept in CO2_Residuals_Volume vs. Weight regression is approximately "
      f"{model_weight.pvalues['Intercept']:.6f},")
if model_weight.pvalues['Intercept'] < 0.05:
    print(f"which is less than 0.05, which is statistically significant.\n"
          f"This indicates that, after subtracting out the effect of engine volume on CO2 emissions\n"
          f"as well as the previous baseline level, there is another baseline level of CO2 emissions, \n"
          f"which is approximately {model_weight.params['Intercept']:.6f}.")
else:
    print(f"which is greater than or equal to 0.05, which is not statistically significant.\n"
          f"This indicates that, after subtracting out the effect of engine volume on CO2 emissions\n"
          f"as well as the previous baseline level, there is not another baseline level of CO2 emissions.")

# Step 8B4: For CO2 residuals of volume vs. Weight, is the CO2 residuals-volume relationship significant?
print(f"\nThe p-value for Weight in CO2 residuals of volume vs. Weight regression is approximately"
      f" {model_weight.pvalues['Weight']:.6f},")
if model_weight.pvalues['Weight'] < 0.05:
    print(f"which is less than 0.05, which is statistically significant.\n"
          f"This indicates that CO2 residuals of volume are dependent on engine weight.\n"
          f"For every kg of engine weight, CO2 emissions increase by approximately"
          f" {model_weight.params['Weight']:.6f}.")
else:
    print(f"which is greater than or equal to 0.05, which is not statistically significant.\n"
          f"This indicates that CO2 residuals of volume are not dependent on engine weight.")
