#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5;

vector<int> g[N];
int c[N];
int in[N];
bool vis[N];

// Not gonna lie, I like this one better than BFS
void dfs(int cur) {
    // This check could be here also,
    // instead of inside the for loop below
    if (vis[cur])
        return;

    vis[cur] = 1;
    for (int nxt : g[cur]) {
        in[nxt]++;
        dfs(nxt);
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

    // Path length = # edges
    int longest_path[n + 1] = {};

    queue<int> q;
    q.push(s);
    while (q.size()) {
        int cur = q.front();
        q.pop();
        for (int nxt : g[cur]) {
            in[nxt]--;
            longest_path[nxt] = max(longest_path[nxt], longest_path[cur] + 1);
            if (in[nxt] == 0)
                q.push(nxt);
        }
    }

    // Unlike the DFS version, there may be multiple sink (i.e. last) nodes
    // Gotta check 'em all!
    cout << *max_element(longest_path, longest_path + n + 1) << "\n";
}