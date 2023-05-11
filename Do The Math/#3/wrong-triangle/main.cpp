#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    ll ans = n / 2 - n / 4 + 1 + (n >= 4);
    cout << ans << "\n";
}