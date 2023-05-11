#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;
const int K = 18;
int par[N][K];
int h[N];
vector<int> g[N];

void dfs(int c = 1, int p = 0) {
    h[c] = h[p] + 1; // Don't let h[0] = h[1] = 0!
    par[c][0] = p;
    for (int j = 1; j < K; j++)
        par[c][j] = par[par[c][j - 1]][j - 1];
    for (int nxt : g[c]) {
        if (nxt == p)
            continue;
        dfs(nxt, c);
    }
}

int lca(int u, int v) {
    if (h[u] < h[v])
        swap(u, v);
    for (int j = K - 1; j >= 0; j--)
        if (h[par[u][j]] >= h[v])
            u = par[u][j];

    if (u == v)
        return u;

    for (int j = K - 1; j >= 0; j--)
        if (par[u][j] != par[v][j])
            u = par[u][j], v = par[v][j];

    return par[u][0];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    dfs();
    while (q--) {
        int u, v;
        cin >> u >> v;
        int l = lca(u, v);
        cout << l << " " << h[u] + h[v] - 2 * h[l] << "\n";
    }
}