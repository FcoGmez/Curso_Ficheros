import csv

with open('datos_ambientales.csv') as csvfile:
    reader=csv.DictReader(csvfile)

    for row in reader:
        print (row['X'], row['Y'], row['Z'])