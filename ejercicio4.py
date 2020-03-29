import csv
import numpy as np
import matplotlib.pyplot as plt


x=np.array([])
y=np.array([])
z=np.array([])

with open('aceleraciones.csv') as csvfile:
    reader=csv.DictReader(csvfile)

    for row in reader:
        
        x=np.append(x,row['X'])
        y=np.append(y,row['Y'])
        z=np.append(z,row['Z'])

plt.plot(x)
plt.plot(y)
plt.plot(z)

plt.ylabel('G')

plt.title('Ejercicio4')
plt.legend('XYZ')
plt.show()
