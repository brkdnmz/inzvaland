#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;

vector<array<int, 2>> g[N];

int main() {
    int n, m;
    cin >> n >> m;
    int s;
    cin >> s;
    vector<vector<ll>> dist(n + 1, vector<ll>(n + 1, 1e18));
    while (m--) {
        ll a, b, c;
        cin >> a >> b >> c;
        dist[a][b] = min(dist[a][b], c);
    }
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
}