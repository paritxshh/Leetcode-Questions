class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Store as (end, start, weight, originalIndex) and sort by end boundary
        sortedIntervals = [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
        sortedIntervals.sort(key=lambda x: x[0])

        # dp[i][j] stores a tuple: (-max_weight, lexicographically_smallest_indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]

        for i, (end, start, weight, originalIndex) in enumerate(sortedIntervals):
            # Binary search to find the latest non-overlapping interval
            # bisect_left finds the first interval whose end >= current start
            k = bisect_left(sortedIntervals, (start,), hi=i)
            
            for j in range(1, 5):
                prevWeight, prevIndices = dp[k][j - 1]
                
                skip = dp[i][j]
                
                # min() naturally prioritizes the lowest (most negative) weight sum, 
                # then lexicographically smallest sorted indices
                takeWeight = prevWeight - weight
                takeIndices = sorted(prevIndices + [originalIndex])
                take = (takeWeight, takeIndices)
                
                dp[i + 1][j] = min(skip, take)

        return dp[-1][4][1]