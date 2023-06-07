import csv
import matplotlib.pyplot as plt

def read_particulate_data(filename):
    aqi_list = []
    concentration_list = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            aqi_list.append(float(row[0]))
            concentration_list.append(float(row[1]))
    return aqi_list, concentration_list

aqi,concentration = read_particulate_data("particulate_matter.csv")

plt.plot(concentration, aqi, 'o-')
plt.title('EPA AQI Determination - Small Particulate Concentration')
plt.ylabel("AQI")
plt.xlabel("Concentration (ug/m^3)")

c = [-25.0,525.0]
aqi1 = [0.0,0.0]
plt.plot(c,aqi1,color='green',linestyle='dashed')
aqi1 = [50.0,50.0]
plt.plot(c,aqi1,color='yellow',linestyle='dashed')
aqi1 = [100.0,100.0]
plt.plot(c,aqi1,color='orange',linestyle='dashed')
aqi1 = [150.0,150.0]
plt.plot(c,aqi1,color='red',linestyle='dashed')
aqi1 = [200.0,200.0]
plt.plot(c,aqi1,color='purple',linestyle='dashed')
aqi1 = [300.0,300.0]
plt.plot(c,aqi1,color='maroon',linestyle='dashed')
plt.show()

