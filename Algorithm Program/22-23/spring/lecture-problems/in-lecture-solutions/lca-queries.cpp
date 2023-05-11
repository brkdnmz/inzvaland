#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define FOR(i, n) for (int i = 0; i < (n); i++)
using ll = long long;

const int N = 2e5 + 5;
const int M = 18;
vector<int> g[N];
int level[N];
int par[N][M];

void dfs(int cur = 1) {
    level[cur] = level[par[cur][0]] + 1;
    for (int j = 1; j < M; j++) {
        par[cur][j] = par[par[cur][j - 1]][j - 1];
    }
    for (int child : g[cur]) {
        if (child == par[cur][0])
            continue;
        par[child][0] = cur;
        dfs(child);
    }
}

int lca(int u, int v) {
    if (level[u] < level[v])
        swap(u, v);

    // level[u] - level[v]'inci parent'a git, binary lifting'le

    /*
        int level_diff = level[u] - level[v];

        for (int j = M - 1; j >= 0; j--) {
            int cur_power = 1 << j;
            if (level_diff >= cur_power) {
                level_diff -= cur_power;
                u = par[u][j];
            }
        }
    */

    for (int j = M - 1; j >= 0; j--) {
        if (level[par[u][j]] >= level[v])
            u = par[u][j];
    }

    // don't forget
    if (u == v)
        return u;

    for (int j = M - 1; j >= 0; j--) {
        if (par[u][j] != par[v][j]) {
            u = par[u][j];
            v = par[v][j];
        }
    }
    return par[u][0]; // veya par[v][0]
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;
    FOR(i, n - 1) {
        int a, b;
        cin >> a >> b;
        g[a].pb(b);
        g[b].pb(a);
    }
    dfs();
    while (q--) {
        int u, v;
        cin >> u >> v;
        int l = lca(u, v);
        cout << l << " " << level[u] + level[v] - 2 * level[l] << "\n";
    }
}