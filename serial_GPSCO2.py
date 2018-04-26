import serial
#from geojson import Point, feature
i=0
serinput = serial.Serial('/dev/ttyACM0', 11500)

file= open("writetst.txt", "w") 

serlist = []
serlist.append(serinput)
if i<10:
    file.write(serlist)
    i = i+1
else:
    file.close