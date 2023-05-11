#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

int exp(int base, ll exponent) {
    exponent %= mod - 1;
    int res = 1;
    while (exponent) {
        if (exponent & 1)
            res = 1ll * res * base % mod;
        exponent >>= 1;
        base = 1ll * base * base % mod;
    }
    return res;
}

int nC2(ll n) {
    n %= mod;
    // n * (n-1) / 2 % mod
    int numerator = 1ll * n * (n - 1) % mod;
    while (numerator % 2)
        numerator += mod;
    return numerator / 2;
}

int main() {
    ll n;
    cin >> n;
    int ans = (exp(2, n) - 1 - n - nC2(n)) % mod;
    if (ans < 0)
        ans += mod;
    cout << ans << "\n";
}