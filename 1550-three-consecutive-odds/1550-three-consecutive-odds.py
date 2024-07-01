class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for v in arr:
            if v & 1:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False