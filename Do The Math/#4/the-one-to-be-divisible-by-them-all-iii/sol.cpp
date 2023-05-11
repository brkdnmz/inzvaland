#include <bits/stdc++.h>
using namespace std;

int main() {
    int q;
    cin >> q;
    int N = 5e6;
    vector<int> n_primes(N + 1, 1);
    n_primes[0] = n_primes[1] = 0;
    for (int i = 2; i <= N; i++) {
        n_primes[i] += n_primes[i - 1];
        if (n_primes[i] == n_primes[i - 1])
            continue;
        for (int k = 2 * i; k <= N; k += i)
            n_primes[k] = 0;
    }
    while (q--) {
        int n;
        cin >> n;
        cout << n_primes[n] << "\n";
    }
}