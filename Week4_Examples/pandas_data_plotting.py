import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':

    df = pd.read_csv("testdata.csv")
    print(df)

    fig, ax = plt.subplots()
    sns.regplot(x='Temperature',y='Pollen Count', data=df, order=2, ci=68.0, ax=ax, label='Quadratic Fit')
    ax.errorbar(df['Temperature'],df['Pollen Count'],df['Error in Pollen Count'],df['Error in Temperature'],'o',color='blue', label='Pollen Count Data')
    ax.set_title("Basic Plotting Example")
    ax.set_ylim(0.0)

    plt.legend()
    plt.show()
