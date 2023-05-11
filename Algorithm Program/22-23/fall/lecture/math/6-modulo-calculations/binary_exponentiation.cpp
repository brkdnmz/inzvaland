// https://ideone.com/AoHkEA
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

int binary_exponentiation(ll base, ll exponent, bool take_exponent_mod = false) {
    // The base can also be huge. Remember the properties of multiplication modulo m:
    //   We may take base % m beforehand since we just trying to compute base * base * base * ... * base (exponent times).
    base %= mod;

    // In fact, you can take exponent % (m - 1) — remember base^(m - 1) = 1 (mod m)
    if (take_exponent_mod)
        exponent %= mod - 1;

    int result = 1;
    // Find the powers of 2 in exponent's binary representation,
    // and simultaneously, multiply base with itself (base^2, base^4, base^8,...)
    // That is, they can be done simultaneously.
    while (exponent) {
        // 2's power is taken only if current value of exponent is odd!
        if (exponent & 1) { // bitwise AND, identical to exponent % 2
            result = 1ll * result * base % mod;
        }

        exponent /= 2; // or exponent >>= 1 (right shift, i.e., shift bits one to the right, drop the last bit)

        // Multiply base with itself to get the next value in [base^2, base^4, base^8,...]
        base = 1ll * base * base % mod;
    }

    return result;
}

int main() {
    ll base = 1e18, exponent = 1e18;
    cout << base << "^" << exponent << " modulo " << mod << ": " << binary_exponentiation(base, exponent) << "\n";
    cout << base << "^" << exponent % mod << " modulo " << mod << " (took exponent mod m): " << binary_exponentiation(base, exponent, true) << "\n";
}