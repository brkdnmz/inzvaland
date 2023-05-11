#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Or use the built-in __gcd!
int gcd(int a, int b) {
    return !a ? b : gcd(b % a, a);
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        int a, b;
        cin >> a >> b;
        cout << 1ll * a * b / gcd(a, b) << "\n";
    }
}