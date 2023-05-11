#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

int main() {
    int n;
    cin >> n;
    ll ans = 1;
    for (int i = 2; i <= n; i++)
        (ans *= i) %= mod;
    cout << ans << "\n";
}