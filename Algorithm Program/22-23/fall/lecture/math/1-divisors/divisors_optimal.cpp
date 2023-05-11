// https://ideone.com/acmpIs
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
    ll n = 1234567891011;
    vector<ll> positive_divisors;
    // i <= sqrt(n) is identical to i*i <= n
    // Adding a factor of 1ll (literal for 64-bit 1) makes the expression's result long long (64 bits)
    for (int i = 1; 1ll * i * i <= n; i++) {
        if (n % i)
            continue; // r > 0
        // i is a divisor
        positive_divisors.push_back(i);
        // n/i is the complementary (larger) divisor
        // however, check if i != n/i (occurs only when n is a perfect square)
        if (i != n / i) {
            positive_divisors.push_back(n / i);
        }
    }
    int n_positive_divisors = positive_divisors.size();
    cout << "n: " << n << "\n";
    cout << "Number of positive divisors: " << n_positive_divisors << "\n";
    cout << "Number of all divisors: " << 2 * n_positive_divisors << "\n";
    cout << "Positive divisors:\n";
    for (ll d : positive_divisors) {
        cout << d << " ";
    }
    cout << "\n";
}