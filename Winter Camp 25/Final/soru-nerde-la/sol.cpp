#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int mod = 1e9 + 7;

int main(int argc, char **argv) {
    // freopen(argv[1], "r", stdin);
    // freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m, q;
    cin >> n >> m >> q;
    vector<array<int, 2>> g[n + 1];
    while (m--) {
        int a, b, c;
        cin >> a >> b >> c;
        g[a].push_back({b, c});
        g[b].push_back({a, c});
    }

    auto dijkstra = [&](int src) -> array<vector<ll>, 2> {
        vector<ll> dist(n + 1, 1e18);
        dist[src] = 0;
        vector<ll> dp(n + 1);
        dp[src] = 1;
        priority_queue<array<ll, 2>> q;
        q.push({0, src});
        while (!q.empty()) {
            auto [d, u] = q.top();
            q.pop();
            if (-d > dist[u]) {
                continue;
            }
            for (auto [v, w] : g[u]) {
                if (dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                    dp[v] = dp[u];
                    q.push({-dist[v], v});
                } else if (dist[v] == dist[u] + w) {
                    (dp[v] += dp[u]) %= mod;
                }
            }
        }
        return {dist, dp};
    };

    auto [dist1, dp1] = dijkstra(1);
    auto [distn, dpn] = dijkstra(n);

    while (q--) {
        ll u, v, w;
        cin >> u >> v >> w;
        if (dist1[u] + distn[v] > dist1[v] + distn[u]) {
            swap(u, v);
        }
        ll new_shortest_paths = dp1[u] * dpn[v] % mod;
        ll actual_shortest = dist1[n];
        ll ans = dp1[n];
        if (actual_shortest == dist1[u] + distn[v] + w) {
            (ans += new_shortest_paths) %= mod;
        } else if (actual_shortest > dist1[u] + distn[v] + w) {
            ans = new_shortest_paths;
        }
        cout << ans;
        if (q)
            cout << "\n";
    }
}