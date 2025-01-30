#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5;

vector<int> g[N];
int c[N];
bool vis[N];
int longest_path[N];

void dfs(int cur) {
    vis[cur] = 1;
    for (int nxt : g[cur]) {
        if (!vis[nxt])
            dfs(nxt);
        longest_path[cur] = max(longest_path[cur], longest_path[nxt] + 1);
    }
}

int main() {
    int n, m, s;
    cin >> n >> m >> s;
    for (int i = 1; i <= n; i++) {
        cin >> c[i];
    }
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        if (c[a] > c[b])
            g[a].push_back(b);
        else
            g[b].push_back(a);
    }
    dfs(s);
    cout << longest_path[s] << "\n";
}