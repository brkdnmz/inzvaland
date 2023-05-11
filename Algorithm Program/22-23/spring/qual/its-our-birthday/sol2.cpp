#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 1e4 + 5;
const int M = 10;
const int mod = 1e9 + 7;

ll invexp(ll x) {
    ll exp = mod - 2;
    ll ans = 1;
    while (exp) {
        if (exp & 1)
            ans = ans * x % mod;
        exp >>= 1;
        x = x * x % mod;
    }
    return ans;
}

int cnt[M + 1];
int taken_cnt[M + 1];
ll f[N], invf[N];

ll C(int a, int b) {
    return f[a] * invf[a - b] % mod * invf[b] % mod;
}

int lc = 1;
ll res;

void rec(int i = 1, int sum = 0) {
    if (i == M + 1) {
        if (sum != lc)
            return;
        ll ans = 1;
        for (int i = 1; i <= M; i++) {
            (ans *= C(cnt[i], taken_cnt[i])) %= mod;
        }
        (res += ans) %= mod;
        return;
    }
    int cur = lc / i;
    for (int j = 0; j <= cnt[i] && sum <= lc; j++, sum += cur) {
        taken_cnt[i] = j;
        rec(i + 1, sum);
    }
}

int main() {
    f[0] = 1;
    invf[0] = 1;
    for (int i = 1; i < N; i++) {
        f[i] = f[i - 1] * i % mod;
        invf[i] = invexp(f[i]);
    }
    for (int i = 2; i <= M; i++) {
        lc = lc / __gcd(lc, i) * i;
    }
    int n;
    cin >> n;
    while (n--) {
        int x;
        cin >> x;
        cnt[x]++;
    }
    rec();
    cout << res << "\n";
}