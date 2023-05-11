#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const int N = 3e6;
int main() {
    int q;
    cin >> q;
    vector<bool> is_p(N + 1, 1);
    vector<int> ans(N + 1, 1);
    for (int i = 2; i <= N; i++) {
        ans[i] = ans[i - 1];
        if (!is_p[i])
            continue;
        ans[i] = 1ll * ans[i] * i % mod;
        for (int k = 2 * i; k <= N; k += i)
            is_p[k] = 0;
    }
    while (q--) {
        int n;
        cin >> n;
        cout << ans[n] << " ";
    }
}