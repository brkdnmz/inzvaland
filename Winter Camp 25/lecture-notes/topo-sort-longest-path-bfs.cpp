#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

vector<int> g[N];

int main() {
    int n, m;
    cin >> n >> m;
    int in[n + 1] = {};
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        in[b]++;
    }
    queue<int> q;
    for (int i = 1; i <= n; i++) {
        // root node
        if (!in[i]) {
            q.push(i);
        }
    }
    vector<int> longest_path(n + 1, 1);
    // int ans = 1;
    while (q.size()) {
        int cur = q.front();
        // ans = max(ans, longest_path[cur]);
        q.pop();
        for (int nxt : g[cur]) {
            longest_path[nxt] = max(longest_path[nxt], longest_path[cur] + 1);
            // üstteki tüm node'lar bittiğinde keşfetmeye başla
            if (!--in[nxt]) {
                q.push(nxt);
            }
        }
    }
    int ans = *max_element(longest_path.begin(), longest_path.end());
}