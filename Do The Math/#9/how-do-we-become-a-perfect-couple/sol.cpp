#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    ll mask = 1;
    ll initial_n = n;
    for (ll i = 2; i * i <= n; i++) {
        while (n % (i * i) == 0)
            n /= i * i;
        if (n % i == 0)
            n /= i, mask *= i;
    }
    mask *= n;
    cout << int(sqrt(initial_n / mask)) << "\n";
}