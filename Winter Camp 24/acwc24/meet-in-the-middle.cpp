#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Soru:
// https://algoleague.com/problem/it-is-brute-force/detail

void helper(vector<ll> &v, int i, ll sum, bool empty, vector<ll> &subset_sums) {
    if (i == v.size()) {
        if (!empty)
            subset_sums.push_back(sum);
        return;
    }
    helper(v, i + 1, sum, empty, subset_sums);
    helper(v, i + 1, sum + v[i], false, subset_sums);
}

int main() {
    int n;
    cin >> n;
    ll a[n];
    for (auto &x : a)
        cin >> x;
    vector<ll> left, right;
    for (int i = 0; i < n; i++) {
        i < n / 2 ? left.push_back(a[i]) : right.push_back(a[i]);
    }
    vector<ll> lsums, rsums;
    // Boş subsetleri dahil etmiyoruz.
    helper(left, 0, 0, true, lsums);
    helper(right, 0, 0, true, rsums);
    sort(lsums.begin(), lsums.end());
    sort(rsums.begin(), rsums.end());
    ll ans = 1e18;

    // Bir tarafın boş olduğu durumları handle ediyoruz.
    for (auto &lsum : lsums)
        ans = min(ans, abs(lsum));
    for (auto &rsum : rsums)
        ans = min(ans, abs(rsum));

    // İki tarafın da dolu olduğu durumlar.
    int r = rsums.size() - 1;
    for (int i = 0; i < lsums.size(); i++) {
        while (r && lsums[i] + rsums[r] >= 0)
            r--;
        ans = min(ans, abs(lsums[i] + rsums[r]));
        if (r + 1 < rsums.size())
            ans = min(ans, abs(lsums[i] + rsums[r + 1]));
    }
    cout << ans << "\n";
}