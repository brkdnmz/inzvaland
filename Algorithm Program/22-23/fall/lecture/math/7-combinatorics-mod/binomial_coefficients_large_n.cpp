// https://ideone.com/5V5FFT
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

int mul(int a, int b) {
    return 1ll * a * b % mod;
}

// base^(mod - 2)
int invexp(int base) {
    int result = 1;
    int exponent = mod - 2;
    while (exponent) {
        if (exponent & 1)
            result = mul(result, base);
        exponent >>= 1;
        base = mul(base, base);
    }
    return result;
}

int C(ll n, ll k) {
    if (n < k)
        return 0;
    // n * (n-1) * (n-2) * ... * (n-k+1) / k!
    k = min(k, n - k); // to guarantee k is small
    int numerator = 1, denominator = 1;
    for (ll i = n; i > n - k; i--) {
        numerator = mul(numerator, i % mod);
        denominator = mul(denominator, (i - (n - k)) % mod);
    }
    return mul(numerator, invexp(denominator));
}

void print_binomial_coefficients(int upper_bound) {

    int n_examples = 10;
    for (int i = 0; i < n_examples; i++) {
        ll n = 1ll * rand() * rand();
        bool k_is_big = rand() % 2;
        ll k = rand() % (upper_bound + 1);
        if (k_is_big)
            k = n - rand() % (upper_bound + 1);
        cout << "C(" << n << ", " << k << ") mod (1e9 + 7): " << C(n, k) << "\n";
    }
}

int main() {
    // To make program generate different sequences of random integers for each run.
    srand(time(0));
    int upper_bound = 1e6;
    print_binomial_coefficients(upper_bound);
}