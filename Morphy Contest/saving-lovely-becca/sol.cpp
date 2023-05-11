#include <bits/stdc++.h>
using namespace std;
using ll = long long;

/*
def required_rotation_angle(self, a1: int, a2: int) -> int:
        a1 %= 360
        a2 %= 360
        diff = abs(a2 - a1)
        return min(diff, 360 - diff)
*/

int required_rotation_angle(int a1, int a2) {
    a1 %= 360;
    a2 %= 360;
    int diff = abs(a1 - a2);
    return min(diff, 360 - diff);
}

int main() {
    int n;
    cin >> n;
    int r[n];
    ll all_sum = 0;
    for (int i = 0; i < n; i++)
        cin >> r[i], all_sum += r[i] * r[i];
    int a[n - 1];
    for (int i = 0; i < n - 1; i++)
        cin >> a[i];
    ll prefix_sum = 0;
    ll ans = 0;
    for (int i = 1; i < n - 1; i++) {
        prefix_sum += r[i - 1] * r[i - 1];
        ans += required_rotation_angle(a[i - 1], a[i]) * min(prefix_sum, all_sum - prefix_sum - r[i] * r[i]);
    }
    cout << ans << "\n";
}