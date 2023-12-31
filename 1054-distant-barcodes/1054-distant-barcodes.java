class Solution {
    public int[] rearrangeBarcodes(int[] barcodes) {
        int[] ans = new int[barcodes.length];
        int[] count = new int[10001];
        int maxcount = 0;
        int maxnum = 0;
        
        for (final int b : barcodes)
            ++count[b];
        
        for (int i = 1; i < 10001; ++i)
            if (count[i] > maxcount) {
                maxcount = count[i];
                maxnum = i;
            }
        
        fillAns(ans, count, maxnum, barcodes.length);
        for (int num = 1; num < 10001; ++num)
            fillAns(ans, count, num, barcodes.length);
        
        return ans;
    }
    
    private int i = 0; // ans' index
    
    private void fillAns(int[] ans, int[] count, int num, int n) {
        while (count[num]-- > 0) {
            ans[i] = num;
            i = i + 2 < n ? i + 2 : 1;
        }
    }
}