import random
n=random.randint(1,10)
guess=int(input("Guess a num b/w 1 to 10:"))
if guess==n:
    print("Correct! You Win!")
else:
    print("Wrong! Number was",n)