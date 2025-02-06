#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;
    int mn = 1e9, mx = 0;
    vector<int> min_pos, max_pos;
    int a[n + 1];
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        a[i + 1] = x;
        if (x == mn)
            min_pos.push_back(i + 1);
        else if (x < mn)
            mn = x, min_pos = {i + 1};
        if (x == mx)
            max_pos.push_back(i + 1);
        else if (x > mx)
            mx = x, max_pos = {i + 1};
    }

    while (q--) {
        int g;
        cin >> g;

        int min_left = lower_bound(min_pos.begin(), min_pos.end(), g) - min_pos.begin();
        int min_right = min_left--;
        if (min_right < min_pos.size() && min_pos[min_right] == g)
            min_right++;

        int min_taken = min_left < 0                                      ? min_right
                        : min_right >= min_pos.size()                     ? min_left
                        : g - min_pos[min_left] <= min_pos[min_right] - g ? min_left
                                                                          : min_right;

        int max_left = lower_bound(max_pos.begin(), max_pos.end(), g) - max_pos.begin();
        int max_right = max_left--;
        if (max_right < max_pos.size() && max_pos[max_right] == g)
            max_right++;

        int max_taken = max_left < 0                                      ? max_right
                        : max_right >= max_pos.size()                     ? max_left
                        : g - max_pos[max_left] <= max_pos[max_right] - g ? max_left
                                                                          : max_right;

        if (a[g] - mn > mx - a[g]) {
            cout << min_pos[min_taken];
        } else if (a[g] - mn < mx - a[g]) {
            cout << max_pos[max_taken];
        } else {
            int a1 = 0 <= min_taken && min_taken < min_pos.size() ? min_pos[min_taken] : -1,
                a2 = 0 <= max_taken && max_taken < max_pos.size() ? max_pos[max_taken] : 1e9;
            cout << (a1 != -1 && abs(g - a1) < abs(g - a2) || (a1 < g && abs(g - a1) == abs(g - a2)) ? a1 : a2);
        }
        if (q)
            cout << "\n";
    }
}