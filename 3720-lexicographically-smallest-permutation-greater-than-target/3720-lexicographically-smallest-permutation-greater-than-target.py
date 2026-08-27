class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        # Try the position where we make the string greater.
        # Rightmost position is preferred.
        for i in range(n - 1, -1, -1):

            # Rebuild the frequency array for this pivot.
            remain = cnt[:]

            # Try to keep target[0 ... i-1] unchanged.
            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if remain[x] == 0:
                    possible = False
                    break

                remain[x] -= 1

            if not possible:
                continue

            # At position i, we need the smallest
            # available character strictly greater than target[i].
            target_char = ord(target[i]) - ord('a')

            for c in range(target_char + 1, 26):

                if remain[c] == 0:
                    continue

                ans = target[:i]

                # Make the first difference here.
                ans += chr(ord('a') + c)

                remain[c] -= 1

                # Fill the rest in sorted order.
                for x in range(26):
                    ans += chr(ord('a') + x) * remain[x]

                return ans

        return ""