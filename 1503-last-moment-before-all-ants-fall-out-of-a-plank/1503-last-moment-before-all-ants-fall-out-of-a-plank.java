class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        int maxLeft = 0;
        int minRight = n;

        for (int ant : left) {
            maxLeft = Math.max(maxLeft, ant);
        }

        for (int ant : right) {
            minRight = Math.min(minRight, ant);
        }

        return Math.max(maxLeft, n - minRight);
    }
}