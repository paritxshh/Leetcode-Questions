
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        size = 4 * n
        sum1 = [0] * size
        sum2 = [0] * size
        lazy = [0] * size

        def apply(node, l, r, val):
            length = r - l + 1
            sum2[node] = (sum2[node] + 2 * val * sum1[node]
                          + length * val * val) % MOD
            sum1[node] = (sum1[node] + length * val) % MOD
            lazy[node] += val

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return
            mid = (l + r) // 2
            val = lazy[node]
            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)
            lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)

            sum1[node] = (sum1[node * 2]
                          + sum1[node * 2 + 1]) % MOD
            sum2[node] = (sum2[node * 2]
                          + sum2[node * 2 + 1]) % MOD

        ans = 0
        last = {}

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            # Increase distinct counts for subarrays
            # starting at prev + 1 through i.
            update(1, 0, n - 1, prev + 1, i, 1)

            # Sum of squared distinct counts for subarrays
            # ending at index i.
            ans = (ans + sum2[1]) % MOD
            last[x] = i

        return ans
