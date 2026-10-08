import time
S = ""
for i in range(10,128):
    if i % 2 != 0:
        S = S + f"{i}" + ", " 

print(S)