#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int A = 5e6 + 5;
const int mod = 1e9 + 7;

int main() {
    vector<int> prime_factor(A);
    for (int i = 2; i < A; i++) {
        if (prime_factor[i])
            continue;
        for (int k = i; k < A; k += i)
            prime_factor[k] = i;
    }

    int n;
    cin >> n;

    vector<int> exponents(A);

    while (n--) {
        int x;
        cin >> x;
        while (x > 1) {
            int p = prime_factor[x];
            int exp = 0;
            while (x % p == 0) {
                x /= p;
                exp++;
            }
            exponents[p] = max(exponents[p], exp);
        }
    }
    ll ans = 1;
    for (int i = 2; i < A; i++) {
        for (int j = 0; j < exponents[i]; j++)
            (ans *= i) %= mod;
    }
    cout << ans << "\n";
}