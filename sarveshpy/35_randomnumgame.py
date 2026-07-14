import random

num=random.randint(1,5)
tries=0

while True:
    guess=int(input("Enter a number:"))

    if num==guess:
        tries+=1
        print(f"You are right and U guessed the number in {tries} tries.")
        break

    elif num>guess:
        tries+=1
        print("You may have guessed a little higher")

    elif num<guess:
        tries+=1
        print("You may have guessed a little lower")        

    else:
        print("Sorry U are wrong")    