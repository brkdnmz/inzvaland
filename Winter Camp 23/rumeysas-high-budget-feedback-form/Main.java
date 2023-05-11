//Brace your keyboard
//inzva community built algoleague for every algorithm enthusiast hungry for self-improvement and friendly competition. Have fun and good luck!

import java.util.Scanner;

class Main {
    final static int mod = (int) 1e9 + 7;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        sc.close();
        if (a < b) {
            long tmp = a;
            a = b;
            b = tmp;
        }
        if (b == 0) {
            System.out.println(exp(2, Math.max(0, a - 1)));
            return;
        }

        int[][] dp = new int[(int) a + 1][(int) b + 1];
        dp[0][0] = 1;
        for (int i = 0; i <= a; i++) {
            for (int j = 0; j <= b; j++) {
                if (i > 0) {
                    dp[i][j] += dp[i - 1][j];
                    dp[i][j] %= mod;
                    if (i + j > 1) {
                        dp[i][j] += dp[i - 1][j];
                        dp[i][j] %= mod;
                    }
                }
                if (j > 0) {
                    dp[i][j] += dp[i][j - 1];
                    dp[i][j] %= mod;
                    if (i + j > 1) {
                        dp[i][j] += dp[i][j - 1];
                        dp[i][j] %= mod;
                    }
                }
                if (i > 0 && j > 0) {
                    dp[i][j] -= dp[i - 1][j - 1];
                    dp[i][j] %= mod;
                    if (i > 1 || j > 1) {
                        dp[i][j] -= dp[i - 1][j - 1];
                        dp[i][j] %= mod;
                    }
                    if (dp[i][j] < 0)
                        dp[i][j] += mod;
                }
            }
        }
        System.out.println(dp[(int) a][(int) b]);
    }

    public static int exp(int base, long exponent) {
        exponent %= mod - 1;
        int res = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1)
                res = (int) ((long) res * base % mod);
            exponent >>= 1;
            base = (int) ((long) base * base % mod);
        }
        return res;
    }
}