def compute_operations(n):
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

    ans = [n]
    while n != 1:
        ans_temp = [(n,dp[n])]
        if n % 3 == 0:
            ans_temp.append((n // 3, dp[n // 3]))
        if n % 2 == 0:
            ans_temp.append((n // 2, dp[n // 2]))
        n = min((ans_temp), key = lambda x:x[1])[0]
        ans.append(dp[n])
    ans = ans.reverse()
    return ans


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)