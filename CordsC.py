import time

print("Coords format: x:y (example: 235:266)")
time.sleep(2)

firstcord = input("First coordinate")

secondcord = input("Second coordinate")


def sepcords(cord1, cord2):
  ncord1 = cord1.replace(":", " ")
  ncord2 = cord2.replace(":", " ")
  
  ncord1 = ncord1.split(" ")
  ncord2 = ncord.split(" ")
  
  x = ncord1[0] - ncord2[0]
  y = ncord2[1] - ncord2[1]
  result = x + y
  
  print("Distance:" + str(result**0.5))
