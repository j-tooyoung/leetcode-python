# 72. 编辑距离
#如果是将a中最后一个位置删除了，那么需要的操作是f[i-1, j] + 1
# 如果是将a中最后一个位置插入了一个元素，那么这个元素一定是b中最后一个元素，所以操作为f[i, j-1] + 1
# 如果是将a中最后一个位置替换为和b最后一个位置相同，这个时候需要考虑原本是否就相同，如果相同，则为f[i-1, j-1],否则为f[i-1, j-1] + 1。
# 边界情况处理，这个问题和前面的不同，边界不再是零，需要人为初始化一下。
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2),
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
        for i in range(len2 + 1):
            dp[0][i] = i

        for i in range(1,len1 + 1):
            for j in range(1, len2 + 1):
                # a最后一个位置，删除，插入操作
                dp[i][j] = min(dp[i - 1][j] + 1,dp[i][j - 1] + 1)
                if word1[i - 1] == word2[j -1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j - 1])    #
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j - 1] + 1) # 替换操作
        return dp[len1][len2]