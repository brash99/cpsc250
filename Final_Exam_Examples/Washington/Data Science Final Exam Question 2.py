import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf


# Read in the CSV file into a pandas data frame.
file = pd.read_csv('EmissionsData.csv')

# Create a 2 x 2 set of plots in a figure that is 9 inches x 9 inches, with tight layout padding
# of 2.5 around each plot.

# In the top two plots, display the data for CO2 emissions vs. Volume and Weight, respectively.

# Subplot 1
plt.suptitle('Dependency of CO2 Emissions on Car Engine Volume and Weight')
plt.tight_layout(pad=2.5)
plt.figure(figsize=(9,9))
plt.subplot(2, 2, 1)
plt.scatter(file['Volume'], file['CO2'])
plt.xlabel('Engine Volume(mL)')
plt.ylabel('CO2 Emissions')


# Subplot 2
plt.subplot(2, 2, 2)
plt.scatter(file['Weight'], file['CO2'])
plt.xlabel('Weight (kg)')
plt.ylabel('CO2 Emissions', loc='center')


# In the lower left plot, display the data for C02 vs. Volume, along with the linear regression fit.

# Carry out a linear regression fit to the CO2vsVolumeResiduals vs. Weight. Store the results of this
# fit in the data frame, along with the new residuals, i.e. the difference between CO2vsVolumeResiduals
# and this second fit.
model = smf.ols('CO2 ~ Volume', data=file)
model = model.fit()
file['vol_co2'] = model
file_predict = model.predict()

residuals = file['CO2'] - model.resid


# Subplot 3
plt.subplot(2, 2, 3)
plt.scatter(file['Volume'], file['CO2'])
plt.plot(file['Volume'], file_predict, color ='orange')
plt.xlabel('Engine Volume(mL)')
plt.ylabel('CO2 Emissions')

# In the lower right plot, display the data for C02vsVolumeResiduals vs. Weight,
# along with this second linear regression fit.

model2 = smf.ols('CO2 ~ Weight', data=file)
model2 = model2.fit()
file['weight_co2'] = model
file_predict = model.predict()



# Subplot 4
plt.subplot(2, 2, 4)
plt.scatter(file['Weight'], file['CO2'])
plt.plot(file['Volume'], file_predict, color ='orange')
plt.xlabel('Weight(kg)')
plt.ylabel('CO2 Emissions vs Volume Residuals')



# Print the summary information for each of the two linear regression models.

#Report on your interpretation of the results from these two models - do CO2 emissions depend on Volume?
# Do they depend on Weight?
print(f'CO2 emissions do depend on engine volume, but show no relationship with engine weight')
plt.savefig('emission_plots.png')