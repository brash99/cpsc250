import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf


# read the csv file
data = pd.read_csv('EmissionsData.csv')
# Create a 2 x 2 set of plots in a figure that is 9 inches x 9 inches, with tight layout padding of 2.5 around each plot
# I used chat gpt to help me write this
fig, axs = plt.subplots(2, 2, figsize=(9, 9), tight_layout=True)
fig.subplots_adjust(hspace=0.5, wspace=0.5)

# Top left plot: CO2 emissions vs. Volume
# i used chat gpt to help me write this
axs[0, 0].scatter(data['Volume'], data['CO2'], color='blue')
axs[0, 0].set_title('CO2 vs. Volume')
axs[0, 0].set_xlabel('Volume (mL)')
axs[0, 0].set_ylabel('CO2 emissions (g/km)')

# Top right plot: CO2 emissions vs. Weight

# i used chat gpt to help me write this plot
axs[0, 1].scatter(data['Weight'], data['CO2'], color='green')
axs[0, 1].set_title('CO2 vs. Weight')
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 emissions (g/km)')

# i used chat gpt to help me write the code for the linear regression model

model1 = smf.ols('CO2 ~ Volume', data=data).fit()
data['CO2VolumeResiduals'] = data['CO2'] - model1.fittedvalues
axs[1, 0].scatter(data['Volume'], data['CO2'], color='blue')
axs[1, 0].plot(data['Volume'], model1.fittedvalues, color='red')
axs[1, 0].set_title('CO2 vs. Volume with Fit')
axs[1, 0].set_xlabel('Volume (mL)')
axs[1, 0].set_ylabel('CO2 emissions (g/km)')

model2 = smf.ols('CO2VolumeResiduals ~ Weight', data=data).fit()
data['WeightResiduals'] = data['CO2VolumeResiduals'] - model2.fittedvalues

# Lower right plot: CO2VolumeResiduals vs. Weight with linear regression fit
axs[1, 1].scatter(data['Weight'], data['CO2VolumeResiduals'], color='green')
axs[1, 1].plot(data['Weight'], model2.fittedvalues, color='red')
axs[1, 1].set_title('CO2 Residuals vs. Weight with Fit')
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Residuals')

print(model1.summary())
print(model2.summary())

plt.show()