#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct F {
    int p, q;
    bool operator<(const F &o) const {
        return p * o.q > o.p * q;
    }
};

const int mod = 1e9 + 7;

int main() {
    int n;
    cin >> n;
    map<F, int> dp;
    dp[{0, 1}] = 1;
    while (n--) {
        int x;
        cin >> x;
        for (auto [f, ans] : dp) {
            auto [p, q] = f;
            // p / q + 1 / x
            int new_p = p * x + q;
            int new_q = q * x;
            if (new_p > new_q)
                continue;

            int gcd = __gcd(new_p, new_q);
            new_p /= gcd;
            new_q /= gcd;
            (dp[{new_p, new_q}] += dp[{p, q}]) %= mod;
        }
    }
    cout << dp[{1, 1}] << "\n";
}