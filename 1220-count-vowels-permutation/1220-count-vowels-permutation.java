class Solution {
    public int countVowelPermutation(int n) {
        int MOD = 1000000007;
        long[][] dp = new long[n + 1][5];

        for (int i = 0; i < 5; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= n; i++) {
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % MOD; // a
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD; // e
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MOD; // i
            dp[i][3] = dp[i - 1][2] % MOD; // o
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % MOD; // u
        }

        long result = 0;
        for (int i = 0; i < 5; i++) {
            result = (result + dp[n][i]) % MOD;
        }

        return (int) result;
    }
}