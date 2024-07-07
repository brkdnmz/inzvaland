#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int mod = 1e9 + 7;

void generate(vector<ll> &armutlar, vector<array<ll, 2>> &secimler, int i = 0, int mask = 0, ll toplam = 0) {
    if (i == armutlar.size()) {
        secimler.push_back({mask, toplam});
        return;
    }
    generate(armutlar, secimler, i + 1, mask, toplam);
    if (!i || !(mask >> (i - 1) & 1))
        generate(armutlar, secimler, i + 1, mask | (1 << i), (toplam + armutlar[i]) % mod);
}

ll solve() {
    int n;
    cin >> n;
    int a[n];
    for (int &x : a)
        cin >> x;

    vector<ll> l, r;
    for (int i = 0; i < n; i++)
        i < n / 2 ? l.push_back(a[i]) : r.push_back(a[i]);

    vector<array<ll, 2>> lchoices, rchoices;
    generate(l, lchoices);
    generate(r, rchoices);

    int lsize = n / 2;
    int rsize = n - n / 2;
    vector<ll> rsums[2][2];
    for (auto &[mask, sum] : rchoices) {
        bool l_taken = rsize && mask >> (rsize - 1) & 1;
        bool r_taken = mask & 1;
        rsums[l_taken][r_taken].push_back(sum);
    }
    for (int i : {0, 1})
        for (int j : {0, 1})
            sort(rsums[i][j].begin(), rsums[i][j].end());

    ll max_ans = 0;
    for (auto &[mask, sum] : lchoices) {
        bool l_taken = lsize && mask >> (lsize - 1) & 1;
        bool r_taken = mask & 1;
        for (int i = 0; i <= !r_taken; i++) {
            for (int j = 0; j <= !l_taken; j++) {
                auto &target_sums = rsums[i][j];
                auto it = upper_bound(target_sums.begin(), target_sums.end(), mod - 1 - sum);
                if (it == target_sums.begin())
                    continue;
                max_ans = max(max_ans, sum + *(--it));
            }
        }
    }
    return max_ans;
}

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll ans = solve();
    cout << ans;
}