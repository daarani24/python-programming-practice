n=int(input())
m=n
t=len(str(n))
sum=0
while m>0:
    r=m%10
    sum+=(r**t)
    m//=10
if sum==n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")