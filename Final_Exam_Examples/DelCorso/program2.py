import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

# Reads the CSV file into pandas data frame
df = pd.read_csv('EmissionsData.csv')

# Create a 2 x 2 set of plots in a figure that is 9 inches x 9 inches, tightlayout makes sure something isn't left out.
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
plt.tight_layout(pad=2.5)

# Display the data for CO2 emissions vs. Volume and Weight
axs[0, 0].scatter(df['Volume'], df['CO2'])
axs[0, 0].set_title('CO2 vs Volume')

axs[0, 1].scatter(df['Weight'], df['CO2'])
axs[0, 1].set_title('CO2 vs Weight')

# Makes a linear fit of CO2 vs. Volume
model1 = smf.ols(formula='CO2 ~ Volume', data=df).fit()
df['CO2vsVolumeFit'] = model1.fittedvalues
df['CO2vsVolumeResiduals'] = model1.resid

# Display the data for CO2 vs. Volume, along with the linear fit
axs[1, 0].scatter(df['Volume'], df['CO2'])
axs[1, 0].plot(df['Volume'], df['CO2vsVolumeFit'], color='red')
axs[1, 0].set_title('CO2 vs Volume (with fit)')

# Carry out a linear fit to the CO2vsVolumeResiduals vs. Weight
model2 = smf.ols(formula='CO2vsVolumeResiduals ~ Weight', data=df).fit()
df['CO2vsVolumeResidualsFit'] = model2.fittedvalues
df['CO2vsVolumeResiduals2'] = model2.resid

# Display the data for CO2vsVolumeResiduals vs. Weight, along with this second linear fit
axs[1, 1].scatter(df['Weight'], df['CO2vsVolumeResiduals'])
axs[1, 1].plot(df['Weight'], df['CO2vsVolumeResidualsFit'], color='red')
axs[1, 1].set_title('CO2vsVolumeResiduals vs Weight (with fit)')

# Show the plots
plt.show()

# Prints the summary information for each of the two linear models
#print(model1.summary())
#print(model2.summary())
print("Completed")