#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 1e6;

const int mod = 1e9 + 7;

int exp(int base, int exponent) {
    int result = 1;
    while (exponent) {
        if (exponent % 2)
            result = 1ll * result * base % mod;
        exponent /= 2;
        base = 1ll * base * base % mod;
    }
    return result;
}

int main() {
    // For fast cin / cout!
    // If we don't put this line, the I/O operations take much more time than our actual algorithm.
    ios::sync_with_stdio(0), cin.tie(0);
    // Instead of cin / cout, you may use printf / scanf. They're also always proper.
    // If you wonder, I ALWAYS use cin / cout since I love their syntaxes.

    // Sieve
    vector<int> prime_divisor(N + 1); // auto initialized to 0
    vector<int> primes;
    for (int p = 2; p <= N; p++) {
        // This line was faulty while we were trying to solve during the solution hour :D
        // It was written !prime_divisor[p], in which case p is a prime :DD
        if (prime_divisor[p])
            continue;
        prime_divisor[p] = p;
        primes.push_back(p);
        if (1ll * p * p > N)
            continue;
        for (int k = p * p; k <= N; k += p) {
            prime_divisor[k] = p;
        }
    }

    int n;
    cin >> n;

    /*
        0.  We need a data structure that stores (key, value) pairs where key might be too big (1e12),
            and gets / updates the value of a specific key fast.
            We use it to update the prime factorization after each multiplication.
    */
    unordered_map<ll, int> factorization;

    for (int i = 0; i < n; i++) {
        ll x;
        cin >> x;

        /*
            1. Factorize x to update exponents of the product.
        */
        if (x <= N) {
            while (x > 1) {
                int p = prime_divisor[x];
                int exponent = 0;
                while (x % p == 0) {
                    x /= p;
                    exponent++;
                    // factorization[p]++;
                }
                factorization[p] += exponent;
            }
        } else { // <= 1e12
            for (int p : primes) {
                // p <= sqrt(x)
                // p*p <= x
                if (1ll * p * p > x)
                    break;
                if (x % p)
                    continue; // x % p != 0
                int exponent = 0;
                while (x % p == 0) {
                    x /= p;
                    exponent++;
                }
                factorization[p] += exponent;
            }
            if (x > 1) {
                factorization[x]++;
            }
        }

        /*
            2. Find the number of coprime positive pairs (a, b) s.t. a * b = a1 * a2 * ... * ai
            Hint: If one is divisible by a prime, the other one must not be.
        */
        int n_primes = factorization.size();
        cout << exp(2, n_primes) << "\n"; // Don't you ever use "endl"!
        // Note: Binary exponentiation is not necessary. You may figure out other ways.
        // Hint: How to update 2^k after each a_i?
    }

    int n_divisors = 2;

    // 3. Find the number of divisors of the product of all a_i.
    // Use exponents!
    for (auto [prime, exponent] : factorization) {
        n_divisors = 1ll * n_divisors * (exponent + 1) % mod;
    }

    cout << n_divisors << "\n";
}