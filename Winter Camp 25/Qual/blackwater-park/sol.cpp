#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;
const int M = 19;

vector<array<int, 2>> g[N];
ll sz[N], l[N], w[N];
ll dist[N];
int par[N][M];
ll dp[N][M];
ll total_w_to_root[N];

void dfs1(int c, int p) {
    sz[c] = 1;
    l[c] = l[p] + 1;

    par[c][0] = p;
    for (int i = 1; i < M; i++) {
        par[c][i] = par[par[c][i - 1]][i - 1];
    }

    total_w_to_root[c] = total_w_to_root[p] + w[c];

    for (auto &[n, w_] : g[c]) {
        if (n == p)
            continue;
        w[n] = w_;
        dfs1(n, c);
        sz[c] += sz[n];
        dist[c] += dist[n] + sz[n] * w[n];
    }
}

void dfs2(int c, int p) {
    dp[c][0] = sz[c] * w[c];
    for (int i = 1; i < M; i++) {
        dp[c][i] = dp[c][i - 1] + dp[par[c][i - 1]][i - 1];
    }
    for (auto &[n, w_] : g[c]) {
        if (n == p)
            continue;
        dfs2(n, c);
    }
}

int lca(int a, int b) {
    if (l[a] < l[b])
        swap(a, b);
    for (int i = M - 1; i >= 0; i--) {
        if (l[par[a][i]] >= l[b])
            a = par[a][i];
    }
    if (a == b)
        return a;
    for (int i = M - 1; i >= 0; i--) {
        if (par[a][i] != par[b][i]) {
            a = par[a][i];
            b = par[b][i];
        }
    }
    return par[a][0];
}

ll total_dist_to(int u) {
    /*
        d[u0]
        d[u1] - (d[u0] + sz[u0] * w0) + (sz[u1] - sz[u0]) * w0 = d[u1] - d[u0] + sz[u1] * w0 - 2*sz[u0]*w0
        d[u2] - (d[u1] + sz[u1] * w1) + (sz[u2] - sz[u1]) * w0..1


        d[u2] + sz[u2] * w0..1 - 2*sz[u1]*w1 - 2*sz[u0]*w0
    */

    return dist[1] + sz[1] * total_w_to_root[u] - 2 * dp[u][M - 1];
}

ll total_dp(int u, int k) {
    ll ans = 0;
    for (int i = 0; i < M; i++) {
        if (k & (1 << i)) {
            ans += dp[u][i];
            u = par[u][i];
        }
    }
    return ans;
}

ll solve(int a, int b) {
    if (l[a] < l[b])
        swap(a, b);
    int c = lca(a, b);
    ll ans = total_dist_to(c) - total_dp(a, l[a] - l[c]);
    if (b != c) {
        ans -= total_dp(b, l[b] - l[c]);
    }
    return ans;
}

ll solve_brute(int a, int b) {
    int c = lca(a, b);
    queue<array<ll, 2>> q;
    vector<bool> vis(N);
    int cur = a;
    for (; cur != c;) {
        q.push({cur, 0});
        cur = par[cur][0];
    }
    cur = b;
    for (; cur != c;) {
        q.push({cur, 0});
        cur = par[cur][0];
    }
    q.push({c, 0});
    ll ans = 0;
    while (!q.empty()) {
        auto [u, d] = q.front();
        q.pop();
        if (vis[u])
            continue;
        vis[u] = 1;
        ans += d;
        for (auto &[n, w_] : g[u]) {
            q.push({n, d + w_});
        }
    }
    return ans;
}

int main(int argc, char **argv) {
    // freopen(argv[1], "r", stdin);
    // freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;
    for (int i = 0; i < n - 1; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        g[a].push_back({b, c});
        g[b].push_back({a, c});
    }
    dfs1(1, 0);
    dfs2(1, 0);
    // for (int i = 1; i <= n; i++) {
    //     cout << i << " " << total_dist_to(i) << endl;
    // }
    while (q--) {
        int a, b;
        cin >> a >> b;
        /*
            dist[u]
            dist[u1] - (dist[u] + sz[u]*w0)
            dist[u2] - (dist[u1] + sz[u1]*w1)
            ...
            = dist[lca] - sum(sz[i]*w[i])
        */
        ll a1 = solve(a, b);
        cout << a1;
        if (q)
            cout << "\n";
        // ll a2 = solve_brute(a, b);
        // assert(a1 == a2);
    }
}