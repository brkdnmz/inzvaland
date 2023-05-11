#include <bits/stdc++.h>
using namespace std;

bool is_p(int x) {
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0)
            return false;
    return true;
}

int calc_max_exp(int b, int n) {
    int exp = 0;
    int cur = 1;
    while (1ll * cur * b <= n) {
        cur *= b;
        exp++;
    }
    return exp;
}

int main() {
    int n;
    cin >> n;
    int ans = 1;
    int mod = 1e9 + 7;
    for (int i = 2; i <= n; i++) {
        if (!is_p(i))
            continue;
        ans = 1ll * ans * (calc_max_exp(i, n) + 1) % mod;
    }
    cout << ans << "\n";
}