def making_change(coins, amount):
    # Create DP array
    dp = [float('inf')] * (amount + 1)

    # 0 coins are needed to make amount 0
    dp[0] = 0

    # Calculate minimum coins for each amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# Take input from the user
n = int(input("Enter the number of coin denominations: "))

print("Enter the coin denominations:")
coins = []

for i in range(n):
    coin = int(input(f"Coin {i + 1}: "))
    coins.append(coin)

amount = int(input("Enter the amount: "))

# Find minimum number of coins
minimum_coins = making_change(coins, amount)

# Display result
if minimum_coins == float('inf'):
    print("Change cannot be made for the given amount.")
else:
    print("\nMinimum number of coins required:", minimum_coins)


#TC : O(n * amount),
#SC : O(amount)