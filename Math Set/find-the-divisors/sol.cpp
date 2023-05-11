#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll n;
    cin >> n;
    vector<ll> divisors;
    for (ll divisor = 1; divisor * divisor <= n; divisor++) {
        if (n % divisor)
            continue;
        divisors.push_back(divisor);
        if (divisor * divisor != n)
            divisors.push_back(n / divisor);
    }
    sort(divisors.begin(), divisors.end());
    cout << divisors.size() << "\n";
    for (ll divisor : divisors) {
        cout << divisor << " ";
    }
    cout << "\n";
}