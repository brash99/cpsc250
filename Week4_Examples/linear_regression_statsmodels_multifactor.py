import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

# Get the data
advert = pd.read_csv('advertising.csv')
print(advert.head())

# Look at the data!  Create plots of Sales vs. each variable
fig, ax = plt.subplots(2, 3, figsize=(12,8))
fig.suptitle("Effects of Advertising on Sales")
ax[0][0].plot(advert['TV'], advert['Sales'], 'o', label = "Data")           # scatter plot showing actual data
ax[0][0].set_xlabel('TV Advertising Costs')
ax[0][0].set_ylabel('Sales')

ax[0][1].plot(advert['Radio'], advert['Sales'], 'o', label = "Data")           # scatter plot showing actual data
ax[0][1].set_xlabel('Radio Advertising Costs')
ax[0][1].set_ylabel('Sales')

ax[0][2].plot(advert['Newspaper'], advert['Sales'], 'o', label = "Data")           # scatter plot showing actual data
ax[0][2].set_xlabel('Newspaper Advertising Costs')
ax[0][2].set_ylabel('Sales')


do_fit = True

if do_fit:
    # Fit a linear regression model to a single parameter - Sales vs. TV advertising costs
    model = smf.ols('Sales ~ TV', data=advert)
    model = model.fit()

    # View model summary
    # print(model.summary())

    # Predict values
    sales_pred = model.predict()

    # Add this prediction to the DataFrame
    advert['Sales_TV'] = sales_pred
    # Add the DIFFERENCE between Sales data and prediction to the DataFrame
    advert['Sales_TV_Residual'] = advert['Sales'] - sales_pred
    print(advert.head())

do_plot = True

if do_plot:
    # Plot regression against actual data
    ax[1][0].plot(advert['TV'], advert['Sales'], 'o', label = "Data")           # scatter plot showing actual data
    ax[1][0].plot(advert['TV'], sales_pred, '.', linewidth=2, label = "Prediction")   # regression line
    ax[1][0].set_xlabel('TV Advertising Costs')
    ax[1][0].set_ylabel('Sales')

    # Plot residuals
    ax[1][1].plot(advert['Radio'], advert['Sales_TV_Residual'], 'o', label = "Data")  # scatter plot showing actual data
    ax[1][1].set_xlabel('Radio Advertising Costs')
    ax[1][1].set_ylabel('Sales Residuals')

do_fit2 = True

if do_fit2:
    # Fit a linear regression model to a single parameter - Sales_TV_Residual vs. Radio advertising costs
    model2 = smf.ols('Sales_TV_Residual ~ Radio', data=advert)
    model2 = model2.fit()

    sales_pred2 = model2.predict()

    advert['Sales_TV_Radio'] = sales_pred2
    advert['Sales_TV_Radio_Residual'] = advert['Sales_TV_Residual'] - sales_pred2
    print(advert.head())

do_plot2 = True

if do_plot2:
    ax[1][1].plot(advert['Radio'], sales_pred2, 'o', label = "Data")  # scatter plot showing actual data

    # plot residuals
    ax[1][2].plot(advert['Newspaper'], advert['Sales_TV_Radio_Residual'], 'o', label = "Data")  # scatter plot showing actual data
    ax[1][2].set_xlabel('Newspaper Advertising Costs')
    ax[1][2].set_ylabel('Sales vs. TV/Radio Residual')

do_fit3 = True

if do_fit3:
    # Fit a linear regression model to a single parameter - Sales_TV_Radio_Residual vs. Newspaper advertising costs
    model3 = smf.ols('Sales_TV_Radio_Residual ~ Newspaper', data=advert)
    model3 = model3.fit()

    sales_pred3 = model3.predict()

    advert['Sales_TV_Radio_Newspaper'] = sales_pred3
    advert['Sales_TV_Radio_Newspaper_Residual'] = advert['Sales_TV_Radio_Residual'] - sales_pred3
    print(advert.head())

do_plot3 = True

if do_plot3:
     ax[1][2].plot(advert['Newspaper'], sales_pred3, 'o', label = "Data")  # scatter plot showing actual data


print(model.summary())
print(model2.summary())
print(model3.summary())

plt.show()