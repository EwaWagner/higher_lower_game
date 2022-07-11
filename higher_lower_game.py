from operator import truediv
import random
numb1 = random.randint(0,10)
print(numb1)

print("Say 1. higher or 2. lower")
decision = input()
numb2 = random.randint(0,10)

if decision == "higher" or decision == "1":
    if numb1 < numb2:
        print("you are correct, the second number was", numb2)
    else:
        print("loserrrrrr, your number was", numb2)

if decision == "lower" or decision == "2":
    if numb1 > numb2:
        print("you are correct, the second number was", numb2)
    else:
        print("loserrrrrr, your number was", numb2)

