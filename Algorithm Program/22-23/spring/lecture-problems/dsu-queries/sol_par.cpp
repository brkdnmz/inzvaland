#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5;
int par[N], sz[N];

int find(int x) {
    return (x == par[x] ? x : par[x] = find(par[x]));
}

void combine(int u, int v) {
    u = find(u), v = find(v);
    if (u == v)
        return;
    if (sz[u] < sz[v])
        swap(u, v);
    par[v] = u;
    sz[u] += sz[v];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    for (int i = 1; i < N; i++)
        par[i] = i, sz[i] = 1;
    int n, q;
    cin >> n >> q;
    while (q--) {
        int t, u;
        cin >> t >> u;
        if (t == 1) {
            int v;
            cin >> v;
            combine(u, v);
        }
        cout << sz[find(u)] << "\n";
    }
}