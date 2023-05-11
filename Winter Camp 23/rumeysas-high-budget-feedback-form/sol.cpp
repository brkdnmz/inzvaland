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

void normalize(int &a) {
    while (a >= mod)
        a -= mod;
    while (a < 0)
        a += mod;
}

int main() {
    ll a, b;
    cin >> a >> b;

    if (a < b)
        swap(a, b);

    if (!b) {
        cout << exp(2, max(0ll, a - 1)) << "\n";
        return 0;
    }

    vector<int> dp(b + 1);
    for (int i = 0; i <= a; i++) {
        vector<int> ndp(b + 1);
        ndp[0] = !i;
        for (int j = 0; j <= b; j++) {
            if (i) {
                normalize(ndp[j] += dp[j]);
                if (i + j > 1) {
                    normalize(ndp[j] += dp[j]);
                }
            }
            if (j) {
                normalize(ndp[j] += ndp[j - 1]);
                if (i + j > 1) {
                    normalize(ndp[j] += ndp[j - 1]);
                }
            }
            if (i && j) {
                normalize(ndp[j] -= dp[j - 1]);
                if (i > 1 || j > 1) {
                    normalize(ndp[j] -= dp[j - 1]);
                }
            }
        }
        dp.swap(ndp);
    }
    cout << dp[b] << "\n";
}