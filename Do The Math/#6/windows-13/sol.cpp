#include <bits/stdc++.h>
using namespace std;

const int N = 15e5;
const int S = 10;
int main() {
    vector<int> n_divisors(N + S + 1);
    for (int i = 1; i <= N + S; i++) {
        n_divisors[i] += n_divisors[i - 1];
        for (int k = i; k <= N + S; k += i)
            n_divisors[k]++;
    }
    int q;
    cin >> q;
    while (q--) {
        int n, s;
        cin >> n >> s;
        int ans = n_divisors[n + s] - n_divisors[n - 1];
        for (int i = 1; i <= s; i++) {
            ans -= (n + s) / i - (n - 1) / i - 1;
        }
        cout << ans << "\n";
    }
}