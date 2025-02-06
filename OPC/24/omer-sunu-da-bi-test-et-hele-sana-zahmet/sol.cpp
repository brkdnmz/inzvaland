#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(int argc, char **argv) {
    // freopen(argv[1], "r", stdin);
    // freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    assert(n * m <= 1e8);

    ll parallel = 0, non_parallel = 0;
    ll non_parallel_squares = 0;

    for (int top = 1; top <= m; top++) {
        for (int left = top; left <= n; left += top)
            parallel++;
    }

    for (int left = 1; left <= n; left++) {
        // parallel
        for (int top = 2 * left; top <= m; top += left) {
            parallel++;
        }

        // non-parallel
        for (int top = 1; top <= m; top++) {
            non_parallel_squares += left + top <= min(n, m);
            // left + k * top <= n
            // top + k * left <= m
            non_parallel += min((n - left) / top, (m - top) / left);
        }
    }

    cout << parallel + 2 * non_parallel - non_parallel_squares;
}