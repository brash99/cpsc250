import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('EmissionsData.csv')

fig, axs = plt.subplots(2, 2, figsize=(9, 9))
fig.suptitle("Dependency of C02 Emissions on Car Engine Volume and Weight")
fig.tight_layout(pad=2.5)
#CO2 emissions vs volume
axs[0, 0].scatter(df['Volume'], df['CO2'], alpha=0.6, edgecolors='w')
axs[0, 0].set_xlabel('Engine Volume (ml)')
axs[0, 0].set_ylabel('CO2 Emissions')
#CO2 emissions vs weight
axs[0, 1].scatter(df['Weight'], df['CO2'], alpha=0.6, edgecolors='w')
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions')
#linear regression co2 vs volume
model_volume = smf.ols('CO2 ~ Volume', data=df).fit()
df['CO2_pred_volume'] = model_volume.predict(df['Volume'])
df['CO2_residuals_volume'] =df['CO2'] - df['CO2_pred_volume']
#co2 vs volume
axs[1, 0].scatter(df['Volume'], df['CO2'], alpha=0.6, edgecolors='w', label='Data')
axs[1, 0].plot(df['Volume'], df['CO2_pred_volume'], color='orange', linestyle='--', label='Linear Fit')
axs[1, 0].set_xlabel('Engine Volume (ml)')
axs[1, 0].set_ylabel('CO2 Emissions')
axs[1, 0].legend()

model_residuals = smf.ols('CO2_residuals_volume ~ Weight', data=df).fit()
df['CO2_residuals_pred'] = model_residuals.predict(df['Weight'])

axs[1, 1].scatter(df['Weight'], df['CO2_residuals_volume'], alpha=0.6, edgecolors='w', label='Data')
axs[1, 1].plot(df['Weight'], df['CO2_residuals_pred'], color='orange', linestyle='--', label='Linear Fit')
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Emissions vs. Volume Residuals')
axs[1, 1].legend()

print(model_volume.summary())
print(model_residuals.summary())
plt.show()
print("Completed")