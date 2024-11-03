#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5; // Max. number of nodes

vector<int> g[N];
int timer;
int in[N], out[N];

void dfs(int cur, int par) {
    in[cur] = timer++;

    for (int nxt : g[cur]) {
        if (nxt == par)
            continue;

        dfs(nxt, cur);
    }

    out[cur] = timer;
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

    // Now, in[u] and out[u] represent the two endpoints of the subarray that represents u's entire subtree.
    // Think about what in[u] itself represents based on the `dfs` implementation.
    // You can use them to maintain a segment tree/lazy segment tree that supports node/subtree update and node/subtree
    // sum.
}