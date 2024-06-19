class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def check(day: int) -> bool:
            cnt = curr = 0
            for bd in bloomDay:
                curr = curr + 1 if bd <= day else 0
                if curr == k:
                    cnt += 1
                    curr = 0
            return cnt >= m
        
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left