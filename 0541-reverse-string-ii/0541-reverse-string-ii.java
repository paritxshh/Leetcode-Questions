class Solution {
    public String reverseStr(String s, int k) {
        StringBuilder rs = new StringBuilder(s);
        
        for(int i = 0; i < rs.length(); i += 2 * k) {
            int l = i;
            int r = Math.min(i + k - 1, rs.length() - 1);
            while(l < r) {
                rs.setCharAt(l, s.charAt(r));
                rs.setCharAt(r, s.charAt(l));
                ++l;
                --r;
            }
        }
        
        return rs.toString();
    }
}