class Solution {
    public int longestNiceSubarray(int[] nums) {
        int ans = 0;
        int usedbits = 0;
        
        for (int l = 0, r = 0; r < nums.length; ++r) {
            while ((usedbits & nums[r]) > 0)
                usedbits ^= nums[l++];
            usedbits |= nums[r];
            ans = Math.max(ans, r - l + 1);
        }
        
        return ans;
    }
}