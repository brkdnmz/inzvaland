#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

vector<int> g[N];
bool vis[N];
int longest_path[N];

void dfs(int cur) {
    for (int nxt : g[cur]) {
        if (vis[nxt])
            continue;
        dfs(nxt);
        longest_path[cur] = max(longest_path[cur], longest_path[nxt] + 1);
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    int in[n + 1] = {};
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
    cout << *max_element(longest_path, longest_path + n + 1) + 1 << "\n";
}