import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

# Get the data
advert = pd.read_csv('testing/EmissionsData.csv')
print(advert.head())

# Look at the data!  Create plots of Sales vs. each variable
fig, ax = plt.subplots(2, 2, figsize=(9,9))
fig.tight_layout(pad=2.5)
fig.suptitle("Dependency of CO2 Emissions on Car Engine Volume and Weight")
ax[0][0].plot(advert['Volume'], advert['CO2'], 'o', label = "Data")           # scatter plot showing actual data
ax[0][0].set_xlabel('Engine Volume (mL)')
ax[0][0].set_ylabel('CO2 Emissions')

ax[0][1].plot(advert['Weight'], advert['CO2'], 'o', label = "Data")           # scatter plot showing actual data
ax[0][1].set_xlabel('Weight (kg)')
ax[0][1].set_ylabel('CO2 Emissions')


do_fit = True

if do_fit:
    # Fit a linear regression model to a single parameter - Sales vs. TV advertising costs
    model = smf.ols('CO2 ~ Volume', data=advert)
    model = model.fit()

    # View model summary
    # print(model.summary())

    # Predict values
    co2_pred = model.predict()

    # Add this prediction to the DataFrame
    advert['CO2_Volume'] = co2_pred
    advert['CO2_Volume_Residual'] = advert['CO2'] - co2_pred

do_plot = True

if do_plot:
    # Plot regression against actual data
    ax[1][0].plot(advert['Volume'], advert['CO2'], 'o', label = "Data")           # scatter plot showing actual data
    ax[1][0].plot(advert['Volume'], co2_pred, '-', linewidth=2, label = "Prediction")   # regression line
    ax[1][0].set_xlabel('Engine Volume (mL)')
    ax[1][0].set_ylabel('CO2 Emissions')
    ax[1][0].legend()

    # Plot residuals
    ax[1][1].plot(advert['Weight'], advert['CO2_Volume_Residual'], 'o', label = "Data")  # scatter plot showing actual data
    ax[1][1].set_xlabel('Weight (kg)')
    ax[1][1].set_ylabel('CO2 vs. Volume Residual')

do_fit2 = True

if do_fit2:
    # Fit a linear regression model to a single parameter - Sales_TV_Residual vs. Radio advertising costs
    model2 = smf.ols('CO2_Volume_Residual ~ Weight', data=advert)
    model2 = model2.fit()

    co2_pred2 = model2.predict()

    advert['CO2_Volume_Weight'] = co2_pred2
    advert['CO2_Volume_Weight_Residual'] = advert['CO2_Volume_Residual'] - co2_pred2
    print(advert.head())

do_plot2 = True

if do_plot2:
    ax[1][1].plot(advert['Weight'], co2_pred2, '-', label = "Data")  # scatter plot showing actual data
    ax[1][1].legend()

print(model.summary())
print(model2.summary())

plt.show()