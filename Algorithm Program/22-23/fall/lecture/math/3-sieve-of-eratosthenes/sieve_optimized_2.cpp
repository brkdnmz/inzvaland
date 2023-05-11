// https://ideone.com/RLkzSo
#include <iostream>
#include <vector>
using namespace std;

vector<bool> sieve(int n) {
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;

    for (int i = 2; i <= n; i++) {
        if (!is_prime[i])
            continue;

        if (i * i > n) // To prevent any overflow, just break since the inner loop won't be executed anymore
            break;

        for (int multiple = i * i; multiple <= n; multiple += i) {
            is_prime[multiple] = false;
        }
    }
    return is_prime;
}

int main() {
    int n = 1e8;
    vector<bool> is_prime = sieve(n);
    int n_primes = 0;
    for (int i = 2; i <= n; i++) {
        n_primes += is_prime[i];
    }
    cout << "Number of primes up to " << n << " = " << n_primes << "!\n";
}