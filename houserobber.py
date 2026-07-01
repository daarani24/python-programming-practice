def rob(l):
    n=len(l)
    if n==1:
        return n
    dp=[0]*n
    dp[0]=l[0]
    dp[1]=l[1]
    for i in range(2,n):
        dp[i]=max(dp[i-1],l[i]+dp[i-2])
    return dp[-1]
l=list(map(int,input().split()))
print(rob(l))