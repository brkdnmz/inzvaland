#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    srand(time(0));
    int n = 1e6;
    int k = rand() % 100 + 1;
    cout << "k: " << k << "\n";
    ll gcd = 0;
    // ll minimum = 1e18;
    for (int i = 0; i < n; i++) {
        ll x = 1ll * rand() * k;
        gcd = __gcd(x, gcd);
        // minimum = min(minimum, x);
    }
    // k * 4, k * 6, k * 8
    cout << "gcd: " << gcd << "\n";
}