#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

int main() {
    ll n;
    cin >> n;
    ll ans = 1;
    ll power = n;
    for (int i = 2; 1ll * i * i <= n; i++) {
        int exp = 0;
        while (n % i == 0) {
            n /= i;
            exp++;
        }
        (ans *= power * exp % mod + 1) %= mod;
    }
    if (n > 1)
        (ans *= power % mod + 1) %= mod;
    cout << ans << "\n";
}