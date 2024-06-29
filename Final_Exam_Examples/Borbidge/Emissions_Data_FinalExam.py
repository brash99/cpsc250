import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf


advert = pd.read_csv('EmissionsData.csv')
print(advert.head())

# Look at the data!  Create plots of Sales vs. each variable
fig, ax = plt.subplots(2, 2, figsize=(9,9))#
fig.suptitle("Dependency of CO2 Emissions on Car Engine Volume and Weight")#
ax[0][0].plot(advert['Volume'], advert['CO2'], 'o', label = "Data")           # scatter plot showing actual data
ax[0][0].set_xlabel('Engine Volume mL')#volume
ax[0][0].set_ylabel('CO2 Emissions')#change labels

ax[0][1].plot(advert['Weight'], advert['CO2'], 'o', label = "Data")           # scatter plot showing actual data
ax[0][1].set_xlabel('Weight (kg)')
ax[0][1].set_ylabel('CO2 Emissions')
#change labels
'''ax[0][2].plot(advert['Newspaper'], advert['Sales'], 'o', label = "Data")           # scatter plot showing actual data
ax[0][2].set_xlabel('Newspaper Advertising Costs')
ax[0][2].set_ylabel('Sales')'''


do_fit = True

if do_fit:
    # Fit a linear regression model to a single parameter - Sales vs. TV advertising costs
    model = smf.ols('CO2 ~ Volume', data=advert)
    model = model.fit()

    # View model summary
    # print(model.summary())

    # Predict values
    sales_pred = model.predict()

    # Add this prediction to the DataFrame
    advert['Emissions_Volume'] = sales_pred
    # Add the DIFFERENCE between Sales data and prediction to the DataFrame
    advert['Emissions_Volume_Residual'] = advert['CO2'] - sales_pred
    print(advert.head())

do_plot = True

if do_plot:
    # Plot regression against actual data
    ax[1][0].plot(advert['Volume'], advert['CO2'], 'o', label = "Data")           # scatter plot showing actual data
    ax[1][0].plot(advert['Volume'], sales_pred, '-', linewidth=2, label = "Prediction")   # regression line
    ax[1][0].set_xlabel('Engine Volume (mL)')
    ax[1][0].set_ylabel('CO2 Emissions')

    # Plot residuals
    ax[1][1].plot(advert['Weight'], advert['Emissions_Volume_Residual'], 'o', label = "Data")  # scatter plot showing actual data
    ax[1][1].set_xlabel('Weight (kg)')
    ax[1][1].set_ylabel('CO2_Emissions_Residuals')

do_fit2 = True

if do_fit2:
    # Fit a linear regression model to a single parameter - Sales_TV_Residual vs. Radio advertising costs
    model2 = smf.ols('Emissions_Volume_Residual ~ Weight', data=advert)
    model2 = model2.fit()

    sales_pred2 = model2.predict()

    advert['Emissions_Volume_Weight'] = sales_pred2
    advert['Emissions_Volume_Weight_Residual'] = advert['Emissions_Volume_Residual'] - sales_pred2
    print(advert.head())

do_plot2 = True

if do_plot2:
    ax[1][1].plot(advert['Weight'], sales_pred2, '-', label = "Data")  # scatter plot showing actual data

    # plot residuals
    '''ax[1][2].plot(advert['Newspaper'], advert['Sales_TV_Radio_Residual'], 'o', label = "Data")  # scatter plot showing actual data
    ax[1][2].set_xlabel('Newspaper Advertising Costs')
    ax[1][2].set_ylabel('Sales vs. TV/Radio Residual')

do_fit3 = False

if do_fit3:
    # Fit a linear regression model to a single parameter - Sales_TV_Radio_Residual vs. Newspaper advertising costs
    model3 = smf.ols('Sales_TV_Radio_Residual ~ Newspaper', data=advert)
    model3 = model3.fit()

    sales_pred3 = model3.predict()

    advert['Sales_TV_Radio_Newspaper'] = sales_pred3
    advert['Sales_TV_Radio_Newspaper_Residual'] = advert['Sales_TV_Radio_Residual'] - sales_pred3
    print(advert.head())

do_plot3 = False

if do_plot3:
     ax[1][2].plot(advert['Newspaper'], sales_pred3, 'o', label = "Data")'''  # scatter plot showing actual data


print(model.summary())
#print(model2.summary())
#print(model3.summary())

plt.show()
print("Completed")