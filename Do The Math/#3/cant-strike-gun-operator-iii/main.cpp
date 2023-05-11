#include <bits/stdc++.h>
using namespace std;

#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define REVERSE(v) reverse((v).begin(), (v).end())
#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))
#define pb push_back
#define FOR(i, n) for (int i = 0; i < (n); i++)
typedef long long ll;
typedef unsigned long long ull;

int mod = 1e9 + 7;
// int mod = 998244353;

inline void sum_self(int &a, int b) {
    a += b;
    if (a >= mod)
        a -= mod;
    if (a < 0)
        a += mod;
}
inline int sum(int a, int b) {
    a += b;
    if (a >= mod)
        a -= mod;
    if (a < 0)
        a += mod;
    return a;
}
inline void mul_self(int &a, int b) { a = 1ll * a * b % mod; }
inline int mul(int a, int b) {
    a = 1ll * a * b % mod;
    return a;
}
inline int exp(ll b, ll p) {
    if (p < 0)
        return 0;
    b %= mod;
    int res = 1;
    int mul = b;
    while (p) {
        if (p & 1)
            mul_self(res, mul);
        p >>= 1;
        mul_self(mul, mul);
    }
    return res;
}
inline int invexp(ll b) { return exp(b, mod - 2); } // 1/i modulo mod

const int N = 5e4 + 5;
int rec(int m, int r, int M) {
    if (!m && !r) {
        return 1;
    }
    int ans = 0;
    if (m && (r > M - m || !r)) {
        ans += rec(m - 1, r, M);
    }

    if (r && m < M) {
        ans += rec(m + min(M - m, r), r - min(M - m, r), M);
    }
    return ans;
}

void solve() {
    int m, r;
    cin >> m >> r;
    int ans = exp(2, r - 1);
    for (int i = 0; i <= r - (m + 1); i++) {
        // put m+1+i in one
        // distribute the rest r - (m+1 + i)
        int exc = 1; // m+1+i == r
        if (r - (m + 1) - i)
            exc = exp(2, r - (m + 1 + i)); // only on one side
        if (r - (m + 1) - i > 1)
            sum_self(exc,
                     mul(r - (m + 1 + i) - 1, exp(2, (r - (m + 1 + i) - 2))));
        exc %= mod;
        sum_self(ans, -exc);
    }
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }
}