class Solution {
    public boolean predictTheWinner(int[] nums) {
        final int n = nums.length;
        int[] dp = nums.clone();

        for (int d = 1; d < n; ++d)
            for (int j = n - 1; j - d >= 0; --j) {
                final int i = j - d;
                dp[j] = Math.max(nums[i] - dp[j],      // Pick left num
                                 nums[j] - dp[j - 1]); // Pick right num
            }
        
        return dp[n - 1] >= 0;
    }
}