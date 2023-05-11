#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int A = 5e6 + 5;

int main() {
    vector<int> spf(A);
    for (int i = 2; i < A; i++) {
        if (spf[i])
            continue;
        for (int k = i; k < A; k += i)
            if (!spf[k])
                spf[k] = i;
    }

    int q;
    cin >> q;
    while (q--) {
        int x;
        cin >> x;
        int n_divisors = 1;
        vector<int> primes;
        while (x > 1) {
            int p = spf[x];
            int exp = 0;
            while (x % p == 0) {
                x /= p;
                exp++;
                primes.push_back(p);
            }
            n_divisors *= exp + 1;
        }
        cout << n_divisors << "\n";
        for (int p : primes)
            cout << p << " ";
        cout << "\n";
    }
}