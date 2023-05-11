#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n = 1e7;
    vector<bool> is_prime(n + 1, 1);
    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (!is_prime[i])
            continue;
        primes.push_back(i);
        for (int k = 2 * i; k <= n; k += i) {
            is_prime[k] = 0;
        }
    }
    ll i = (ll)1234567 * 1234567;
    unordered_map<ll, int> exps;
    for (int p : primes) {
        if ((ll)p * p > i)
            break;
        if (i % p)
            continue;
        int exp = 0;
        while (i % p == 0) {
            i /= p;
            exp++;
        }
        exps[p] = exp;
    }
    if (i > 1) { // i might be a prime up to 10**14!
        exps[i] = 1;
    }
}
