class Solution {
    public int findChampion(int[][] grid) {
        int n = grid.length;
        for (int i = 0;; ++i) {
            int count = 0;
            for (int j = 0; j < n; ++j) {
                if (i != j && grid[i][j] == 1) {
                    ++count;
                }
            }
            
            if (count == n - 1) {
                return i;
            }
        }
    }
}