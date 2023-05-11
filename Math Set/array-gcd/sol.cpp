#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Or use the built-in __gcd!
ll gcd(ll a, ll b) {
    return !a ? b : gcd(b % a, a);
}

int main() {
    int n;
    cin >> n;
    ll ans = 0;
    while (n--) {
        ll x;
        cin >> x;
        ans = gcd(ans, x);
    }
    cout << ans << "\n";
}