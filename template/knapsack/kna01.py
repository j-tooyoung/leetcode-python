# 01背包
def dp(w, v, V):
    dp = [[0] for i in range(len(w))] * (V+1)
    for i in range(len(w)):
        for j in range(V+1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-w[i]] + v[i])
    return dp[len(w) - 1][V]

def dp(w, v, V):
    dp = [[0] for i in range(V+1)]
    for i in range(len(w)):
        # 逆序遍历，dp[j-v[i]] 避免覆盖上一行的结果
        for j in range(V+1)[::-1]:
            if j >= w[i]:
                dp[j] = max(dp[j], dp[j-v[i]] + w[i])
    return dp[V]

if __name__ == '__main__':
    print()