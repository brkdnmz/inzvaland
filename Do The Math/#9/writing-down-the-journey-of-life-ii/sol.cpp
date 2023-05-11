#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    int m;
    cin >> n >> m;
    ll overall_gcd = n + 1;
    while (m--) {
        ll line;
        cin >> line;
        overall_gcd = __gcd(overall_gcd, line);
    }
    int n_divisors = -1; // exclude overall_gcd itself!
    for (int i = 1; 1ll * i * i <= overall_gcd; i++) {
        if (overall_gcd % i)
            continue;
        n_divisors += 1 + (i != overall_gcd / i);
    }
    cout << n_divisors << "\n";
}