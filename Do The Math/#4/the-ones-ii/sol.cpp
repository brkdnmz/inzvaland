#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

ll pw(ll base, ll exp) {
    base %= mod;
    ll res = 1;
    while (exp--)
        (res *= base) %= mod;
    return res;
}

int main() {
    ll n, m;
    cin >> n >> m;
    ll ans = 1;
    for (int i = 2; 1ll * i * i <= n; i++) {
        if (n % i)
            continue;
        int exp = 0;
        for (; n % i == 0; n /= i, exp++)
            ;
        ans *= (pw(exp + 1, m) - pw(exp, m) + mod) % mod;
        ans %= mod;
    }
    if (n > 1) {
        ans *= (pw(2, m) - 1 + mod) % mod;
        ans %= mod;
    }
    cout << ans << "\n";
}