#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 998244353;

ll invexp(ll x) {
    int exp = mod - 2;
    ll ans = 1;
    while (exp) {
        if (exp & 1)
            (ans *= x) %= mod;
        exp >>= 1;
        (x *= x) %= mod;
    }
    return ans;
}

int main() {
    ll n, k;
    cin >> n >> k;
    k = min(k, n - k);
    ll numer = 1, denom = 1;
    for (int i = 1; i <= k; i++) {
        (numer *= (n - i + 1) % mod) %= mod;
        (denom *= i) %= mod;
    }

    cout << numer * invexp(denom) % mod << "\n";
}