// https://ideone.com/tlbrtz
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll factorial(int n) {
    ll res = 1;
    for (int i = 1; i <= n; i++) {
        res *= i;
    }
    return res;
}

// We abbreviate "binomial coefficient" as "C" standing for "Combination".
ll C(int n, int k) {
    if (k > n)
        return 0;
    // numerator == n!
    // denominator = (n-k)! * k!
    ll numerator = factorial(n), denominator = factorial(n - k) * factorial(k);
    return numerator / denominator;
}

void print_binomial_coefficients(int n) {
    ll C_table[n + 1][n + 1];
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            if (i < j) {
                C_table[i][j] = 0;
                continue;
            }
            if (!j) {
                C_table[i][j] = 1;
                continue;
            }
            C_table[i][j] = C_table[i - 1][j - 1] + C_table[i - 1][j]; // even if i-1 < j, C_table[i-1][j] = 0, no problem here!
        }
    }
    cout << "Binomial coefficients calculated w/ factorial (left) vs. w/ recursive formula (right)\n";
    int n_examples = 10;
    for (int i = 0; i < n_examples; i++) {
        cout << i + 1 << ".\t";
        int rand_n = rand() % n;
        int rand_k = rand() % (rand_n + 1);
        cout << "n = " << rand_n << ", k = " << rand_k << ", C(n, k): " << C(rand_n, rand_k) << " vs. " << C_table[rand_n][rand_k] << "\n";
    }
}

int main() {
    int n = 30;
    print_binomial_coefficients(n);
}