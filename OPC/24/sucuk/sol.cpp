#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int mod = 1e9 + 7; // 998244353

const int N = 2e5 + 5;

ll exp(ll a, ll b) {
    ll r = 1;
    while (b) {
        if (b & 1)
            (r *= a) %= mod;
        b >>= 1;
        (a *= a) %= mod;
    }
    return r;
}

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    int a[n];
    for (int &x : a)
        cin >> x;
    int sum = accumulate(a, a + n, 0);
    ll f[sum + 1], invf[sum + 1];
    f[0] = 1;
    for (int i = 1; i <= sum; i++)
        f[i] = f[i - 1] * i % mod;
    invf[sum] = exp(f[sum], mod - 2);
    for (int i = sum - 1; i >= 0; i--)
        invf[i] = invf[i + 1] * (i + 1) % mod;
    auto C = [&](int a, int b) { return f[a] * invf[b] % mod * invf[a - b] % mod; };
    vector<ll> dp(sum + 1);
    dp[0] = 1;
    for (int x : a) {
        for (int i = sum; i >= 0; i--) {
            dp[i] = 0;
            for (int j = 1; j <= min(x, i); j++) {
                dp[i] += dp[i - j] * C(x - 1, j - 1) % mod * invf[j] % mod;
                dp[i] %= mod;
            }
        }
    }
    for (int i = 1; i <= sum; i++) {
        ((dp[i] *= f[i]) += dp[i - 1]) %= mod;
    }
    int q;
    cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << (dp[r] - dp[l - 1] + mod) % mod;
        if (q)
            cout << "\n";
    }
}