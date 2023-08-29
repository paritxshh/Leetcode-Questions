class Solution {
    public int numSub(String s) {
        int mod = 1000000007;
        int count = 0;
        int currcount = 0;
        
        for (char c : s.toCharArray()) {
            if (c == '1') {
                currcount++;
                count = (count + currcount) % mod;
            } else {
                currcount = 0;
            }
        }
        
        return count;
    }
}