#include <bits/stdc++.h>
using namespace std;

const int N = 5e6 + 5;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> n_primes(N, 1);
    n_primes[0] = n_primes[1] = 0;
    for (int i = 2; i < N; i++) {
        n_primes[i] += n_primes[i - 1];
        if (n_primes[i] == n_primes[i - 1])
            continue;
        for (int k = 2 * i; k < N; k += i)
            n_primes[k] = 0;
    }
    int q;
    cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << n_primes[r] - n_primes[l - 1] << "\n";
    }
}