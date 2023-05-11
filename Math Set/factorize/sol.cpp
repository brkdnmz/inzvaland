#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    vector<ll> factorization;
    for (ll divisor = 2; divisor * divisor <= n; divisor++) {
        while (n % divisor == 0) {
            n /= divisor;
            factorization.push_back(divisor);
        }
    }
    if (n > 1)
        factorization.push_back(n);
    for (ll prime : factorization) {
        cout << prime << " ";
    }
    cout << "\n";
}