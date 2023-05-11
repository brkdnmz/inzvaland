#include <bits/stdc++.h>
using namespace std;
using ll = long long;

bool is_square(ll x) {
    ll root = sqrt(x);
    while (root * root > x)
        root--;
    while ((root + 1) * (root + 1) <= x)
        root++;
    return root * root == x;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        ll x, y;
        cin >> x >> y;
        ll gcd = __gcd(x, y);
        x /= gcd, y /= gcd;
        bool ok = is_square(x) && is_square(y);
        cout << (ok ? "Yes" : "No") << "\n";
    }
}