#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int A = 1e5 + 5;

int main() {
    vector<bool> is_prime(A, 1);
    vector<int> primes;
    for (int i = 2; i < A; i++) {
        if (!is_prime[i])
            continue;
        primes.push_back(i);
        for (int k = 2 * i; k < A; k += i)
            is_prime[k] = 0;
    }

    int q;
    cin >> q;
    while (q--) {
        ll x;
        cin >> x;
        int n_divisors = 1;
        for (int p : primes) {
            if (1ll * p * p > x)
                break;
            int exp = 0;
            while (x % p == 0) {
                x /= p;
                exp++;
            }
            n_divisors *= exp + 1;
        }
        if (x > 1)
            n_divisors *= 2;
        cout << n_divisors << "\n";
    }
}