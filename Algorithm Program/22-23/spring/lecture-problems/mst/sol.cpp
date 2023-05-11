#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;
int par[N], sz[N];

int find(int x) {
    return (x == par[x] ? x : par[x] = find(par[x]));
}

bool combine(int u, int v) {
    u = find(u), v = find(v);
    if (u == v)
        return false;
    if (sz[u] < sz[v])
        swap(u, v);
    par[v] = u;
    sz[u] += sz[v];
    return true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    for (int i = 1; i < N; i++)
        par[i] = i, sz[i] = 1;
    int n, m;
    cin >> n >> m;
    array<int, 3> edges[m];
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges[i] = {w, u, v};
    }
    sort(edges, edges + m);
    ll mst_weight = 0;
    int n_comps = n;
    for (auto &[w, u, v] : edges) {
        bool different = combine(u, v);
        if (different) {
            n_comps--;
            mst_weight += w;
        }
    }
    if (n_comps > 1)
        mst_weight = -1;
    cout << mst_weight << "\n";
}