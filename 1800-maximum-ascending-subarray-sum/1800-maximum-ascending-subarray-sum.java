class Solution {
    public int maxAscendingSum(int[] nums) {
        int maxsum = 0;
        int currsum = nums[0];
        
        for(int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                currsum += nums[i];
            } else {
                maxsum = Math.max(maxsum, currsum);
                currsum = nums[i];
            }
        }
        
        return Math.max(maxsum, currsum);
    }
}