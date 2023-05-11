#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    string s;
    cin >> s;
    int exp_10 = 2;
    bool seen_dot = false;
    ll n = 0;
    for (char c : s) {
        if (c == '.') {
            seen_dot = true;
            continue;
        }
        exp_10 += seen_dot;
        n = 10 * n + c - '0';
    }
    while (exp_10--) {
        if (n % 2 == 0)
            n /= 2;
        if (n % 5 == 0)
            n /= 5;
    }
    cout << n << "\n";
}