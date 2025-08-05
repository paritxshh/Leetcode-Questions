class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF
        MASK = 0xFFFFFFFF

        while b != 0:
            # Sum without carry
            sum_ = (a ^ b) & MASK
            # Carry
            carry = ((a & b) << 1) & MASK
            a, b = sum_, carry

        # Handle negative numbers
        return a if a <= MAX_INT else ~(a ^ MASK)