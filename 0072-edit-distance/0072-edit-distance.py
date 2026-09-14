class Solution(object):
    def minDistance(self, word1, word2):
        # dp[j] is the cost to convert the processed part of
        # word1 into word2[:j].
        dp = list(range(len(word2) + 1))

        for i in range(1, len(word1) + 1):
            previous_diagonal = dp[0]
            dp[0] = i

            for j in range(1, len(word2) + 1):
                previous_above = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = previous_diagonal
                else:
                    dp[j] = 1 + min(
                        dp[j - 1],          # Insert
                        previous_above,     # Delete
                        previous_diagonal   # Replace
                    )

                previous_diagonal = previous_above

        return dp[-1]