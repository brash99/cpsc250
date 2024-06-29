import matplotlib.pyplot as plt
import pandas as pd
import csv

#opening file Refrense chat and youtube video "Complete Python Pandas Data Science Tutorial! "
def read_file(file_name):
    df = pd.read_csv(file_name)
    return df
#for some reason it would not let me import csv so I copyed its direct path
file_name = "Projectile.csv"
df = read_file(file_name)
print(df)

x = df['Time']
y = df['Height']
plt.xlabel('Time (s)')
plt.ylabel("Height (m)")

plt.title('Projectile Motion Experiment')
plt.figure(figsize=(8, 6))
#plt.scatter(x, y) refrence form youtube 'matplotlib graphs using csv files, bar, pie, line graph'
plt.scatter(x, y, color='red', marker = '^')
plt.legend('Height')
plt.show()
