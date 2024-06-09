class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        rem_count = {0: 1} # initialize with 0:1 to handle subarrays starting from the beginning
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k # to handle negative remainders
            
            if remainder in rem_count:
                count += rem_count[remainder]
                rem_count[remainder] += 1
            else:
                rem_count[remainder] = 1
        
        return count