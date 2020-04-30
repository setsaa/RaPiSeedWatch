from picamera import PiCamera, Color
from time import sleep, asctime
from sense_hat import SenseHat
from datetime import datetime
from csv import writer

camera = PiCamera()
sense = SenseHat()
camera.rotation = -90
camera.annotate_background = Color('black')

timestamp = datetime.now()
delay = 3600
image_number = 0

def get_data():
    data = []
    temp = round(sense.get_temperature(), 1)
    hum = round(sense.get_humidity(), 2)
    date = datetime.now()
    data.append([temp, hum, date])
    return data

with open('log.csv', 'w', newline='') as f:
    data_writer = writer(f, delimiter="\t")
    data_writer.writerow(["temp", "hum", "", "time"])

    while True:
        data = get_data()
        dt = data[0][-1] - timestamp
        if dt.seconds > delay:
            data_writer.writerow(data[0])
            for i, d in enumerate(data[0]):
                if i == 0:
                    data[0].insert(1, "C")
                if i == 1:
                    data[0].insert(3, "%")
            del data[0][-1]       
            data = str(data).replace('[','').replace(']','').replace("'","").replace(',','') \
                            .replace('datetime','').replace('(','').replace(')','')
            data = data + " " + str(asctime())
            print(data)
            camera.annotate_text = data
            image_name = 'image{0:04d}.jpg'.format(image_number)
            camera.capture("/home/pi/Documents/Projects/SeedWatch/images/" + image_name)
            image_number += 1
            timestamp = datetime.now()
