// https://ideone.com/VVaql5
#include <iostream>
#include <vector>
using namespace std;

vector<int> sieve(int n) {
    vector<bool> is_prime(n + 1, 1);
    is_prime[0] = is_prime[1] = 0;
    vector<int> n_primes(n + 1); // if you define a vector of ints without the initial value, they'll all be initialized to 0.

    for (int i = 2; i <= n; i++) {
        n_primes[i] = n_primes[i - 1] + is_prime[i];

        if (!is_prime[i])
            continue;

        // We wrote factor <= n/i instead of factor * i <= n. Convenient trick to prevent overflow!
        for (int factor = i; factor <= n / i; factor++) {
            is_prime[factor * i] = false;
        }
    }
    return n_primes;
}

int main() {
    int n = 1e8;
    vector<int> n_primes = sieve(n);
    cout << "Number of primes up to " << n << " = " << n_primes[n] << "!\n";
}