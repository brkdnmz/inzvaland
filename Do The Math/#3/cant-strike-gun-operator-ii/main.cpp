#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int m, r;
    cin >> m >> r;
    int ans = 0;
    int mod = 1e9 + 7;
    int pw2[r];
    pw2[0] = 1;
    for (int i = 1; i < r; i++)
        pw2[i] = pw2[i - 1] * 2 % mod;
    for (int last_reload = 1; last_reload <= r; last_reload++) {
        ans += 1ll * pw2[max(0, r - last_reload - 1)] * (m - last_reload + 1) %
               mod;
        ans %= mod;
    }
    cout << ans << "\n";
}