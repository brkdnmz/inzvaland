#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 1e6 + 5;

int n;
int lmost[N], rmost[N];

int f_lmost(int x) { return x == lmost[x] ? x : lmost[x] = f_lmost(lmost[x]); }
int f_rmost(int x) { return x == rmost[x] ? x : rmost[x] = f_rmost(rmost[x]); }

void comb(int l, int r) {
    l = f_lmost(l), r = f_lmost(r);
    lmost[r] = l;
    l = f_rmost(l), r = f_rmost(r);
    rmost[l] = r;
}

struct node {
    int cnt;
    ll sum;
    node merge(const node &o) const { return node{cnt + o.cnt, sum + o.sum}; }
};

node seg[4 * N];

#define mid (l + r) / 2
void upd(int c, int l, int r, int t, int v) {
    if (l == r) {
        seg[c].cnt = 1;
        seg[c].sum = v;
        return;
    }

    t <= mid ? upd(2 * c, l, mid, t, v) : upd(2 * c + 1, mid + 1, r, t, v);
    seg[c] = seg[2 * c].merge(seg[2 * c + 1]);
}
node get(int c, int l, int r, int tl, int tr) {
    if (l > tr || tl > r)
        return {0, 0};

    if (tl <= l && r <= tr)
        return seg[c];

    return get(2 * c, l, mid, tl, tr).merge(get(2 * c + 1, mid + 1, r, tl, tr));
}

array<int, 2> get_actual_bounds(int l, int r) { return {f_lmost(max(0, l - 1)), f_rmost(min(n - 1, r + 1))}; }

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    array<int, 2> h[n];
    for (int i = 0; i < n; i++) {
        cin >> h[i][0];
        h[i][1] = i;
        rmost[i] = lmost[i] = i;
    }

    int rmost_decreasing[n], lmost_decreasing[n];
    for (int i = 0; i < n; i++) {
        lmost_decreasing[i] = i;
        if (i && h[i][0] >= h[i - 1][0])
            lmost_decreasing[i] = lmost_decreasing[i - 1];
    }
    for (int i = n - 1; i >= 0; i--) {
        rmost_decreasing[i] = i;
        if (i + 1 < n && h[i][0] >= h[i + 1][0])
            rmost_decreasing[i] = rmost_decreasing[i + 1];
    }

    sort(h, h + n);

    int o;
    cin >> o;
    array<int, 4> qs[o];

    int q_i = 0;
    for (auto &[m, l, r, i] : qs)
        cin >> l >> r >> m, i = q_i++;

    sort(qs, qs + o);

    int h_ptr = 0;
    bool vis[n] = {};
    ll ans[o];
    for (auto [m, l, r, i] : qs) {
        while (h_ptr < n && h[h_ptr][0] <= m) {
            auto [height, pos] = h[h_ptr];
            upd(1, 0, N - 1, pos, height);
            vis[pos] = 1;
            if (pos && vis[pos - 1])
                comb(pos - 1, pos);
            if (pos + 1 < n && vis[pos + 1])
                comb(pos, pos + 1);
            h_ptr++;
        }
        l--, r--;
        l = lmost_decreasing[l], r = rmost_decreasing[r];
        auto [nl, nr] = get_actual_bounds(l, r);
        l = nl, r = nr;
        auto node = get(1, 0, N - 1, l, r);
        ans[i] = (ll)node.cnt * m - node.sum;
    }
    for (int i = 0; i < o; i++) {
        cout << ans[i];
        if (i + 1 < o)
            cout << "\n";
    }
}