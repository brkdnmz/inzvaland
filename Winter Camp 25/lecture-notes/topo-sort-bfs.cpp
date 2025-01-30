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
    vector<int> topo_sort;
    while (q.size()) {
        int cur = q.front();
        topo_sort.push_back(cur);
        q.pop();
        for (int nxt : g[cur]) {
            // Start discovering when all predecessors are visited
            if (!--in[nxt]) {
                q.push(nxt);
            }
        }
    }

    // Think what would be the case when there is a cycle
    // Would the in degree of any node in the cycle reach zero?
    // Figure out how to determine the existence of a cycle!
}