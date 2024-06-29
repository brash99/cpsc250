import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

# reads the CSV file into a pandas data frame
file_name = 'EmissionsData.csv'
df = pd.read_csv(file_name)

# creates a 2 x 2 set of plots in a  9 by 9 picture, with 2.5 inch around each
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
fig.tight_layout(pad=2.5)

# displays CO2 emissions vs volume & weight
axs[0, 0].scatter(df['Volume'], df['CO2'], color='blue', alpha=0.5)
axs[0, 0].set_xlabel('Engine Volume (mL)')
axs[0, 0].set_ylabel('CO2 Emissions (g/km)')
axs[0, 0].set_title('CO2 Emissions vs. Volume')

axs[0, 1].scatter(df['Weight'], df['CO2'], color='green', alpha=0.5)
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions (g/km)')
axs[0, 1].set_title('CO2 Emissions vs. Weight')

# creates the linear regression model/fit for CO2 vs the volume
model_volume = smf.ols('CO2 ~ Volume', data=df).fit()
df['CO2VolumeFit'] = model_volume.predict(df['Volume'])
df['CO2VolumeResiduals'] = df['CO2'] - df['CO2VolumeFit']

# displays the data for co2 vs volume and the linear regression fit
axs[1, 0].scatter(df['Volume'], df['CO2'], color='blue', alpha=0.5, label='Data')
axs[1, 0].plot(df['Volume'], df['CO2VolumeFit'], color='red', label='Fit')
axs[1, 0].set_xlabel('Engine Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions (g/km)')
axs[1, 0].set_title('CO2 vs. Volume with Fit')
axs[1, 0].legend()

# carries out the linear regression fit to co2volumeresiduals vs weight
model_weight = smf.ols('CO2VolumeResiduals ~ Weight', data=df).fit()
df['CO2WeightFit'] = model_weight.predict(df['Weight'])
df['CO2WeightResiduals'] = df['CO2VolumeResiduals'] - df['CO2WeightFit']

#  display the data for co2volumeresiduals vs. weight, along with the second linear regression fit
axs[1, 1].scatter(df['Weight'], df['CO2VolumeResiduals'], color='green', alpha=0.5, label='Data')
axs[1, 1].plot(df['Weight'], df['CO2WeightFit'], color='red', label='Fit')
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Volume Residuals (g/km)')
axs[1, 1].set_title('CO2 Volume Residuals vs. Weight with Fit')
axs[1, 1].legend()

#  prints the model summary for co2 vs the volume
print("Model Summary for CO2 vs. Volume:")
print(model_volume.summary())

print("\nModel Summary for CO2VolumeResiduals vs. Weight:")
print(model_weight.summary())

# interprets the results
print("\nInterpretation of the Results:")
if model_volume.pvalues['Volume'] < 0.05:
    print("CO2 emissions depend on Engine Volume.")
else:
    print("CO2 emissions don't depend on Engine Volume.")

if model_weight.pvalues['Weight'] < 0.05:
    print("CO2 emissions depend on Weight.")
else:
    print("CO2 emissions don't significantly depend on Weight.")

plt.show()  # shows the plot
print("Completed")