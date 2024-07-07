#include <bits/stdc++.h>
using namespace std;

int mod = 1e9 + 7;
// int mod = 998244353;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    int g[n][n][n];
    for (int d = 0; d < n; d++) {
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                cin >> g[c][r][d];
            }
        }
    }
    vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(n + 1, vector<int>(n + 1, 0)));
    char next[n][n][n];
    for (int c = n - 1; c >= 0; c--) {
        for (int r = n - 1; r >= 0; r--) {
            for (int d = n - 1; d >= 0; d--) {
                int mx = 0;
                char cur_next;
                if (mx < dp[c][r + 1][d]) {
                    mx = dp[c][r + 1][d];
                    cur_next = 'U';
                }
                if (mx <= dp[c + 1][r][d]) {
                    mx = dp[c + 1][r][d];
                    cur_next = 'R';
                }
                if (mx <= dp[c][r][d + 1]) {
                    mx = dp[c][r][d + 1];
                    cur_next = 'F';
                }
                next[c][r][d] = cur_next;
                dp[c][r][d] = mx + g[c][r][d];
            }
        }
    }
    int c = 0, r = 0, d = 0;
    string path;
    while (c + 1 < n || r + 1 < n || d + 1 < n) {
        path += next[c][r][d];
        if (next[c][r][d] == 'U') {
            r++;
        } else if (next[c][r][d] == 'R') {
            c++;
        } else if (next[c][r][d] == 'F') {
            d++;
        }
    }
    cout << dp[0][0][0] << "\n";
    cout << path;
}