class Solution {
    public int maximumPopulation(int[][] logs) {
        int[] yrs = new int[101];
        for(int[] lg : logs) {
            yrs[lg[0] - 1950]++;
            yrs[lg[1] - 1950]--;
        }
        
        int maxpop = 0;
        int maxyr = 0;
        int currpop = 0;
        
        for(int i = 0; i < yrs.length; i++) {
            currpop += yrs[i];
            if(currpop > maxpop) {
                maxpop = currpop;
                maxyr = i + 1950;
            }
        }
        
        return maxyr;
    }
}