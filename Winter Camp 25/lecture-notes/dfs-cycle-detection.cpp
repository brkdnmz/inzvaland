#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

vector<int> g[N];
bool vis[N];

// Information about the nodes in the DFS stack
bool in_stack[N];
vector<int> stk; // can't use "stack" as a name

void dfs(int cur) {
    vis[cur] = 1;
    in_stack[cur] = 1;
    stk.push_back(cur);
    for (int nxt : g[cur]) {
        if (in_stack[nxt]) {
            // Well, there is a cycle...
            // Can do something here
            return;
        }
        if (vis[nxt])
            continue;
        dfs(nxt);
    }
    in_stack[cur] = 0;
    stk.pop_back();
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
}