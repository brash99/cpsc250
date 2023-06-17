import matplotlib.pyplot as plt

x_values = []
y_values = []

def calls(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return calls(n-1) + calls(n-2)

for i in range(30):
    x_values.append(i)
    y_values.append(calls(i))

plt.plot(x_values,y_values)
plt.show()
