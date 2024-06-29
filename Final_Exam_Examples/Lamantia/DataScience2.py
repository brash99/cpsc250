import matplotlib.pyplot as plt
import pandas as pd

data_file = pd.read_csv('EmissionsData.csv')

fig, axs = plt.subplots(2, 2, figsize=(9, 9))

axs[0, 0].scatter(data_file['Volume'], data_file['CO2'])
axs[0, 0].set_xlabel('Volume (mL)')
axs[0, 0].set_ylabel('CO2 Emissions')

axs[0, 1].scatter(data_file['Weight'], data_file['CO2'])
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions')

mean_volume = data_file['Volume'].mean()
mean_co2 = data_file['CO2'].mean()
numerator = ((data_file['Volume'] - mean_volume) * (data_file['CO2'] - mean_co2)).sum()
denominator = ((data_file['Volume'] - mean_volume) ** 2).sum()
beta1 = numerator / denominator
beta0 = mean_co2 - beta1 * mean_volume

axs[1, 0].scatter(data_file['Volume'], data_file['CO2'])
axs[1, 0].plot(data_file['Volume'], beta0 + beta1 * data_file['Volume'], color='red')
axs[1, 0].set_xlabel('Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions')

data_file['CO2VolumeResiduals'] = data_file['CO2'] - (beta0 + beta1 * data_file['Volume'])

mean_weight = data_file['Weight'].mean()
numerator_res = ((data_file['Weight'] - mean_weight) * data_file['CO2VolumeResiduals']).sum()
denominator_res = ((data_file['Weight'] - mean_weight) ** 2).sum()
beta2 = numerator_res / denominator_res
beta2_intercept = data_file['CO2VolumeResiduals'].mean() - beta2 * mean_weight

axs[1, 1].scatter(data_file['Weight'], data_file['CO2VolumeResiduals'])
axs[1, 1].plot(data_file['Weight'], beta2_intercept + beta2 * data_file['Weight'], color='red')
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Volume Residuals')

plt.show()