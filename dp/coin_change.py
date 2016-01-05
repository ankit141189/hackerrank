if __name__ == '__main__':
	input = raw_input().split()
	n, m = int(input[0]), int(input[1])
	coins = sorted([int(x) for x in raw_input().split()])
	dp = [None] * (n + 1)
	dp[0] = [1] * m
	for i in range(1, n+1):
		dp[i] = [0] * m
		for j in range(0, m):
			if i >= coins[j]:
				dp[i][j] = dp[i - coins[j]][j]
			if j > 0:
				dp[i][j] += dp[i][j - 1]
	print dp[n][m - 1]
