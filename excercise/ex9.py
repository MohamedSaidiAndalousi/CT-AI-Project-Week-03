import random
f = ""
numb = random.randint(1,20)
print(numb)
answer = int(input(f"guess the number between 1-20: "))
guess_counter = 1 

while answer != numb:
    if answer > numb:
        print("too small")
        guess_counter += 1
    else:
        print("too big")
        guess_counter += 1


print(f"you got it in {guess_counter} tries")

