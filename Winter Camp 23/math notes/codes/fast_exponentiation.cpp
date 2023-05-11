#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll fast_exp(ll a, ll b, int m) {
    // If m is a prime and a != m*k, can do the following:
    // b %= m-1;

    // Can do this without any restrictions!
    a %= m;

    ll result = 1;
    while (b) { // Find c_i's while b > 0
        bool c_i = b % 2;
        if (c_i) {
            result = result * a % m;
        }
        b /= 2;

        // a becomes a^(2^i)
        a = a * a % m;
    }

    return result;
}

int main() {
    ll a = 123456789101112ll;
    ll b = 1e18;
    int m = 1e9 + 7;
    cout << fast_exp(a, b, m) << "\n";
}
