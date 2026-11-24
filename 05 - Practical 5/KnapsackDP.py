def knapsack(weights, profits, capacity, n):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter the number of items: "))

weights = []
profits = []

print("Enter weights:")
for i in range(n):
    weights.append(int(input()))

print("Enter profits:")
for i in range(n):
    profits.append(int(input()))

capacity = int(input("Enter knapsack capacity: "))

max_profit = knapsack(weights, profits, capacity, n)

print("\nMaximum Profit:", max_profit)