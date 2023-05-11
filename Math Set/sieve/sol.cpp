#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<bool> is_prime(n + 1, 1);
    int ans = n - 1;
    for (int i = 2; i <= n; i++) {
        if (!is_prime[i]) {
            ans--;
            continue;
        }
        for (int k = 2 * i; k <= n; k += i)
            is_prime[k] = 0;
    }
    cout << ans << "\n";
}