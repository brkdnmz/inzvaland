#include <bits/stdc++.h>
using namespace std;
using ll = long long; // Code faster!

int main() {
    // Too big to find divisors in O(n)
    ll n = 1234567ll * 1234567;
    int n_divisors = 0;
    /**
     * d <= sqrt(n) -> d^2 <= n
     * no need to use any function to compute sqrt!
     */
    for (ll d = 1; d * d <= n; d++) {
        /**
         * Instead of adding an extra scope:
         * if(n % d == 0){
         *  ...
         * }
         *
         * Continue when what you want isn't satisfied
         */
        if (n % d)
            continue;

        n_divisors++;
        // Complementary divisor
        ll k = n / d;
        // Equality holds only when n is a perfect square
        // and d = sqrt(n) (d * d = n)
        if (d != k) {
            n_divisors++;
        }
    }
    cout << n_divisors << "\n";
}
