#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;
vector<int> g[N];
int tin[N], tout[N];
int timer;
vector<ll> seg;
#define mid (l + r) / 2

void add(int c, int l, int r, int t, int v) {
    if (!(l <= t && t <= r))
        return;
    if (l == r) {
        seg[c] += v;
        return;
    }
    add(2 * c, l, mid, t, v);
    add(2 * c + 1, mid + 1, r, t, v);
    seg[c] = seg[2 * c] + seg[2 * c + 1];
}

ll get(int c, int l, int r, int tl, int tr) {
    if (tl > r || tr < l)
        return 0;
    if (tl <= l && r <= tr)
        return seg[c];
    return get(2 * c, l, mid, tl, tr) + get(2 * c + 1, mid + 1, r, tl, tr);
}

void dfs(int c = 1) {
    tin[c] = timer++;
    for (int nxt : g[c]) {
        dfs(nxt);
    }
    tout[c] = timer++;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;
    for (int i = 2; i <= n; i++) {
        int p;
        cin >> p;
        g[p].push_back(i);
    }
    dfs();
    seg.assign(timer * 4, 0);
    while (q--) {
        int t, u;
        cin >> t >> u;
        if (t == 1) {
            int x;
            cin >> x;
            add(1, 0, timer, tin[u], x);
        }
        cout << get(1, 0, timer, tin[u], tout[u]) << "\n";
    }
}