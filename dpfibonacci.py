def fibo(n):
    if n<=1:
        return n
    l=[0]*(n+1)
    l[1]=1
    for i in range(2,n+1):
        l[i]=l[i-1]+l[i-2]
    return l
n=int(input())
print(fibo(n))