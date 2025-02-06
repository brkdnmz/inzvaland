#include <bits/stdc++.h>
using namespace std;
using ll = long long;

mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

long long randint(long long l, long long r) { return uniform_int_distribution<long long>(l, r)(rng); }

int main(int argc, char **argv) {
    // freopen(argv[1], "r", stdin);
    // freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    while (1) {
        int n, m;
        n = 9;
        m = 9;
        int cnt[n + 1][m + 1] = {};
        int up[m + 1] = {};
        ll ans = 0;
        char g[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                char c = "/\\"[randint(0, 2) ? 0 : 1];
                g[i][j] = c;
                if (c != '/') {
                    up[j] = 0;
                    continue;
                }
                up[j]++;
                cnt[i][j] = cnt[i][j - 1] + 1;
                for (int k = 1; 2 * k + 1 <= up[j]; k++) {
                    ans += max(0, min({cnt[i][j], cnt[i - k][j], cnt[i - 2 * k][j]}) - 1);
                }
            }
        }
        if (ans == 81) {
            cout << n << " " << m << "\n";
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
                    cout << g[i][j];
                }
                cout << "\n";
            }
            break;
        }
        // cout << ans << "\n";
    }
}