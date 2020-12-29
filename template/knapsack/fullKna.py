# 完全背包
# 每个物品可以用无穷多次。
# 和01背包问题相类似，只不过是在考虑选择第i个物品的时候，由于其可以无穷多个候选，
# 需要需要将集合按照选择的第i个
def dp(w, v, V):
    dp = [[0] for i in range(V + 1)]
    for i in range(len(w)):
        for j in range(w[i], V + 1):
            # 和01背包问题的区别就是，一个必须从前到后，一个必须从后向前
            dp[j] = max(dp[j], dp[j - v[i]] + w[i])
    return dp[V]

if __name__ == '__main__':
    print()