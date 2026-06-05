from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, state, prev2, prev1):
                """
                state:
                    0 -> no non-leading digit seen yet
                    1 -> exactly 1 digit formed
                    2 -> at least 2 digits formed
                Returns: (count_numbers, total_waviness_sum)
                """
                if pos == m:
                    return (1, 0)

                limit = digits[pos] if tight else 9
                total_count = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if state == 0:
                        if d == 0:
                            cnt, wav = dp(pos + 1, ntight, 0, 10, 10)
                        else:
                            cnt, wav = dp(pos + 1, ntight, 1, 10, d)

                        total_count += cnt
                        total_wavy += wav

                    elif state == 1:
                        cnt, wav = dp(pos + 1, ntight, 2, prev1, d)

                        total_count += cnt
                        total_wavy += wav

                    else:  # state == 2
                        add = 1 if (
                            (prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)
                        ) else 0

                        cnt, wav = dp(pos + 1, ntight, 2, prev1, d)

                        total_count += cnt
                        total_wavy += wav + add * cnt

                return (total_count, total_wavy)

            return dp(0, True, 0, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)