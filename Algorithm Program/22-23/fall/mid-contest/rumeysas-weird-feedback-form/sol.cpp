#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

int exp(int b, int e) {
    int res = 1;
    while (e) {
        if (e % 2)
            res = 1ll * res * b % mod;
        e /= 2;
        b = 1ll * b * b % mod;
    }
    return res;
}

const int N = 1e6 + 1;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> prime_divisor(N, 0);
    vector<int> primes;
    for (int p = 2; p < N; p++) {
        if (prime_divisor[p])
            continue;
        prime_divisor[p] = p;
        primes.push_back(p);
        if (1ll * p * p >= N)
            continue;
        for (int k = p * p; k < N; k += p)
            prime_divisor[k] = p;
    }

    map<ll, int> exponents;

    int n;
    cin >> n;
    while (n--) {
        ll x;
        cin >> x;
        if (x <= 1e6) {
            while (x > 1) {
                int p = prime_divisor[x];
                int incr = 0;
                while (x % p == 0) {
                    x /= p;
                    exponents[p]++;
                    incr++;
                }
            }
        } else {
            for (int p : primes) {
                if (p > x / p)
                    break; // same as 1ll * p * p > x
                if (x % p)
                    continue;
                int incr = 0;
                while (x % p == 0) {
                    x /= p;
                    exponents[p]++;
                    incr++;
                }
            }
            if (x > 1) {
                exponents[x]++;
            }
        }
        cout << exp(2, exponents.size()) << "\n";
    }
    int ans = 2;
    for (auto [p, e] : exponents) {
        ans = 1ll * ans * (e + 1) % mod;
    }
    cout << ans << "\n";
}