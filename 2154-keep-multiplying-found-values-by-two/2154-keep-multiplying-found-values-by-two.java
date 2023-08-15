class Solution {
    public int findFinalValue(int[] nums, int original) {
        for(int i = 0; i<nums.length; i++) {
            if(nums[i] == original) {
                original = 2 * original;
                return findFinalValue(nums, original);
            }
        }
        
        return original;
    }
}