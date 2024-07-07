#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int array[n];
    for (auto &x : array)
        cin >> x;

    // f'te neyi döndürürseniz LIS'in I kısmı ona göre değişir:
    //  Longest *Increasing* Subsequence
    //  Longest *Non-decreasing* Subsequence
    //  Longest *Decreasing* Subsequence
    //  Longest *Non-increasing* Subsequence
    auto f = [&](int prev, int cur) {
        return array[prev] < array[cur]; // increasing
        // return array[prev] <= array[cur]; // non-decreasing
        // return array[prev] > array[cur];  // decreasing
        // return array[prev] >= array[cur]; // non-increasing
    };

    // Sıfırla başlatmaya gerek yok aslında, içeride "dp[i] = 1" yapıyoruz zaten.
    int dp[n] = {};

    for (int i = 0; i < n; i++) {
        dp[i] = 1; // Base case
        for (int prev = 0; prev < i; prev++) {
            // Burada f'i kullanarak daha genel bir kod yazmış oluyoruz.
            if (f(prev, i))
                dp[i] = max(dp[i], dp[prev] + 1);
        }
    }

    // dp[i], i'inci elemanın kesin dahil edildiği LIS oluyor.
    // LIS'in hangi elemanda bittiğini bilemeyiz, sonuncuda bitmeyebilir.
    // Bu yüzden max. değeri alıyoruz.
    cout << *max_element(dp, dp + n) << "\n";
}