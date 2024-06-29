import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

def read_file(file_name):
    df = pd.read_csv(file_name)
    return df
# I copyed its direct path
file_name = "EmissionsData.csv"
df = read_file(file_name)
print(df)

#refreence from linear regression notes and examples and youtube video
fig, ax = plt.subplots(2, 2, figsize=(9, 9))
#theis ax[] will show which out of the 4 plits it will show up on
ax[0, 0].scatter(df['Volume'], df['CO2'], color='blue', marker='o')
ax[0, 0].set_xlabel('Engine Volume (mL)')
ax[0, 0].set_ylabel('CO2 Emissions')


ax[0, 1].scatter(df['Weight'], df['CO2'], color='blue', marker='o')
ax[0, 1].set_xlabel('Weight (kg)')
ax[0, 1].set_ylabel('CO2 Emissions')


#unsure how to make a prediction line
ax[1, 0].scatter(df['Volume'], df['CO2'], color='blue', marker='o')
ax[1, 0].set_xlabel('Engine Volume (mL)')
ax[1, 0].set_ylabel('CO2 Emissions')
ax[1, 0].legend('Data')

ax[1, 1].scatter(df['Weight'], df['CO2'], color='blue', marker='o')
ax[1, 1].set_xlabel('Weight (kg)')
ax[1, 1].set_ylabel('CO2 Emissions')
ax[1, 0].legend('Data')

#shows the plots and tight_layout is in the instructions found on matplotlib.org
plt.tight_layout()
plt.show()




