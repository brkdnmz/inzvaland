#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<ll> dp0;
vector<ll> dp1;

// vector<ll> dp[2];

void dfs(vector<pair<vector<int>, ll>> &adjlist, int node, int parent) {
    if (adjlist[node].first.size() == 1) {
        dp0[node] = 0;
        dp1[node] = adjlist[node].second;
    }

    for (int next : adjlist[node].first) {
        if (next == parent) {
            continue;
        }
        dfs(adjlist, next, node);
        dp0[node] += max(dp0[next], dp1[next]);
        dp1[node] += dp0[next];
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;

    vector<pair<vector<int>, ll>> adjlist(n + 1);
    for (int i = 0; i < n - 1; i++) {
        ll a, b;
        cin >> a >> b;
        adjlist[a].first.push_back(b);
        adjlist[b].first.push_back(a);
    }
    for (int i = 1; i <= n; i++) {
        cin >> adjlist[i].second;
    }

    dp0.resize(n + 1);
    dp1.resize(n + 1);

    for (int i = 1; i <= n; i++) {
        dp1[i] = adjlist[i].second;
    }

    dfs(adjlist, 1, 0);

    cout << max(dp0[1], dp1[1]);

    return 0;
}