#include <bits/stdc++.h>
using namespace std;

const int M = 18; // log2(2e5) (assuming n <= 2e5)

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    int a[n];
    for (int &x : a)
        cin >> x;

    int sp[n][M];

    for (int i = 0; i < n; i++)
        sp[i][0] = a[i];

    for (int j = 1; j < M; j++) {
        int r_offset = 1 << (j - 1);
        for (int i = 0; i < n; i++) {
            // You know what to do to support functions other than `min`, right?
            sp[i][j] = min(sp[i][j], sp[min(n - 1, i + r_offset)][j - 1]);
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;
        l--, r--; // 1-indexed to 0-indexed

        int len = r - l + 1;

        // 32 here would give the 1-indexed position of the leftmost 1-bit.
        // We want its exponent, which is 0-indexed.
        int lg = 31 - __builtin_clz(len); // Largest e s.t. 2^e <= len

        // You know what to do to support functions other than `min`, right? (again)
        int ans = min(sp[l][lg], sp[r - (1 << lg) + 1][lg]);

        // Alternative log(n) way
        int ans2 = sp[l][0]; // Just to initialize with something
        for (int i = M - 1; i >= 0; i--) {
            if (r - l + 1 >= (1 << i)) {
                ans2 = min(ans2, sp[l][i]);
                l += 1 << i;
            }
        }

        cout << ans << "\n";
    }
}