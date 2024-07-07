#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Soru:
// https://algoleague.com/problem/curb-your-greed/detail

const int N = 20;
const int M = 1 << N;

// Recursive fonksiyon bunlara kolayca erişebilsin diye global tanımladım.
int n;
int grid[N][N];

// Hesaplanmamış değer için -1 kullanıyoruz.
// Negatif değerler de olabilseydi -1e18 falan tercih edebilirdik
// veya ekstra bir is_calculated boolean array kullanabilirdik.
vector<ll> dp(1 << N, -1);

// Aslında row_number == __builtin_popcount(taken_cols_mask)
// Ama recursive fonksiyon kolaylığından yararlanarak
// bu şekilde parametre olarak da yazabiliriz.
ll solve(int taken_cols_mask, int row_number) {
    // Kod yazımını kolaylaştırmak için güzel bir yöntem.
    ll &ans = dp[taken_cols_mask];

    // Hesaplanmışsa direkt döndürüyoruz (memoization).
    if (ans != -1)
        return ans;

    // Önceki call'da son satıra ulaşmışız bile.
    if (row_number == n) {
        return 0;
    }

    for (int col = 0; col < n; col++) {
        // Seçilmiş bir sütunu tekrar seçemeyiz.
        if (taken_cols_mask >> col & 1)
            continue;

        // (row_number, col)'daki sayıyı seçip bir sonraki satıra gidiyoruz.
        ans = max(ans, grid[row_number][col] + solve(taken_cols_mask | (1 << col), row_number + 1));
    }

    return ans;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }
    cout << solve(0, 0) << "\n";
}