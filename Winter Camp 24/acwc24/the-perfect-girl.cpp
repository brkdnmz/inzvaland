#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int mod = 1e9 + 7;

int main() {
    int n, D;
    cin >> n >> D;
    int c[n], d[n];
    for (int i = 0; i < n; i++)
        cin >> c[i] >> d[i];
    ll dp[D + 1] = {};
    dp[0] = 1;
    for (int i = 0; i < n; i++) {
        // Elimizde c[i] tane d[i] değerinde banknot var

        // dp[j] += dp[j - d[i]] + dp[j - 2 * d[i]] + dp[j - 3 * d[i]]...
        // 1 tane kullanırsam:      dp[j] += dp[j - d[i]]
        // 2 tane kullanırsam:      dp[j] += dp[j - 2 * d[i]]
        // 3 tane kullanırsam:      dp[j] += dp[j - 3 * d[i]]
        // 4 tane kullanırsam:      dp[j] += dp[j - 4 * d[i]]
        // 5 tane kullanırsam:      dp[j] += dp[j - 5 * d[i]]
        // ...
        // c[i] tane kullanırsam:   dp[j] += dp[j - c[i] * d[i]]
        int prefix_sum[D + 1] = {};
        for (int j = 0; j <= D; j++) {
            int prev_sum = j - d[i] >= 0 ? prefix_sum[j - d[i]] : 0;
            prefix_sum[j] = (prev_sum + dp[j]) % mod;
        }
        for (int j = d[i]; j <= D; j++) {
            // l ve r nedir?
            // r = j - d[i]
            // l = j - (c[i] + 1) * d[i]
            // prefix[r] - prefix[l]
            int r = j - d[i];
            ll l = j - (ll)(c[i] + 1) * d[i];
            dp[j] += prefix_sum[r] - (l >= 0 ? prefix_sum[l] : 0);
            // dp[j] %= mod;
            (dp[j] += mod) %= mod;

            // Yukarıdaki prefix sum hesabı, şunu optimize ediyor:
            // for (int cnt = 1; cnt <= c[i] && j - cnt * d[i] >= 0; cnt++) {
            //     (dp[j] += dp[j - cnt * d[i]]) %= mod;
            // }
        }
    }
    cout << dp[D] << "\n";
}

/*
6 10
2 3
3 2
5 5
1 10
15 1
5 1


3 3
2 2 2
5 5 5 5 5
10
1 1 1...1 -> 15 tane
1 1 1 1 1
*/