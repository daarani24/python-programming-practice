import random
score=0
for i in range(3):
    a=random.randint(1,10)
    b=random.randint(1,10)
    ans=int(input(f"{a}+{b}="))
    if ans==a+b:
        print("correct")
        score+=1
    else:
        print("wrong")
print("Final score:",score)