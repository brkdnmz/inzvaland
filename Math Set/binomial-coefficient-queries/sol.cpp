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

const int N = 1e6 + 5;
vector<ll> f(N), invf(N);

ll C(int n, int k) { // O(1)
    return f[n] * invf[k] % mod * invf[n - k] % mod;
}

ll C_alt(int n, int k) { // O(log(MOD))
    return f[n] * invexp(f[k] * f[n - k] % mod) % mod;
}

int main() {
    f[0] = 1;
    for (int i = 1; i < N; i++)
        f[i] = f[i - 1] * i % mod;
    invf[N - 1] = invexp(f[N - 1]);
    for (int i = N - 2; i >= 0; i--)
        invf[i] = invf[i + 1] * (i + 1) % mod;
    int q;
    cin >> q;
    while (q--) {
        int n, k;
        cin >> n >> k;
        cout << C(n, k) << "\n";
    }
}