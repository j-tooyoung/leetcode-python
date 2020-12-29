# https://wangdh15.github.io/2020/03/27/%E8%83%8C%E5%8C%85%E7%B1%BB%E9%97%AE%E9%A2%98%E6%80%BB%E7%BB%93/
# 多重背包问题
# 每个物品的个数是一个确定的量s[i]
# w重量，v价值，V总容量
def dp(w, v, s, V):
    dp = [[0] for i in range(len(w))] * (V + 1)
    for i in range(len(w)):
        for j in range(V + 1):
            for k in range(s[i] + 1):
                if k * w[i] <= j:
                    continue
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k *w[i]] + k *v[i])
    return dp[len(w) - 1][V]

# 二进制优化
def dp(w, v, s, V):

    return

if __name__ == '__main__':
    print()