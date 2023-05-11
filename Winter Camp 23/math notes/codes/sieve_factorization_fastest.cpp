#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n = 1e7;
    vector<int> prime_divisor(n + 1, 0);
    // Still n * log log(n)!
    for (int i = 2; i <= n; i++) {
        if (prime_divisor[i]) // i isn't a prime, it has a smaller prime divisor
            continue;
        for (int k = i; k <= n; k += i) {
            prime_divisor[k] = i;
            // Might also do this to keep only the smallest prime divisor:
            // if(!prime_divisor[k]) prime_divisor[k] = i;
        }
    }
    // Factorize i in log(i) steps!
    int i = 987654;
    int n_divisors = 1;
    while (i > 1) {
        int p = prime_divisor[i];
        int exp = 0;
        while (i % p == 0) {
            i /= p;
            exp++;
        }
        n_divisors *= exp + 1;
    }
}
