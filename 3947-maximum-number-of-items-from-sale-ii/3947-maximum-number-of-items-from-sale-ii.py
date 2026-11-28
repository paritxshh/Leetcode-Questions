
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Frequency of each factor
        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        # Step 2: Count items divisible by each factor
        divisible = [0] * (n + 1)

        for f in range(1, n + 1):
            for multiple in range(f, n + 1, f):
                divisible[f] += freq[multiple]

        # Step 3: Calculate bonus opportunities per item
        min_price = min(price for factor, price in items)

        bonus_items = []

        for factor, price in items:
            free_count = divisible[factor] - 1

            if free_count > 0 and price <= 2 * min_price:
                bonus_items.append((price, free_count))

        # Step 4: Buy bonus-eligible copies greedily
        bonus_items.sort()

        answer = 0

        for price, count in bonus_items:
            buy = min(count, budget // price)

            answer += 2 * buy
            budget -= buy * price

            if buy < count:
                break

        # Step 5: Buy ordinary copies using remaining budget
        answer += budget // min_price

        return answer