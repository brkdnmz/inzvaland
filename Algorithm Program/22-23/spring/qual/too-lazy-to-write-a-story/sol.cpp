#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    array<int, 2> a[n];
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        a[i] = {x, i};
    }
    sort(a, a + n);
    ll ans = 0;
    for (int i = 1; i < n; i++) {
        ans += abs(a[i][1] - a[i - 1][1]);
    }
    cout << ans << "\n";
}