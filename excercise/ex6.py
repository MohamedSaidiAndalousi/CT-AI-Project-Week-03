a = int(input("1 : "))
b = int(input("2 : "))
import time
import sys
if a > b:
    print("1 can't be bigger than 2")
    sys.exit("1 can't be bigger than 2")
else:
    for i in range(a,b):
        if i % 7 == 0 and i % 5 != 0:
            print(i)
            time.sleep(.1)