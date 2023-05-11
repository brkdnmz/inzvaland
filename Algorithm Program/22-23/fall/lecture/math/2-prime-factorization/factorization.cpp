// https://ideone.com/NH7x3F
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

// Wrapper for prime factorization elements
struct Divisor {
    ll prime;
    int exponent;
};

int main() {
    ll n = 10512969114312ll; // Put ll or LL to the end to specify 64-bit literal
    vector<Divisor> prime_powers;
    ll initial_n = n;
    for (int i = 2; 1ll * i * i <= n; i++) {
        if (n % i)
            continue; // r > 0
        // i is a prime divisor
        Divisor divisor{i, 0};
        // While n is divisible by i, divide and increment the exponent
        // Observe that n itself is modified. Therefore, the loop condition changes.
        while (n % i == 0) {
            n /= i;
            divisor.exponent++;
        }
        // The prime factorization includes "divisor"
        prime_powers.push_back(divisor);
    }
    // n became a prime itself
    if (n > 1) {
        // Factorization includes n^1
        prime_powers.push_back(Divisor{n, 1});
    }
    cout << "n = " << initial_n << " = ";
    for (Divisor d : prime_powers) {
        cout << d.prime << "^" << d.exponent;
        if (d.prime != prime_powers.back().prime)
            cout << " * ";
    }
    cout << "\n";
}