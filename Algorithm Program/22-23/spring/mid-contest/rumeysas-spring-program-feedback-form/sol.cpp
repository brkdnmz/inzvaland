#include <bits/stdc++.h>
using namespace std;

const int N = 215;
const int mod = 1e9 + 7;
vector<vector<vector<int>>> dp(N + 1, vector<vector<int>>(N + 1, vector<int>(N + 1, -1)));

void add(int &a, int b) {
    a += b;
    if (a >= mod)
        a -= mod;
    if (a < 0)
        a += mod;
}

int factor(int a, int b, int c) {
    return 1 + (a + b + c > 0);
}

int rec(int a, int b, int c) {
    if (a < 0 || b < 0 || c < 0)
        return 0;
    int &cur = dp[a][b][c];
    if (~cur)
        return cur;
    cur = 0;
    add(cur, factor(a - 1, b, c) * rec(a - 1, b, c) % mod);
    add(cur, factor(a, b - 1, c) * rec(a, b - 1, c) % mod);
    add(cur, factor(a, b, c - 1) * rec(a, b, c - 1) % mod);
    add(cur, -factor(a - 1, b - 1, c) * rec(a - 1, b - 1, c) % mod);
    add(cur, -factor(a - 1, b, c - 1) * rec(a - 1, b, c - 1) % mod);
    add(cur, -factor(a, b - 1, c - 1) * rec(a, b - 1, c - 1) % mod);
    add(cur, factor(a - 1, b - 1, c - 1) * rec(a - 1, b - 1, c - 1) % mod);
    return cur;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    dp[0][0][0] = 1;
    int q;
    cin >> q;
    while (q--) {
        int a, b, c;
        cin >> a >> b >> c;
        cout << rec(a, b, c) << "\n";
    }
}