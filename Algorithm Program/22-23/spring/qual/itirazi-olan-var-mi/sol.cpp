#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n];
    for (int &x : a)
        cin >> x;
    int prefix_max[n];
    int suffix_max[n];
    for (int i = 0; i < n; i++) {
        prefix_max[i] = max(i ? prefix_max[i - 1] : 0, a[i]);
    }
    for (int i = n - 1; i >= 0; i--) {
        suffix_max[i] = max(i + 1 < n ? suffix_max[i + 1] : 0, a[i]);
    }
    array<int, 2> ans[n];
    auto find_l = [&](int i) {
        int l = 0, r = i;
        while (l < r) {
            int mid = (l + r) / 2;
            if (prefix_max[mid] < a[i])
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    };
    auto find_r = [&](int i) {
        int l = i, r = n - 1;
        while (l < r) {
            int mid = (l + r + 1) / 2;
            if (suffix_max[mid] < a[i])
                r = mid + -1;
            else
                l = mid;
        }
        return l;
    };
    for (int i = 0; i < n; i++) {
        cout << find_l(i) << " " << find_r(i) << "\n";
    }
}