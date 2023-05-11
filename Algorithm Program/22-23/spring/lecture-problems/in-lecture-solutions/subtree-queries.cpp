#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define FOR(i, n) for (int i = 0; i < (n); i++)
using ll = long long;

const int N = 2e5 + 5;
const int M = 18;
vector<int> g[N];
int timer;
int in[N], out[N];

vector<ll> seg;
#define mid (l + r) / 2

void upd(int cur, int l, int r, int target, int val) {
    if (!(l <= target && target <= r))
        return;
    if (l == r) {
        seg[cur] += val;
        return;
    }
    upd(2 * cur, l, mid, target, val);
    upd(2 * cur + 1, mid + 1, r, target, val);
    seg[cur] = seg[2 * cur] + seg[2 * cur + 1];
}

// [tl, tr] arasının toplamı
ll get(int cur, int l, int r, int tl, int tr) {
    if (l > tr || r < tl)
        return 0;
    if (tl <= l && r <= tr) {
        return seg[cur];
    }
    return get(2 * cur, l, mid, tl, tr) + get(2 * cur + 1, mid + 1, r, tl, tr);
}

void dfs(int cur = 1) {
    in[cur] = timer++;
    for (int nxt : g[cur]) {
        dfs(nxt);
    }
    out[cur] = timer++;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;
    FOR(i, n - 1) {
        int p;
        cin >> p;
        g[p].push_back(i + 2);
    }
    dfs();
    seg.assign(4 * timer, 0);
    while (q--) {
        int t, u;
        cin >> t >> u;
        if (t == 1) {
            int x;
            cin >> x;
            upd(1, 0, timer - 1, in[u], x);
        }
        cout << get(1, 0, timer - 1, in[u], out[u]) << "\n";
    }
}