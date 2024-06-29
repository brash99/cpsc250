import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

advert = pd.read_csv('EmissionsData.csv')
print(advert.head())



# Fit
volumemodel = smf.ols('CO2 ~ Volume', data=advert).fit()
print("Linear Regression Summary for CO2 vs. Volume:")
print(volumemodel.summary())
print()
advert['CO2_Volume_Predicted'] = volumemodel.predict()
advert['CO2_Volume_Residuals'] = advert['CO2'] - advert['CO2_Volume_Predicted']

weightmodel = smf.ols(formula='CO2_Volume_Residuals ~ Weight', data=advert).fit()
print("Linear Regression Summary for CO2_Volume_Residuals vs. Weight:")
print(weightmodel.summary())
print()
advert['CO2_Volume_Residuals_Predicted'] = weightmodel.predict()
advert['CO2_Volume_Residuals_Final'] = advert['CO2_Volume_Residuals'] - advert['CO2_Volume_Residuals_Predicted']


#used chatgpt for plotting
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
fig.tight_layout(pad=2.5)

# Plot CO2 vs. Volume
axs[0, 0].scatter(advert['Volume'], advert['CO2'], label='Data')
axs[0, 0].plot(advert['Volume'], advert['CO2_Volume_Predicted'], color='red', label='Linear Fit')
axs[0, 0].set_xlabel('Volume (mL)')
axs[0, 0].set_ylabel('CO2 Emissions')
axs[0, 0].set_title('CO2 Emissions vs. Volume')
axs[0, 0].legend()

# Plot CO2 vs. Weight
axs[0, 1].scatter(advert['Weight'], advert['CO2'], label='Data')
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions')
axs[0, 1].set_title('CO2 Emissions vs. Weight')

# Plot CO2 vs. Volume with residuals
axs[1, 0].scatter(advert['Volume'], advert['CO2'], label='Data')
axs[1, 0].plot(advert['Volume'], advert['CO2_Volume_Predicted'], color='red', label='Linear Fit')
axs[1, 0].set_xlabel('Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions')
axs[1, 0].set_title('CO2 Emissions vs. Volume with Fit')

# Plot CO2_Volume_Residuals vs. Weight
axs[1, 1].scatter(advert['Weight'], advert['CO2_Volume_Residuals'], label='Data')
axs[1, 1].plot(advert['Weight'], advert['CO2_Volume_Residuals_Predicted'], color='red', label='Linear Fit')
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Emissions Residuals')
axs[1, 1].set_title('CO2 Emissions Residuals vs. Weight')

print('While the graphs show an increase in carbon emissions with an increase in volume and weight, I believe there are too many other factors not included that may cause the multiple outliers in the graph')

plt.show()
print("Completed")