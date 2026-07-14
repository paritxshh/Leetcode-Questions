from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAXV = 200

        # Precompute gcd for values 1..200
        g = [[0] * (MAXV + 1) for _ in range(MAXV + 1)]
        for i in range(1, MAXV + 1):
            for j in range(1, MAXV + 1):
                g[i][j] = gcd(i, j)

        dp = [[0] * (MAXV + 1) for _ in range(MAXV + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [[0] * (MAXV + 1) for _ in range(MAXV + 1)]
            for g1 in range(MAXV + 1):
                for g2 in range(MAXV + 1):
                    cur = dp[g1][g2]
                    if cur == 0:
                        continue

                    # Skip current element
                    ndp[g1][g2] = (ndp[g1][g2] + cur) % MOD

                    # Put in first subsequence
                    ng1 = x if g1 == 0 else g[g1][x]
                    ndp[ng1][g2] = (ndp[ng1][g2] + cur) % MOD

                    # Put in second subsequence
                    ng2 = x if g2 == 0 else g[g2][x]
                    ndp[g1][ng2] = (ndp[g1][ng2] + cur) % MOD

            dp = ndp

        ans = 0
        for d in range(1, MAXV + 1):
            ans = (ans + dp[d][d]) % MOD

        return ans