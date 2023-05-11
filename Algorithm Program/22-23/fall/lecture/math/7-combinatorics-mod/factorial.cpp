// https://ideone.com/OLseOi
#include <bits/stdc++.h>
using namespace std;

const int mod = 1e9 + 7;

int mul(int a, int b) {
    return 1ll * a * b % mod;
}

int factorial(int n) {
    int res = 1;
    for (int i = 1; i <= n; i++) {
        res = mul(res, i);
    }
    return res;
}

int factorial_recursive(int n) {
    if (!n)
        return 1;
    return mul(n, factorial_recursive(n - 1));
}

void print_factorials(int bound) {
    int n_examples = 10;
    for (int i = 0; i <= n_examples; i++) {
        int n = rand() % (bound + 1);
        cout << n << "!:\n";
        cout << "\t" << factorial(n) << " (iterative)\n";
        cout << "\t" << factorial_recursive(n) << " (recursive)\n";
    }
}

int main() {
    int bound = 1e7;
    print_factorials(bound);
}