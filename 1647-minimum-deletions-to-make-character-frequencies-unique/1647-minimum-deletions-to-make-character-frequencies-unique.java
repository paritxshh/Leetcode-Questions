class Solution {
    public int minDeletions(String s) {
        int ans = 0;
        int[] count = new int[26];
        Set<Integer> usedfreq = new HashSet<>();
        
        for (final char c : s.toCharArray())
            ++count[c - 'a'];
        
        for (int freq : count) {
            while (freq > 0 && usedfreq.contains(freq)) {
                --freq;
                ++ans;
            }
            usedfreq.add(freq);
        }
        
        return ans;
    }
}