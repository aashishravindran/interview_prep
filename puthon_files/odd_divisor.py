# weights = [2, 4, 4, 5];
# tasks = [2, 2, 3, 4];
# processing_time=15

# dp=[[0 for _ in range(processing_time/2+1)] for _ in range(len(tasks)+1)]

	

# for i in range(1,len(dp)):
# 	for j in range(1,len(dp[0])):
# 		if j < tasks[i-1]:
# 			dp[i][j]=dp[i-1][j]
# 		else:
# 			 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - tasks[i - 1]] + weights[i - 1]);


# print(dp[len(tasks)][processing_time/2])


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