#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5;

vector<int> g[N];
int c[N];

int main() {
    /*
        Alright, I agree with you
        DFS one is cooler
    */
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

    // Here, we precalculate the in degrees for each node where only s is the root node
    // We don't care about the whole graph since Mario starts at s
    int in[n + 1] = {};
    bool vis[n + 1] = {};
    queue<int> q;
    q.push(s);
    while (q.size()) {
        int cur = q.front();
        q.pop();
        if (vis[cur])
            continue;
        vis[cur] = 1;
        for (int nxt : g[cur]) {
            in[nxt]++;
            if (!vis[nxt])
                q.push(nxt);
        }
    }

    // Path length = # edges
    int longest_path[n + 1] = {};

    // We can use the same queue:)
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