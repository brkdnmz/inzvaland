#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n = 1e7;
    // Initially, all are unmarked (marked means composite)
    vector<bool> is_prime(n + 1, 1);
    is_prime[0] = is_prime[1] = 1; // Not that necessary
    for (int i = 2; i <= n; i++) {
        if (!is_prime[i])
            continue;
        for (int k = 2 * i; k <= n; k += i) {
            is_prime[k] = 0;
        }
    }

    // Do whatever you want
    int n_primes = 0;
    for (int i = 2; i <= n; i++)
        n_primes += is_prime[i];
    cout << n_primes << "\n";
}
