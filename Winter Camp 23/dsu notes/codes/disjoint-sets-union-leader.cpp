#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

int leader[N];
int sz[N];

int find_leader(int u) { // atabul
    if (u == leader[u])
        return u;
    // return leader[u] = find_leader(leader[u]);
    leader[u] = find_leader(leader[u]);
    return leader[u];
}

void union_sets(int u, int v) {
    if (sz[u] > sz[v]) {
        swap(u, v);
    }
    int l_u = find_leader(u);
    int l_v = find_leader(v);
    if (l_u == l_v)
        return;
    leader[l_u] = leader[l_v];
    sz[v] += sz[u];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 1; i < N; i++) {
        leader[i] = i;
        sz[i] = 1;
    }

    int n, m;
    cin >> n >> m;

    while (m--) {
        string operation;
        int u, v;
        cin >> operation >> u >> v;
        if (operation == "union") {
            union_sets(u, v);
        } else { // "get"
            cout << (find_leader(u) == find_leader(v) ? "YES" : "NO") << "\n";
        }
    }
}