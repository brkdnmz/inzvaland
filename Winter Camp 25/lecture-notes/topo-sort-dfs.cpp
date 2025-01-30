#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

vector<int> g[N];
bool vis[N];
vector<int> topo_sort;

void dfs(int cur) {
    vis[cur] = 1;
    for (int nxt : g[cur]) {
        if (vis[nxt])
            continue;
        dfs(nxt);
    }
    topo_sort.push_back(cur);
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
    }
    for (int i = 1; i <= n; i++) {
        if (vis[i])
            continue;
        dfs(i);
    }
    // 6 3 2 1 5 4
    reverse(topo_sort.begin(), topo_sort.end());
    // 4 5 1 2 3 6
}