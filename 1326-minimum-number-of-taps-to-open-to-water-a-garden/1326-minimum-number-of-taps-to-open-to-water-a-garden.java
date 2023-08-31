class Solution {
    public int minTaps(int n, int[] ranges) {
        int[] nums = new int[n + 1];
        
        for (int i = 0; i <= n; ++i) {
            int l = Math.max(0, i - ranges[i]);
            int r = Math.min(n, i + ranges[i]);
            nums[l] = Math.max(nums[l], r - l);
        }
        
        int ans = 0;
        int end = 0;
        int far = 0;
        
        for (int i = 0; i < n; i++) {
            far = Math.max(far, i + nums[i]);
            
            if (i == end) {
                ++ans;
                end = far;
            }
        }
        
        return end == n ? ans : -1;
    }
}