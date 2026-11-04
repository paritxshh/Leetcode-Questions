from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        mp = {v: i + 1 for i, v in enumerate(vals)}

        bit_count = Fenwick(m)
        bit_sum = Fenwick(m)

        def add(v, delta):
            idx = mp[v]
            bit_count.add(idx, delta)
            bit_sum.add(idx, v * delta)

        def get_cost():
            median_idx = bit_count.kth((x + 1) // 2)
            median = vals[median_idx - 1]

            left_count = bit_count.query(median_idx)
            left_sum = bit_sum.query(median_idx)

            total_sum = bit_sum.query(m)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (median * left_count - left_sum) + \
                   (right_sum - median * right_count)

        costs = []

        for i in range(n):
            add(nums[i], 1)

            if i >= x:
                add(nums[i - x], -1)

            if i >= x - 1:
                costs.append(get_cost())

        # DP with O(n*k) time and O(n*k) space
        INF = 10**18

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]

                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x]
                    )

        return dp[n][k]