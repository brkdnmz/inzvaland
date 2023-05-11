#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    ll ans = 1;
    for (int i = 2; 1ll * i * i <= n; i++) {
        int exp = 0;
        while (n % i == 0) {
            n /= i;
            exp++;
        }
        ans *= 2 * exp + 1;
    }
    if (n > 1)
        ans *= 3;
    cout << ans << "\n";
}