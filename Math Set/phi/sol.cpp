#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    ll phi = n;
    for (ll i = 2; i * i <= n; i++) {
        if (n % i)
            continue;
        while (n % i == 0)
            n /= i;

        phi /= i, phi *= i - 1;
    }
    if (n > 1)
        phi /= n, phi *= n - 1;
    cout << phi << "\n";
}