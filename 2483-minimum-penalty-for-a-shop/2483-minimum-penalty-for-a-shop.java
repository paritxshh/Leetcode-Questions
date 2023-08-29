class Solution {
    public int bestClosingTime(String customers) {
        int ans = 0;
        int prof = 0;
        int maxprof = 0;
        
        for (int i = 0; i < customers.length(); ++i) {
            prof += customers.charAt(i) == 'Y' ? 1 : -1;
            if (prof > maxprof) {
                maxprof = prof;
                ans = i + 1;
            }
        }
        
        return ans;
    }
}