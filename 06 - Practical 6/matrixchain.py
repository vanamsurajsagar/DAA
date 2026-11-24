def matrix_chain(p, n):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (dp[i][k]
                        + dp[k + 1][j]
                        + p[i - 1] * p[k] * p[j])

                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n - 1]


n = int(input("Enter the number of matrices: "))

p = []

print("Enter matrix dimensions:")
for i in range(n + 1):
    p.append(int(input()))

min_cost = matrix_chain(p, n + 1)

print("\nMinimum Number of Multiplications:", min_cost)
