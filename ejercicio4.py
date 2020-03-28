import csv
import numpy
import matplotlib 
from matplotlib import pyplot
with open('aceleraciones.csv') as csvfile:
    reader=csv.DictReader(csvfile)

    for row in reader:
        
        print (row['X'], row['Y'], row['Z'])
        
        
    pyplot.plot(row['X'],'*')
    pyplot.show()