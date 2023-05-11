#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int m, r;
    cin >> m >> r;
    int ans = 1;
    int mod = 1e9 + 7;
    r--;
    while (r--)
        (ans *= 2) %= mod;
    cout << ans << "\n";
}