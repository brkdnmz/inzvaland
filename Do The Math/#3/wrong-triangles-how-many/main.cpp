#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    ll ans = 0;
    for (int i = 1; 1ll * i * i < n; i++) {
        if (n % i)
            continue;
        ll other = n / i;
        ans += i % 2 == other % 2;
    }
    cout << ans << "\n";
}