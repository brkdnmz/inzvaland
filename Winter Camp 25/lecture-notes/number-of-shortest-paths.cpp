#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;

vector<array<int, 2>> g[N];

int main() {
    int n, m;
    cin >> n >> m;
    int s;
    cin >> s;
    // no need for an iterator or m's value
    // can do this!
    while (m--) {
        int a, b, c;
        cin >> a >> b >> c;
        g[a].push_back({b, c});
        g[b].push_back({a, c});
    }
    vector<ll> dist(n + 1, 1e18);
    vector<int> par[n + 1];
    priority_queue<array<ll, 2>> q;
    // priority_queue<array<ll, 2>, vector<array<ll, 2>>, greater<array<ll, 2>>> q;
    q.push({0, s});
    while (q.size()) {
        auto [d, cur] = q.top();
        // if (d != dist[cur])
        //     continue;
        for (auto &[nxt, w] : g[cur]) {
            if (dist[nxt] > dist[cur] + w) {
                par[nxt] = {(int)cur};
                dist[nxt] = dist[cur] + w;
                q.push({-dist[nxt], nxt});
            } else if (dist[nxt] == dist[cur] + w) {
                par[nxt].push_back(cur);
            }
        }
    }
}