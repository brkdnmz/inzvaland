#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int K = 64;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;
    int p[n];
    for (int &x : p)
        cin >> x;
    int next[n][K];
    for (int i = 0; i < n; i++)
        next[i][0] = p[i] - 1;
    for (int j = 1; j < K; j++) {
        for (int i = 0; i < n; i++)
            next[i][j] = next[next[i][j - 1]][j - 1];
    }
    while (q--) {
        int x;
        ll k;
        cin >> x >> k;
        x--;
        int j = 0;
        while (k) {
            if (k & 1)
                x = next[x][j];
            k >>= 1;
            j++;
        }
        cout << p[x] << "\n";
    }
}