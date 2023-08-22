class Solution {
    public long minimumCost(String s) {
        final int n = s.length();
        long ans = 0;
        
        for (int i = 1; i < n; ++i)
            if (s.charAt(i) != s.charAt(i - 1))
                ans += Math.min(i, n - i);
        
        return ans;
    }
}