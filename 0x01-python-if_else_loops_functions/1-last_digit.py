#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = int(str(number)[len(number)-1])
if value > 5:
  print("Last digit of {} is {} and is greater thzn 5".format(number,value))
elif value == 0:
  print("Last digit of {} is {} and is 0".format(number,value))
else:
  print("Last digit of {} is {} and is less than 6 and not 0".format(number,value))
