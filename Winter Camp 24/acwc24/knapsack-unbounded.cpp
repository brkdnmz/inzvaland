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

    vector<int> dp(W + 1);
    for (int i = 0; i < n; i++) {
        // Tek yol (başka varsa bilmiyorum :D)
        // Aynı vektörün üstünde düz gezme
        for (int old_w = 0; old_w + weight[i] <= W; old_w++) {
            int new_w = old_w + weight[i];
            dp[new_w] = max(dp[new_w], dp[old_w] + profit[i]);
        }
    }
    cout << dp[W] << "\n";
    // Veya
    // cout << dp.back() << "\n";
    // Veya
    // cout << *max_element(dp.begin(), dp.end()) << "\n";
}