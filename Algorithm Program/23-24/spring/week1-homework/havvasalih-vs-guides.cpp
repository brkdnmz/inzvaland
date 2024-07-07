#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// scientific notation
const int N = 2e5 + 5;
int cnt[N];
int is_valid[N];
int total_valid[N];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k, q;
    cin >> n >> k >> q;
    while (n--) {
        int x, y;
        cin >> x >> y;
        // [x, y] aralığını 1 artır
        // for (int i = x; i <= y; i++) {
        //     cnt[i]++;
        // }
        cnt[x]++;
        cnt[y + 1]--;
    }
    // 0 2 1 0 1
    for (int i = 1; i < N; i++) {
        // i'de cnt[i] tane aralık başlıyor
        cnt[i] += cnt[i - 1];
    }
    for (int i = 1; i < N; i++) {
        is_valid[i] = cnt[i] >= k;
        total_valid[i] = is_valid[i] + total_valid[i - 1];
    }
    while (q--) {
        int l, r;
        cin >> l >> r;
        // [l, r] aralığında valid olanların sayısı
        int ans = total_valid[r] - total_valid[l - 1];
        cout << ans << "\n";
    }
}