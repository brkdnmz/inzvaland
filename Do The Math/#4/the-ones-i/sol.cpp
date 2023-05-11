#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll cb(int x) { return 1ll * x * x * x; }

int main() {
    ll n;
    cin >> n;
    ll ans = 1;
    for (int i = 2; 1ll * i * i <= n; i++) {
        if (n % i)
            continue;
        int exp = 0;
        for (; n % i == 0; n /= i, exp++)
            ;
        ans *= cb(exp + 1) - cb(exp);
    }
    if (n > 1)
        ans *= 7;
    cout << ans << "\n";
}