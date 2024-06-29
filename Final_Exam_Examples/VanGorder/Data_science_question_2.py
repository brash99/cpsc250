import matplotlib
matplotlib.use('TkAgg') # This is a workaround for MacOS bug
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm


# Get the data
advert = pd.read_csv('EmissionsData.csv')
print(advert.head())

fig, ax = plt.subplots(2, 2, figsize=(9,9))
fig.tight_layout(pad=2.0)

#Top left plot
ax[0,0].scatter(advert['Volume'], advert['CO2'], marker='o')
ax[0,0].set_xlabel('Volume(mL)')
ax[0,0].set_ylabel('CO2 Emissions')

#Top right plot
ax[0,1].scatter(advert['Weight'], advert['CO2'], marker='o')
ax[0,1].set_xlabel('Weight(kg)')
ax[0,1].set_ylabel('CO2 Emissions')

#Carry out linear regression
X_volume = sm.add_constant(advert['Volume'])
model_volume = sm.OLS(advert['CO2'], X_volume).fit()
advert['CO2_predicted_volume'] = model_volume.predict(X_volume)
advert['CO2_residual_volume'] = advert['CO2'] - advert['CO2_predicted_volume']

#bottom left plot
ax[1,0].scatter(advert['Volume'], advert['CO2'],marker='o',label='Data')
ax[1,0].plot(advert['Volume'], advert['CO2_predicted_volume'], color='orange')
ax[1,0].set_xlabel('Volume(mL)')
ax[1,0].set_ylabel('CO2 Emissions')

#Carry out linear regression
X_weight = sm.add_constant(advert['Weight'])
model_weight = sm.OLS(advert['CO2_residual_volume'], X_weight).fit()
advert['CO2_predicted_weight'] = model_weight.predict(X_weight)

#bottom right plot
ax[1,1].scatter(advert['Weight'], advert['CO2_residual_volume'],marker='o',label='Data')
ax[1,1].plot(advert['Weight'], advert['CO2_predicted_weight'], color='orange')
ax[1,1].set_xlabel('Weight(kg)')
ax[1,1].set_ylabel('CO2 Residuals (after Volume)')

plt.show()



