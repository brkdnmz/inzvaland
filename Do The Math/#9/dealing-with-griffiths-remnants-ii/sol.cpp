#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    string s;
    cin >> s;
    int pw10 = 100;
    bool seen_dot = false;
    int n = 0;
    for (char c : s) {
        if (c == '.') {
            seen_dot = true;
            continue;
        }
        if (seen_dot)
            pw10 *= 10;
        n = 10 * n + c - '0';
    }
    cout << n / __gcd(n, pw10) << "\n";
}