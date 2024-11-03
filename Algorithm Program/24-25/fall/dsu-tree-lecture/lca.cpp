#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5; // Max. number of nodes
const int M = 18;      // Type "log2(2e5)" in browser's search bar, you'll see 17.6...

vector<int> g[N];
int p[N][M];
int level[N]; // Notice root's (1) level won't be set below, hence 0

void dfs(int cur, int par) {
    p[cur][0] = par;
    for (int i = 1; i < M; i++)
        p[cur][i] = p[p[cur][i - 1]][i - 1];

    for (int nxt : g[cur]) {
        if (nxt == par)
            continue;

        level[nxt] = level[cur] + 1;
        dfs(nxt, cur);
    }
}

int kth_ancestor(int u, int k) {
    for (int i = M - 1; i >= 0; i--) {
        if (k >= (1 << i)) {
            k -= 1 << i;
            u = p[u][i];
        }
    }
    return u;
}

int lca(int u, int v) {
    // To make the code clearer
    if (level[u] < level[v])
        swap(u, v);

    u = kth_ancestor(u, level[v] - level[u]);

    // Edge case! Figure out what this case corresponds to.
    if (u == v)
        return u;

    // Jump as long as their ancestors are different.
    // This is the same as finding the k-th ancestor
    // where k is level[u] - level[lca] - 1, but we don't know k itself!
    for (int i = M - 1; i >= 0; i--) {
        if (p[u][i] != p[v][i]) {
            u = p[u][i], v = p[v][i];
        }
    }

    // Figure out why ;)
    return p[u][0];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
    }

    dfs(1, 0);

    // Do what you want
}