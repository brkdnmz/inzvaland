#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
const int N = 5e6;
int main() {
    ull lcm[100];
    lcm[0] = 1;
    int mx = 0;
    for (int i = 1; i < 100; i++) {
        mx = i - 1;
        ull cur_lcm = lcm[i - 1] / __gcd(lcm[i - 1], 1ull * i) * i;
        if (cur_lcm > 1e18)
            break;
        lcm[i] = cur_lcm;
    }

    cout << fixed << setprecision(20) << 1e18 + (double)1 << "\n";

    int q;
    cin >> q;
    while (q--) {
        ull l, r, k;
        cin >> l >> r >> k;
        ull lcm_k = k <= mx ? lcm[k] : 2e18;
        ull lcm_k_1 = (k + 1) <= mx ? lcm[k + 1] : 2e18;
        cout << r / lcm_k - r / lcm_k_1 - ((l - 1) / lcm_k - (l - 1) / lcm_k_1) << "\n";
    }
}