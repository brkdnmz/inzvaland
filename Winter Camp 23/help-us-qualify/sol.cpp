#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll h, m;
    cin >> h >> m;
    ll n = 60 * h + m;
    for (int i = 1; 1ll * i * i <= n; i++) {
        if (n % i)
            continue;
        if (!((i + 1) % 60) || !((n / i + 1) % 60)) {
            cout << "YES\n";
            return 0;
        }
    }
    cout << "NO\n";
}