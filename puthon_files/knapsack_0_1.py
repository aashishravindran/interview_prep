"""Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. 
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
"""
weights=[10,20,30]
value=[60,100,120]
total_weigh=50

dp=[[0 for  _ in range(total_weigh+1)] for _ in range(len(weights)+1)]


for i in range(1,len(dp)):
	for j in range(1,len(dp[0])):
		if j< weights[i-1]:
			dp[i][j]=dp[i-1][j]
		else:
			dp[i][j]=max(value[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j])


print(dp)