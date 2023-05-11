#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

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
    int n, k;
    cin >> n >> k;
    ll numer = 1, denom = 1;
    for (int i = 1; i <= n; i++)
        (numer *= i) %= mod;
    for (int i = 1; i <= k; i++) {
        (denom *= i) %= mod;
    }
    for (int i = 1; i <= n - k; i++) {
        (denom *= i) %= mod;
    }

    cout << numer * invexp(denom) % mod << "\n";
}