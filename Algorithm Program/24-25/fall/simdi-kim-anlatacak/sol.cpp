#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int LOG = 18;

int main(int argc, char **argv) {
    // freopen(argv[1], "r", stdin);
    // freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    multiset<int> a[10];
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < n; j++) {
            int x;
            cin >> x;
            a[i].insert(x);
        }
    }
    int cnt = n * 10;
    int prev = -1, prev_a = -1;
    int cnt_nonempty = 10;
    while (cnt--) {
        int mn = 1e9 + 1, tar = -1;
        for (int i = 0; i < 10; i++) {
            auto it = a[i].lower_bound(prev);
            if (it != a[i].end() && *it < mn && (prev_a != i || cnt_nonempty == 1)) {
                mn = *it;
                tar = i;
            }
        }
        prev_a = tar;
        a[tar].erase(a[tar].find(mn));
        cnt_nonempty -= a[tar].empty();
        cout << mn;
        if (cnt)
            cout << " ";
    }
}