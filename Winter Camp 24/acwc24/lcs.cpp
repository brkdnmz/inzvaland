#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, t;
    cin >> s >> t;
    int n = s.size(), m = t.size();
    int dp[n + 1][m + 1] = {};
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            dp[i][j] = dp[i - 1][j];
            dp[i][j] = max(dp[i][j], dp[i][j - 1]);
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
            }
        }
    }
    cout << dp[n][m] << "\n";
}