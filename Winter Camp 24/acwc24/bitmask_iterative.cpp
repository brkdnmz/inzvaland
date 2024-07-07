#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Soru:
// https://algoleague.com/problem/curb-your-greed/detail

int main() {
    int n;
    cin >> n;
    int grid[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }
    int M = 1 << n;
    ll dp[M] = {};

    // n * 2^n
    // Bir n çarpanı daha yok aslında, 25. satırdan dolayı.
    for (int row = 0; row < n; row++) {
        for (int old_mask = 0; old_mask < M; old_mask++) {
            // int ones = 0;
            // for (int j = 0; j < n; j++)
            //     ones += (old_mask & (1 << j)) > 0;
            int row_index = __builtin_popcount(old_mask); // veya `ones`
            if (row_index != row) {
                continue;
            }
            for (int j = 0; j < n; j++) {
                // Bu sütundan bir cell seçilmiş
                if (old_mask & (1 << j))
                    continue;
                int new_mask = old_mask | (1 << j);
                dp[new_mask] = max(dp[new_mask], dp[old_mask] + grid[row_index][j]);
            }
        }
    }

    // Aşağıdaki yöntem maskeleri bir bir geziyor, bulunduğu satır değişken oluyor.
    // old_mask'in tüm transition'larının (alt maskelerden DP güncellemesi)
    // handle edilmiş olması gerekiyor ve gerçekten de oluyor.
    // Dikkat edin ki herhangi bir alt maske zaten old_mask'ten küçük olmalı.
    // Derste bu yöntemin yanlış olabileceğini söylemiştim.
    // old_mask = 3 iken dp[old_mask]'in hesaplanmamış olabileceğini söylemiştim
    // ama hesaplanıyor aslında (1 -> 3 ve 2 -> 3).

    // Bu yöntem, üsttekinden daha hızlı.
    for (int old_mask = 0; old_mask < M; old_mask++) {
        // int ones = 0;
        // for (int j = 0; j < n; j++)
        //     ones += (old_mask & (1 << j)) >= 0;
        for (int j = 0; j < n; j++) {
            // Bu sütundan bir cell seçilmiş
            if (old_mask & (1 << j))
                continue;
            int new_mask = old_mask | (1 << j);
            int row_index = __builtin_popcount(old_mask); // veya `ones`
            dp[new_mask] = max(dp[new_mask], dp[old_mask] + grid[row_index][j]);
        }
    }
    cout << dp[M - 1] << "\n";
}