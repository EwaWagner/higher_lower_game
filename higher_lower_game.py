import random
print("Chose your level (easy, medium, hard)")
easy = 10
medium = 100
hard = 1000
level = input()



if level == "easy":
    numb1 = random.randint(0,easy)
    print(numb1)
    numb2 = random.randint(0,easy)
if level == "medium":
    numb1 = random.randint(0,medium)
    print(numb1)
    numb2 = random.randint(0,medium)
if level == "hard":
    numb1 = random.randint(0,hard)
    print(numb1)
    numb2 = random.randint(0,hard)



print("Is your next number, (1. higher) or (2. lower)")
decision = input()



if decision == "higher" or decision == "1":
    if numb1 < numb2:
        print("you are correct, the second number was", numb2)
    else:
        print("loserrrrrr, your number was", numb2)
elif decision == "lower" or decision == "2":
    if numb1 > numb2:
        print("you are correct, the second number was", numb2)
    else:
        print("loserrrrrr, your number was", numb2)
else:
    exit()
