import sys

if __name__ == '__main__':
	input = raw_input().split()
	n, m = int(input[0]), int(input[1])
	coins = [int(x) for x in raw_input().split()]
	dp = [0] * (n + 1)
	dp[0] = 1
	for i in range(1, n+1):
		min_coins = sys.maxint
		for coin in coins:
			if i >= coin:
				min_coins = min(dp[i - coin], min_coins)
		dp[i] = min_coins
	print dp[n]
