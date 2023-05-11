#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    n++;
    int ans = -1;
    for (int i = 1; 1ll * i * i <= n; i++) {
        if (n % i)
            continue;
        ans += 1 + (i != n / i);
    }
    cout << ans << "\n";
}