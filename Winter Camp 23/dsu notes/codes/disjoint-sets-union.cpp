#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

int set_of[N];

vector<int> g_set[N];

void union_sets(int u, int v) {
    if (set_of[u] == set_of[v]) {
        return;
    }
    if (g_set[set_of[u]].size() > g_set[set_of[v]].size()) {
        swap(u, v);
    }
    // u'nun setini v'ye ekle, u'nunkini temizle
    int set_of_u = set_of[u];

    // for(int i = 0; i < g_set[set_of_u].size(); i++){
    //     int node = g_set[set_of_u][i];
    //     //...
    // }
    for (int node : g_set[set_of_u]) {
        g_set[set_of[v]].push_back(node);
        set_of[node] = set_of[v];
    }
    g_set[set_of_u].clear();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 1; i < N; i++) {
        set_of[i] = i;
        g_set[i] = {i};
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
            cout << (set_of[u] == set_of[v] ? "YES" : "NO") << "\n";
        }
    }
}