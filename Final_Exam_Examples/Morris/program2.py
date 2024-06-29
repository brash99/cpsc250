import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

# Read the CSV file into a pandas DataFrame
file_path = 'EmissionsData.csv'
df = pd.read_csv(file_path)

# Carry out a linear regression fit of CO2 vs. Volume
model_volume = smf.ols('CO2 ~ Volume', data=df).fit()
df['CO2_volume_pred'] = model_volume.predict(df['Volume'])
df['CO2_volume_resid'] = df['CO2'] - df['CO2_volume_pred']

# Carry out a linear regression fit of CO2_volume_resid vs. Weight
model_weight = smf.ols('CO2_volume_resid ~ Weight', data=df).fit()
df['CO2_weight_pred'] = model_weight.predict(df['Weight'])
df['CO2_weight_resid'] = df['CO2_volume_resid'] - df['CO2_weight_pred']

# Create a 2x2 set of plots in a figure
plt.figure(figsize=(9, 9))
plt.tight_layout(pad=2.5)

# Top left: CO2 vs. Volume
plt.subplot(2, 2, 1)
plt.scatter(df['Volume'], df['CO2'], label='Data')
plt.xlabel('Engine Volume (mL)')
plt.ylabel('CO2 Emissions')
plt.title('CO2 Emissions vs. Engine Volume')

# Top right: CO2 vs. Weight
plt.subplot(2, 2, 2)
plt.scatter(df['Weight'], df['CO2'], label='Data')
plt.xlabel('Weight (kg)')
plt.ylabel('CO2 Emissions')
plt.title('CO2 Emissions vs. Weight')

# Bottom left: CO2 vs. Volume with regression line
plt.subplot(2, 2, 3)
plt.scatter(df['Volume'], df['CO2'], label='Data')
plt.plot(df['Volume'], df['CO2_volume_pred'], color='orange', label='Prediction')
plt.xlabel('Engine Volume (mL)')
plt.ylabel('CO2 Emissions')
plt.title('CO2 Emissions vs. Engine Volume with Regression')
plt.legend()

# Bottom right: CO2_volume_resid vs. Weight with regression line
plt.subplot(2, 2, 4)
plt.scatter(df['Weight'], df['CO2_volume_resid'], label='Data')
plt.plot(df['Weight'], df['CO2_weight_pred'], color='orange', label='Prediction')
plt.xlabel('Weight (kg)')
plt.ylabel('CO2 Emissions vs. Volume Residuals')
plt.title('CO2 Emissions vs. Volume Residuals with Regression')
plt.legend()

# Main title
plt.suptitle('Dependency of CO2 Emissions on Car Engine Volume and Weight')

# Save the figure
plt.savefig('EmissionsData.png')
plt.show()

# Print the summary information for each of the two linear regression models
print("Summary for CO2 vs. Volume:")
print(model_volume.summary())

print("\nSummary for CO2_volume_resid vs. Weight:")
print(model_weight.summary())
