
def solve(nums,n):
    pres=[0]*(n+1)
    for i in range(1,n+1):
        pres[i]=pres[i-1]+nums[i-1]
    odd=False
    if n%2==1:
        odd=True
    dp=[]
    for l in range(n+1):
        dp.append([0]*(n+1))
    for l in range(n):
		for i in range(n-1):
            if l==0:
                if odd:
                    dp[i][i] =nums[i]
                else:
                    dp[i][i]=-nums[i]
			else:
				if odd==True:
					dp[i][i+l] = max(dp[i+1][i+l], dp[i][i+l-1]) + pres[i+l+1] - pres[i]
				else:
					dp[i][i+l] = max(dp[i+1][i+l], dp[i][i+l-1]) - pres[i+l+1] + pres[i]
		odd =  not odd
	return dp[0][n-1]
print solve([1,2,3,4,2,6],6)