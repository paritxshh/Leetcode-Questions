class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Length = 2 initialization
        up = [0] * (m + 1)      # up[v]: last move was increasing
        down = [0] * (m + 1)    # down[v]: last move was decreasing

        for v in range(1, m + 1):
            up[v] = v - 1          # choose any smaller previous value
            down[v] = m - v        # choose any larger previous value

        if n == 2:
            return sum(up[1:]) % MOD

        for _ in range(3, n + 1):
            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            # prefix sums of down
            prefix = [0] * (m + 1)
            for v in range(1, m + 1):
                prefix[v] = (prefix[v - 1] + down[v]) % MOD

            # suffix sums of up
            suffix = [0] * (m + 2)
            for v in range(m, 0, -1):
                suffix[v] = (suffix[v + 1] + up[v]) % MOD

            for v in range(1, m + 1):
                # last step is up => previous step must be down
                new_up[v] = prefix[v - 1]

                # last step is down => previous step must be up
                new_down[v] = suffix[v + 1]

            up, down = new_up, new_down

        return (sum(up[1:]) + sum(down[1:])) % MOD