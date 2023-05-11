// https://ideone.com/d6ZLLE
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<int> primes;

void sieve(int n) {
    vector<bool> is_prime(n + 1, 1);
    is_prime[0] = is_prime[1] = 0;
    for (int i = 2; i <= n; i++) {
        if (!is_prime[i])
            continue;

        primes.push_back(i);
        for (int factor = i; factor <= n / i; factor++) {
            is_prime[factor * i] = 0;
        }
    }
}

struct PrimePower {
    ll prime;
    int exponent;
};

vector<PrimePower> factorize(ll n) {
    vector<PrimePower> factorization;

    for (int prime : primes) {
        if (1ll * prime * prime > n)
            break;
        if (n % prime)
            continue;

        PrimePower p{prime, 0};
        while (n % prime == 0) {
            n /= prime;
            p.exponent++;
        }
        factorization.push_back(p);
    }

    if (n > 1) {
        factorization.push_back({n, 1});
    }

    return factorization;
}

int main() {
    ll n = 10512969114312ll;
    int sieve_bound = sqrt(n) + 5; // +5 is to overcome precision errors! (might also be +1)
    sieve(sieve_bound);            // Find the primes up to sqrt(n)
    vector<PrimePower> factorization = factorize(n);

    cout << "n = " << n << " = ";
    for (PrimePower &prime_power : factorization) {
        cout << prime_power.prime << "^" << prime_power.exponent;
        if (prime_power.prime < factorization.back().prime)
            cout << " * ";
    }
    cout << "\n";
}