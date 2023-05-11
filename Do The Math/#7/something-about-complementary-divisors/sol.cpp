#include <bits/stdc++.h>
using namespace std;

const int N = 5e6;
const int mod = 1e9 + 7;
int main() {
    // vector<int> n_divisors(N + 1, 0);
    vector<int> prime_div(N + 1);
    for (int i = 2; i <= N; i++) {
        if (prime_div[i])
            continue;
        prime_div[i] = i;
        if (1ll * i * i > N)
            continue;
        for (int k = i * i; k <= N; k += i)
            prime_div[k] = i;
        // for (int k = i; k <= N; k += i)
        //     n_divisors[k]++;
    }

    int q;
    cin >> q;
    while (q--) {
        int n;
        cin >> n;
        int n_divs = 1;
        while (n > 1) {
            int p = prime_div[n];
            int exp = 0;
            while (n % p == 0)
                n /= p, exp++;
            n_divs *= exp + 1;
        }
        int ans = 1;
        for (int i = 0; i < n_divs / 2; i++)
            ans = 1ll * ans * 3 % mod;
        if (n_divs % 2)
            (ans *= 2) %= mod;
        cout << ans << "\n";
    }
}