#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    // 2.694.111.336
    ll n = (ll)2 * 2 * 2 * 3 * 3 * 7 * 7 * 7 * 43 * 59;

    /**
     * Store the exponents of primes in the factorization in some data structures. May also use map but hashmap is faster!
     * If you're sure any prime factor fits in int, then you may use array instead of map. (e.g. n <= 10^7)
     */
    unordered_map<ll, int> exps;
    for (ll d = 2; d * d <= n; d++) {
        if (n % d)
            continue;
        int exp = 0;
        while (n % d == 0) {
            n /= d;
            exp++;
            // Could also write exps[d]++ but every access to the map itself has a cost > O(1)
        }
        exps[d] = exp;
    }

    // Occurs only when n's largest prime divisor's exponent is 1
    // In fact, n becomes that divisor after the loop above!
    if (n > 1) {
        exps[n] = 1;
    }

    // Do whatever you wanna do with exps
    int n_divisors = 1;
    for (auto &[prime, exp] : exps) {
        n_divisors *= exp + 1;
    }
    cout << n_divisors << "\n";
}
