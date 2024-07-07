#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, W;
    cin >> n >> W;
    int weight[n], profit[n];
    for (auto &x : weight)
        cin >> x;
    for (auto &x : profit)
        cin >> x;

    // dp[i] = Toplam ağırlık tam "i" olunca max. değer
    // Derste "en fazla i" dedim ama tam olması lazım. :D
    vector<int> dp(W + 1);
    for (int i = 0; i < n; i++) {
        // 1. yol: Kopya DP vektörü
        // vector<int> ndp = dp;
        // for (int old_w = 0; old_w + weight[i] <= W; old_w++) {
        //     int new_w = old_w + weight[i];
        //     ndp[new_w] = max(ndp[new_w], dp[old_w] + profit[i]);
        // }

        // 2. yol: Tersten gezme (en iyisi)
        for (int old_w = W - weight[i]; old_w >= 0; old_w--) {
            int new_w = old_w + weight[i];
            dp[new_w] = max(dp[new_w], dp[old_w] + profit[i]);
        }

        // Yanlış yol: Klonsuz
        // Unbounded versiyonunu çözüyor bu (her eşyadan istediğimiz kadar koyma).
        // for (int old_w = 0; old_w + weight[i] <= W; old_w++) {
        //     int new_w = old_w + weight[i];
        //     dp[new_w] = max(dp[new_w], dp[old_w] + profit[i]);
        // }
    }

    // Çantayı tam dolduramayabiliriz! (Son sıfır olmayan değer de alınabilir.)
    cout << *max_element(dp.begin(), dp.end()) << "\n";
}