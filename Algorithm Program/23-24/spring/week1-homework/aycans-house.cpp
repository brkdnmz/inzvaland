#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    int a[n];
    for (int &x : a)
        cin >> x;

    vector<ll> pre(1, 0);
    for (int i = 0; i < n; i++) {
        pre.push_back(pre.back() + a[i]);
    }

    // pre[r] == pre[l - 1]
    // kaç farklı (l, r) (l != r) var?

    // 0 3 4 3 5 4 1
    sort(pre.begin(), pre.end());
    // 0 1 3 3 3 4 4 4 4 5

    // n = 1
    // 0
    // 0 0

    int cnt = 1; // Bizimle aynı olanların sayısı
    ll ans = 0;  // n * (n+1) / 2'ye kadar gidebilir
    for (int i = 1; i <= n; i++) {
        if (pre[i] == pre[i - 1]) {
            cnt++;
        } else {
            // Önceki cnt ile cevaba katılacak değeri bul
            // Elimizde cnt tane aynı şey var
            // C(cnt, 2)
            ans += (ll)cnt * (cnt - 1) / 2;
            cnt = 1;
        }
    }
    ans += (ll)cnt * (cnt - 1) / 2;
    cout << ans << "\n";
}