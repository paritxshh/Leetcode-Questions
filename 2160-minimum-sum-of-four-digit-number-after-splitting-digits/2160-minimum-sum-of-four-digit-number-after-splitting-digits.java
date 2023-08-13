class Solution {
    public int minimumSum(int num) {
        char[] cr = String.valueOf(num).toCharArray();
        Arrays.sort(cr);
        return (cr[0] - '0') * 10 + (cr[2] - '0') + (cr[1] - '0') * 10 + (cr[3] - '0');
    }
}