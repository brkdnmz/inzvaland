#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;
const int N = 1e6 + 5;

// f[i] = i!
// inv_f[i] = 1/i!
int f[N], inv_f[N]; // defining as ll will consume 2x memory!

// a^(mod-2) (1/a)
ll modular_inverse(ll a) {
    a %= mod;
    int exp = mod - 2;
    ll res = 1;
    while (exp) {
        if (exp % 2)
            res = res * a % mod;
        exp /= 2;
        a = a * a % mod;
    }
    return res;
}

// Fill in the factorial arrays
void setup() {
    f[0] = 1;
    for (int i = 1; i < N; i++) {
        f[i] = 1ll * f[i - 1] * i % mod;
    }
    inv_f[N - 1] = modular_inverse(f[N - 1]);
    for (int i = N - 2; i >= 0; i--) {
        inv_f[i] = 1ll * inv_f[i + 1] * (i + 1) % mod;
    }
}

// C(n, k) binomial coefficient
// Slowest version -> 2 * log(mod)
ll nCk_v1(int n, int k) {
    return (ll)f[n] * modular_inverse(f[k]) % mod * modular_inverse(f[n - k]) % mod;
}
// A bit faster version -> log(mod)
ll nCk_v2(int n, int k) {
    return (ll)f[n] * modular_inverse((ll)f[k] * f[n - k] % mod) % mod;
}
// Fastest version -> O(1)
ll nCk_v3(int n, int k) {
    return (ll)f[n] * inv_f[k] % mod * inv_f[n - k] % mod;
}

int main() {
}
