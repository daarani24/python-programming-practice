import random
n=random.randint(1,20)
guess=input("Guess even or odd:").lower()
if n%2==0:
    r="Even"
else:
    r="odd"
print("Number was",n)
if guess==r:
    print("You guessed correctly!")
else:
    print("Wrong guess!")