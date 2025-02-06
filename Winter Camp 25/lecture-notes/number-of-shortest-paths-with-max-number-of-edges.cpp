#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;

vector<array<int, 2>> g[N];

int main() {
    int n, m, s, t;
    cin >> n >> m >> s >> t;
    while (m--) {
        int a, b, c;
        cin >> a >> b >> c;
        g[a].push_back({b, c});
        g[b].push_back({a, c});
    }
    vector<ll> dist(n + 1, 1e18);
    vector<int> par[n + 1];
    priority_queue<array<ll, 2>> pq;
    pq.push({0, s});
    int max_edges[n + 1] = {};
    int n_paths[n + 1] = {};
    while (pq.size()) {
        auto [d, cur] = pq.top();
        // if (d != dist[cur])
        //     continue;
        for (auto &[nxt, w] : g[cur]) {
            if (dist[nxt] > dist[cur] + w) {
                dist[nxt] = dist[cur] + w;
                max_edges[nxt] = max_edges[cur] + 1;
                n_paths[nxt] = n_paths[cur];
                pq.push({-dist[nxt], nxt});
            } else if (dist[nxt] == dist[cur] + w) {
            }
        }
    }

    // THIS IS RIGHT
    // int in[n + 1] = {};
    // queue<int> q;
    // q.push(t);
    // while (q.size()) {
    //     int cur = q.front();
    //     q.pop();
    //     if (in[cur])
    //         continue;
    //     for (int nxt : par[cur]) {
    //         if (!in[nxt]++)
    //             q.push(nxt);
    //     }
    // }

    // THIS IS WRONG
    // for (int i = 1; i <= n; i++) {
    //     for (int parent : par[i])
    //         in[parent]++;
    // }

    // queue<int> q;
    // q.push(t);
    // while (q.size()) {
    //     int cur = q.front();
    //     q.pop();
    //     for (int parent : par[cur]) {
    //         // number of (shortest) paths with max number of edges
    //         if (max_edges[parent] < max_edges[cur] + 1) {
    //             max_edges[parent] = max_edges[cur] + 1;
    //             n_paths[parent] = n_paths[cur];
    //         } else if (max_edges[parent] == max_edges[cur] + 1) {
    //             n_paths[parent] += n_paths[cur];
    //         }
    //         in[parent]--;
    //         if (in[parent] == 0) {
    //             q.push(parent);
    //         }
    //     }
    // }
    // int ans = n_paths[s]; // number of (shortest) paths with max number of edges
}