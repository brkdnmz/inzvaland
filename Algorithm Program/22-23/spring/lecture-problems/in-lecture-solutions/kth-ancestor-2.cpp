#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define FOR(i, n) for (int i = 0; i < (n); i++)
using ll = long long;

const int N = 2e5 + 5;
vector<int> g[N];
vector<int> ancestors;
vector<array<int, 2>> queries[N];
int ans[N]; // ans[i] = i'inci query'nin cevabı

void dfs(int cur = 1, int par = 0) {
    ancestors.push_back(cur);
    for (auto [qid, k] : queries[cur]) {
        if (ancestors.size() <= k)
            ans[qid] = -1;
        else {
            // ancestors[ancestors.size() - k]
            ans[qid] = ancestors.end()[-(k + 1)];
        }
    }
    for (int child : g[cur]) {
        if (child == par)
            continue;
        dfs(child, cur);
    }
    ancestors.pop_back();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;
    FOR(i, n - 1) {
        int a, b;
        cin >> a >> b;
        g[a].pb(b);
        g[b].pb(a);
    }
    FOR(i, q) {
        int u, k;
        cin >> u >> k;
        queries[u].pb({i, k});
    }
    dfs();
    FOR(i, q)
    cout << ans[i] << "\n";
}