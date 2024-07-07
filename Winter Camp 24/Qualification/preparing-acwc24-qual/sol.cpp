#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll solve() {
    int n;
    cin >> n;
    int p[n], t[n];
    for (int &x : p)
        cin >> x;
    for (int &x : t)
        cin >> x;
    // for (int &x : p)
    //     x = rand() % (int)1e9 + 1;
    // for (int &x : t)
    //     x = rand() % (int)1e9 + 1;
    const int N = 1 << n; // All possible setter masks are within [1, N - 1].
    ll max_total_quality = 0;
    int max_mask = 0;
    for (int ps_mask = 1; ps_mask < N; ps_mask++) {
        vector<int> setting_xps, testing_xps;
        for (int member = 0; member < n; member++) {
            bool is_tester = !(ps_mask >> member & 1);
            testing_xps.push_back(t[member]);
            if (is_tester)
                testing_xps.push_back(t[member]);
            else
                setting_xps.push_back(p[member]);
        }
        sort(setting_xps.begin(), setting_xps.end(), greater<int>()); // Or reverse after sorting without `greater`.
        sort(testing_xps.begin(), testing_xps.end(), greater<int>());
        ll total_quality = 0;
        for (int i = 0; i < setting_xps.size(); i++) {
            int P = setting_xps[i];
            int T = testing_xps[i];
            total_quality += (ll)T * (P + T); // Don't forget casting!
        }
        if (max_total_quality < total_quality)
            max_mask = ps_mask;
        max_total_quality = max(max_total_quality, total_quality);
    }
    return max_total_quality;
}

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll ans = solve();
    cout << ans;
}