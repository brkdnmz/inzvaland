#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        int cnt[n + 1][m + 1] = {};
        int up[m + 1] = {};
        ll ans = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                char c;
                cin >> c;
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
        cout << ans;
        if (t)
            cout << "\n";
    }
}