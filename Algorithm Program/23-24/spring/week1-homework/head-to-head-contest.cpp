#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 1e6 + 5;

// 1 + 2 + 3 + ... + x
ll gauss(int x) { return (ll)x * (x + 1) / 2; }

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int sum, n, x;
    cin >> sum >> n >> x;
    sum -= n;
    int l = 1, r = sum;
    while (l < r) {
        int mid = (l + r + 1) / 2;
        // Doğukan mid soru çözebilir mi?
        // mid-1 mid-2 mid-3...0

        ll left_required = gauss(mid - 1) - gauss(max(0, mid - x - 1));
        // mid-1 mid-2 ... mid-x (mid-x-1 ...)

        // n-1-x
        // mid-1 mid-2 ... mid-(n-1-x) -> Bundan sonra mid-(n-x)
        ll right_required = gauss(mid - 1) - gauss(max(0, mid - (n - x)));

        ll total_required = mid + left_required + right_required;
        if (total_required <= sum) {
            l = mid;
        } else {
            r = mid - 1;
        }
    }

    cout << l + 1 << "\n";
}