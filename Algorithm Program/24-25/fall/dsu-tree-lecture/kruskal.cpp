#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5; // Max. number of nodes

int p[N];
int sz[N];

int find_with_update(int x) { return x == p[x] ? x : p[x] = find_with_update(p[x]); }

bool union_with_swap(int x, int y) {
    x = find_with_update(x);
    y = find_with_update(y);

    if (x == y)
        return false;

    if (sz[x] < sz[y])
        swap(x, y);

    p[y] = x;
    sz[x] += sz[y];
    return true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 1; i < N; i++)
        p[i] = i, sz[i] = 1;

    int n, m;
    cin >> n >> m;

    // - "Yo wtf is array?"
    // + The good old array you know, just wrapped inside a struct so that you can use it inside other containers
    vector<array<int, 3>> edges;

    while (m--) {
        int u, v, w;
        cin >> u >> v >> w;

        // Make weight the first element so that default sorting does what we want
        edges.push_back({w, u, v});
    }

    // Will sort by w's first
    sort(edges.begin(), edges.end());

    int cost = 0;

    // Google "structured binding C++"
    for (auto &[w, u, v] : edges) {
        if (union_with_swap(u, v)) {
            cost += w;
        }
    }

    cout << cost << "\n";
}