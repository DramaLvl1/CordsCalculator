# import time

print("Coords format: x:y (example: 235:266)")
# time.sleep(2)

firstcord = input("First coordinate")

secondcord = input("Second coordinate")

def sepcords(cord1, cord2):
  ncord1 = cord1.replace(":", " ")
  ncord2 = cord2.replace(":", " ")
  
  ncord1 = ncord1.split(" ")
  ncord2 = ncord2.split(" ")
  
  x = int(ncord1[0]) - int(ncord2[0])
  y = int(ncord1[1]) - int(ncord2[1])
  result = x**2 + y**2
  
  print("Distance:" + str(result**0.5))
  print("first cord:" + cord1)
  print("second cord:" + cord2)
  
sepcords(firstcord, secondcord)
