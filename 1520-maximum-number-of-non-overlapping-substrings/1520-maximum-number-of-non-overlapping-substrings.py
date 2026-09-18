class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        # Find the smallest valid interval starting from index i
        def get_interval(i):
            end = last[ord(s[i]) - ord('a')]
            j = i

            while j <= end:
                idx = ord(s[j]) - ord('a')

                # This character appeared before i,
                # so this interval cannot be valid.
                if first[idx] < i:
                    return None

                # We must include all occurrences of this character.
                end = max(end, last[idx])
                j += 1

            return [i, end]

        intervals = []

        # Only the first occurrence of each character
        # can be the beginning of a minimal valid interval.
        for i in range(n):
            if first[ord(s[i]) - ord('a')] == i:
                interval = get_interval(i)

                if interval:
                    intervals.append(interval)

        # Greedily select intervals with the earliest ending position.
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result