#include <bits/stdc++.h>
using namespace std;

int post_decrement(int &x) {
    int tmp = x;
    x -= 1;
    return tmp;
}

int main() {
    int q;
    cin >> q;

    map<int, bool> mp;

    while (q--) {
        char t;
        cin >> t;

        if (t == '1') {
            int x;
            cin >> x;
            mp[x];
        } else {
            int a, b;
            cin >> a >> b;

            // a, a-b, a+b
            bool ok = mp.count(a) && mp.count(a - b) && mp.count(a + b);

            cout << (ok ? "GG EZ" : "GLHF") << "\n";
        }
    }
}