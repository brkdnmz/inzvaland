#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n, m;
    cin >> n >> m;
    int grid[n + 1][m + 1] = {};
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            int x;
            cin >> x;
            grid[i][j] = max(grid[i][j - 1], grid[i - 1][j]) + x;
        }
    }
    cout << grid[n][m] << "\n";
}