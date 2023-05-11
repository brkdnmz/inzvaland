#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    ll ans = n;
    for (int i = 2; 1ll * i * i <= n; i++) {
        while (n % i == 0) {
            n /= i;
            ans += n;
        }
    }
    if (n > 1)
        ans++;
    cout << ans << "\n";
}