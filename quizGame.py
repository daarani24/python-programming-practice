score=0
ans=input("Python is a programming language?(yes/no):")
if ans == 'yes':
    score+=5
ans=input("5+5=9? (yes/no):")
if ans == 'no':
    score+=5
print("Your Score:",score,"out of 10")