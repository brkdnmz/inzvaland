// https://ideone.com/NyqgrL
#include <iostream>
#include <vector>
using namespace std;

vector<bool> sieve(int n) {
    // Initially, every integer is marked as prime.
    // By convention, we named the array "is_prime" instead of "is_composite".
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false; // Should mark them by hand

    // Now, start marking composites
    for (int i = 2; i <= n; i++) {
        for (int multiple = 2 * i; multiple <= n; multiple += i) { // n/i iterations
            is_prime[multiple] = false;
        }
    }
    return is_prime;
}

int main() {
    int n = 1e6;
    vector<bool> is_prime = sieve(n);
    int n_primes = 0;
    for (int i = 2; i <= n; i++) {
        n_primes += is_prime[i];
    }
    cout << "Number of primes up to " << n << " = " << n_primes << "!\n";
}