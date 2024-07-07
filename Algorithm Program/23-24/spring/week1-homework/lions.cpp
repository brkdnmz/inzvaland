#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;
    int lions[n];
    for (int &x : lions)
        cin >> x;
    sort(lions, lions + n);

    // 1 2 3 4
    // lions -> 1
    // lions + 1 -> 2
    // lions + 2 -> 3
    // lions + 3 -> 4

    // for(int i = 0; i < q; i++)
    int l = 0, r = n;
    while (q--) {
        int l, r;
        cin >> l >> r;
        // lower_bound -> leftmost x >= l
        // int left_lion = lower_bound(lions, lions+n, l) - lions;

        int lions_smaller_than_l = lower_bound(lions, lions + n, l) - lions;
        // >= l olan ilk elemanın indexi
        // < l olan elemanların sayısı

        int lions_not_exceeding_r = upper_bound(lions, lions + n, r) - lions;
        // > r olan ilk elemanın indexi
        // <= r olan elemanların sayısı

        // l <= ... <= r
        cout << lions_not_exceeding_r - lions_smaller_than_l << "\n";

        // int lo = 0, hi = n;
        // while (lo < hi) {
        //     int mid = (lo + hi) / 2;
        //     if (lions[mid] < l) {
        //         lo = mid + 1;
        //     } else { // lions[mid] >= l
        //         hi = mid;
        //     }
        // }
        // int left_lion = lo;
        // // < l olan aslanların sayısı

        // // lo == lower_bound(lions, lions+n, l) - lions
        // lo = -1, hi = n - 1;
        // // <= r
        // while (lo < hi) {
        //     // Edge case: hi = lo + 1
        //     int mid = (lo + hi) / 2 + 1;
        //     if (lions[mid] <= r) {
        //         // [mid, hi]
        //         // lions[mid+1] > r
        //         lo = mid;
        //     } else { // lions[mid] > r
        //         hi = mid - 1;
        //     }
        // }
        // int right_lion = lo;

        // // Bütün aslanlar < l ise
        // // left_lion = n
        // // right_lion = n-1

        // // Bütün aslanlar > r ise
        // // left_lion = 0
        // // right_lion = -1
        // cout << right_lion - left_lion + 1 << "\n";
    }
}