// https://ideone.com/LLhWwb
#include <iostream>
#include <vector>
using namespace std;

vector<int> sieve(int n) {
    // Use n_primes as is_prime, initially. We can compute the prefix sums later!
    vector<int> n_primes(n + 1, 1);
    n_primes[0] = n_primes[1] = 0;

    for (int i = 2; i <= n; i++) {
        n_primes[i] += n_primes[i - 1];

        if (n_primes[i] == n_primes[i - 1]) // i is not a prime
            continue;

        for (int factor = i; factor <= n / i; factor++) {
            n_primes[factor * i] = 0;
        }
    }
    return n_primes;
}

int main() {
    int n = 1e8;
    vector<int> n_primes = sieve(n);
    cout << "Number of primes up to " << n << " = " << n_primes[n] << "!\n";
}