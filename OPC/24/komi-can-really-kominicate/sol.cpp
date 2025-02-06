#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 1e7 + 5;
const int mod = 1e9 + 7;

ll bin_exp(ll a, ll b) {
    ll r = 1;
    while (b) {
        if (b & 1)
            (r *= a) %= mod;
        b /= 2;
        (a *= a) %= mod;
    }
    return r;
}

ll inv(ll a) { return bin_exp(a, mod - 2); }

int main(int argc, char **argv) {
    // freopen(argv[1], "r", stdin);
    // freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> spf(N), primes;

    for (ll i = 2; i < N; i++) {
        if (spf[i])
            continue;
        spf[i] = i;
        primes.push_back(i);
        for (ll k = i * i; k < N; k += i)
            if (!spf[k])
                spf[k] = i;
    }

    vector<int> exponent(N);

    // (e2 + 2, 2) * (prod(e + 3, 3) - prod(e + 2, 2)) + #divisors
    // a * (b - c) + d
    ll a = 1, b = 1, c = 1, d = 1;
    ll div2 = (1 + mod) / 2;
    ll div6 = (1 + mod) / 6;

    auto update_ans = [&](int prime, int exp_increase) {
        if (prime >= N) {
            if (prime == 2) {
                (a *= div2 * (exp_increase + 2) % mod * (exp_increase + 1) % mod) %= mod;
                (d *= exp_increase + 1) %= mod;
            } else {
                (b *= div6 * (exp_increase + 3) % mod * (exp_increase + 2) % mod * (exp_increase + 1) % mod) %= mod;
                (c *= div2 * (exp_increase + 2) % mod * (exp_increase + 1) % mod) %= mod;
                (d *= exp_increase + 1) %= mod;
            }
            return;
        }

        int &exp = exponent[prime];
        if (prime == 2) {
            (a *= inv(div2 * (exp + 2) % mod * (exp + 1) % mod)) %= mod;
            (d *= inv(exp + 1)) %= mod;
            exp += exp_increase;
            (a *= div2 * (exp + 2) % mod * (exp + 1) % mod) %= mod;
            (d *= exp + 1) %= mod;
        } else {
            (b *= inv(div6 * (exp + 3) % mod * (exp + 2) % mod * (exp + 1) % mod)) %= mod;
            (c *= inv(div2 * (exp + 2) % mod * (exp + 1) % mod)) %= mod;
            (d *= inv(exp + 1)) %= mod;
            exp += exp_increase;
            (b *= div6 * (exp + 3) % mod * (exp + 2) % mod * (exp + 1) % mod) %= mod;
            (c *= div2 * (exp + 2) % mod * (exp + 1) % mod) %= mod;
            (d *= exp + 1) %= mod;
        }
    };

    ll k;
    cin >> k;

    for (int p : primes) {
        if (p > k / p)
            break;
        int e = 0;
        for (; k % p == 0; k /= p, e++) {
        }
        update_ans(p, e);
    }

    if (k > 1) {
        update_ans(k, 1);
    }

    cout << (a * (b - c + mod) + d) % mod << "\n";

    int s;
    cin >> s;
    while (s--) {
        int m;
        cin >> m;
        while (m > 1) {
            int p = spf[m];

            int e = 0;
            for (; m % p == 0; m /= p, e++) {
            }

            update_ans(p, e);
        }
        cout << (a * (b - c + mod) + d) % mod;
        if (s)
            cout << "\n";
    }
}