#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

int main() {
    ll a, b;
    cin >> a >> b;
    a %= mod;
    b %= mod - 1; // optional
    ll ans = 1;
    while (b) {
        if (b & 1)
            (ans *= a) %= mod;
        b >>= 1;
        (a *= a) %= mod;
    }
    cout << ans << "\n";
}