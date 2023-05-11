#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define FOR(i, n) for (int i = 0; i < (n); i++)
using ll = long long;

const int N = 2e5 + 5;
const int M = 18;
vector<int> g[N];
int par[N][M];

void dfs(int cur = 1) {
    for (int j = 1; j < M; j++) {
        //              par[0][j-1] = 0
        par[cur][j] = par[par[cur][j - 1]][j - 1];
    }
    for (int child : g[cur]) {
        if (child == par[cur][0])
            continue;
        par[child][0] = cur;
        dfs(child);
    }
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
    dfs();
    while (q--) {
        int u, k;
        cin >> u >> k;
        // bitleri soldan sağa gezme
        for (int j = M - 1; j >= 0; j--) {
            int cur_power = 1 << j;
            if (k >= cur_power) {
                k -= cur_power;
                u = par[u][j];
            }
        }

        /* bitleri sağdan sola gezme
            int bit = 0;
            while(k){ // k > 0
                if(k & 1) u = par[u][bit];
                k >>= 1;
                bit++;
            }
        */
        if (!u)
            u = -1;
        cout << u << "\n";
    }
}