// https://ideone.com/HFQx8j
#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;
const int mod = 1e9 + 7;
int f[N], inv_f[N];

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

void precalculate() {
    f[0] = 1;
    for (int i = 1; i < N; i++) {
        f[i] = mul(f[i - 1], i);
    }

    inv_f[N - 1] = invexp(f[N - 1]);
    for (int i = N - 2; i >= 0; i--) {
        inv_f[i] = mul(i + 1, inv_f[i + 1]);
    }
}

void print_binomial_coefficients(int upper_bound) {
    // An example so-called "lambda" function, similar to those in Python.
    // I used it to just let you know about them.
    auto C = [&](int n, int k) {
        if (n < k)
            return 0;
        return mul(f[n], mul(inv_f[n - k], inv_f[k]));
    };

    int n_examples = 10;
    for (int i = 0; i < n_examples; i++) {
        int n = rand() % (N + 1), k = rand() % (N + 1);
        cout << "C(" << n << ", " << k << ") mod (1e9 + 7): " << C(n, k) << "\n";
    }
}

int main() {
    // To make program generate different sequences of random integers for each run.
    srand(time(0));
    precalculate();
    int upper_bound = 1e6;
    print_binomial_coefficients(upper_bound);
}