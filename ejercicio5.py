import csv
from EmulatorGUI import GPIO

from sense_emu import SenseHat
import time 
import matplotlib.pyplot as plt 


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
      
GPIO.setup(4, GPIO.OUT) 
GPIO.setup(17, GPIO.OUT, initial = GPIO.LOW) 
GPIO.setup(18, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial = GPIO.LOW)

sense=SenseHat()

i=0
MAX=20
LIM=40

csvfile = open('datos_ambientales.csv', 'w')
writer = csv.DictWriter(csvfile, fieldnames=['humedad','temp','pres'])
writer.writeheader()

while i<MAX:
    humedad=sense.humidity
    temp=sense.temperature
    pres=sense.pressure

    
    writer.writerow({'humedad': str(humedad), 'temp': str(temp), 'pres': str(pres)})
    

    import csv

    if temp>LIM:
        GPIO.output(17,GPIO.HIGH)
    else:
        GPIO.output(17,GPIO.LOW)
                
    i=i+1
    time.sleep(1)

csvfile.close()
