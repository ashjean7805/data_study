def change(money):
    # write your code here
    coins = [1,3,4]
    dp = [9999] * (money+1)
    for i in range(money+1):
        if i == 0:
            dp[i] = 0 
        elif i in coins:    
            dp[i] = 1
        else:
            dp_temp = []
            for j in range(1,(i//2)+1):
                dp_temp.append(dp[j]+dp[i-j])
            dp[i] = min(dp_temp)
    return dp[-1]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
