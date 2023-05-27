def partition3(loot):
    total_sum = sum(loot)
    target_sum = total_sum // 3

    if len(loot) < 3 or total_sum % 3 != 0 or target_sum == 0:
        return 0

    count = 0
    n = len(loot)
    dp = [[0] * (n + 1) for _ in range(target_sum + 1)]

    for i in range(1, target_sum + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1]
            if loot[j - 1] <= i:
                temp = dp[i - loot[j - 1]][j - 1] + loot[j - 1]
                if temp > dp[i][j]:
                    dp[i][j] = temp
            if dp[i][j] == target_sum:
                count += 1

    if count < 3:
        return 0
    else:
        return 1

# Read input
n = int(input())
loot = list(map(int, input().split()))

# Call the function and print the result
print(partition3(loot))