#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define mid (l + r) / 2
class SegTree {
    int n;
    struct Node {
        int last;
        ll sum;
        int lazy;
    };
    vector<Node> seg;

    void merge(int c) {
        seg[c].last = seg[2 * c + 1].last;
        seg[c].sum = seg[2 * c].sum + seg[2 * c + 1].sum;
    }
    void prop(int c, int l, int r) {
        if (!seg[c].lazy)
            return;
        seg[c].last = seg[c].lazy;
        seg[c].sum = (ll)(r - l + 1) * seg[c].lazy;
        if (l != r) {
            seg[2 * c].lazy = seg[2 * c + 1].lazy = seg[c].lazy;
        }
        seg[c].lazy = 0;
    }

  public:
    SegTree(vector<int> &init) : n(init.size()), seg(4 * n) { build(init); }
    void build(vector<int> &init) { build(1, 0, n - 1, init); }
    void upd(int tl, int tr, int val) { upd(1, 0, n - 1, tl, tr, val); }
    ll get(int tl, int tr) { return get(1, 0, n - 1, tl, tr); }
    int get_first_larger_or_equal(int tl, int tr, int threshold) {
        return get_first_larger_or_equal(1, 0, n - 1, tl, tr, threshold);
    }

  private:
    void build(int c, int l, int r, vector<int> &init) {
        if (l == r) {
            seg[c].last = seg[c].sum = init[l];
            return;
        }
        build(2 * c, l, mid, init);
        build(2 * c + 1, mid + 1, r, init);
        merge(c);
    }
    void upd(int c, int l, int r, int tl, int tr, int val) {
        prop(c, l, r);
        if (l > tr || tl > r)
            return;
        if (tl <= l && r <= tr) {
            seg[c].lazy = val;
            prop(c, l, r);
            return;
        }
        upd(2 * c, l, mid, tl, tr, val);
        upd(2 * c + 1, mid + 1, r, tl, tr, val);
        merge(c);
    }
    ll get(int c, int l, int r, int tl, int tr) {
        prop(c, l, r);
        if (l > tr || tl > r)
            return 0;
        if (tl <= l && r <= tr) {
            return seg[c].sum;
        }
        return get(2 * c, l, mid, tl, tr) + get(2 * c + 1, mid + 1, r, tl, tr);
    }
    int get_first_larger_or_equal(int c, int l, int r, int tl, int tr, int threshold) {
        prop(c, l, r);
        if (l > tr || tl > r || seg[c].last < threshold)
            return tr + 1;
        if (tl <= l && r <= tr) {
            if (l == r)
                return l;
            int left_ans = get_first_larger_or_equal(2 * c, l, mid, tl, tr, threshold);
            if (left_ans < tr + 1)
                return left_ans;
            return get_first_larger_or_equal(2 * c + 1, mid + 1, r, tl, tr, threshold);
        }
        return min(get_first_larger_or_equal(2 * c, l, mid, tl, tr, threshold),
                   get_first_larger_or_equal(2 * c + 1, mid + 1, r, tl, tr, threshold));
    }
};

vector<int> get_first_ok(string s, string tar) {
    int cnt_req[26] = {};
    for (char c : tar)
        cnt_req[c]++;
    int n = s.size(); // All except $
    vector<int> first_ok(n);
    int cnt_unseen = tar.size();
    int r = n - 1;
    for (int i = n - 1; i >= 0; i--) {
        cnt_unseen -= cnt_req[s[i]]-- > 0;
        while (!(cnt_unseen + !cnt_req[s[r]])) {
            cnt_req[s[r--]]++;
        }
        first_ok[i] = r;
    }
    return first_ok;
}

ll calc(SegTree &seg, int l, int r) {
    auto gauss = [](ll x) { return x * (x + 1) / 2; };
    ll ans = seg.get(l, r);
    ans -= gauss(r) - gauss(l - 1) - (r - l + 1);
    return ans;
}

ll calc_brute(vector<int> &first_ok, int l, int r) {
    ll ans = 0;
    for (int i = l; i <= r; i++) {
        ans += first_ok[i] - i + 1;
    }
    return ans;
}

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    string tar = "inzvaolsundagerisiboskalp";
    for (char &c : s)
        c -= 'a';
    int n_occ[26] = {};
    for (char &c : tar)
        c -= 'a', n_occ[c]++;
    int n = s.size();
    vector<int> prev_pos_of_ch(26, -1), next_pos_of_ch(26, n);
    vector<int> prev_pos_of(n), next_pos_of(n);
    for (int i = 0; i < n; i++) {
        prev_pos_of[i] = prev_pos_of_ch[s[i]];
        prev_pos_of_ch[s[i]] = i;
    }
    for (int i = n - 1; i >= 0; i--) {
        next_pos_of[i] = next_pos_of_ch[s[i]];
        next_pos_of_ch[s[i]] = i;
    }

    auto first_ok = get_first_ok(s, tar);
    SegTree seg(first_ok);

    auto change_pos = [&](int changed_pos) {
        int occ = n_occ[s[changed_pos]];

        if (!occ)
            return;

        int cnt = 1;
        int cur_pos = changed_pos;
        for (; prev_pos_of[cur_pos] > -1 && cnt < occ;) {
            cnt++;
            cur_pos = prev_pos_of[cur_pos];
        }
        int lmost = cur_pos;

        cur_pos = changed_pos;
        for (; next_pos_of[cur_pos] < n && cnt < occ;) {
            cnt++;
            cur_pos = next_pos_of[cur_pos];
        }
        int rmost = cur_pos;
        for (; lmost <= changed_pos && rmost < n; lmost = next_pos_of[lmost], rmost = next_pos_of[rmost]) {
            int prev_pos = prev_pos_of[lmost];
            int next_pos = next_pos_of[rmost];
            int tr = seg.get_first_larger_or_equal(prev_pos + 1, changed_pos, next_pos);
            seg.upd(prev_pos + 1, tr - 1, min(n - 1, next_pos));
        }

        if (prev_pos_of[changed_pos] != -1)
            next_pos_of[prev_pos_of[changed_pos]] = next_pos_of[changed_pos];
        if (next_pos_of[changed_pos] < n)
            prev_pos_of[next_pos_of[changed_pos]] = prev_pos_of[changed_pos];
        s[changed_pos] = 'x' - 'a';
    };

    int q;
    cin >> q;
    for (int qq = 1; qq <= q; qq++) {
        int t;
        cin >> t;
        if (t == 1) {
            int changed_pos;
            cin >> changed_pos;
            changed_pos--;
            change_pos(changed_pos);
        } else {
            int l, r;
            cin >> l >> r;
            l--, r--;
            ll ans = calc(seg, l, r);
            cout << ans << "\n";
        }
    }
}