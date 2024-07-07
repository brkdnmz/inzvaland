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
        // int ret = tl;
        // for (; ret <= tr; ret++) {
        //     if (get(ret, ret) >= threshold)
        //         break;
        // }
        // // return ret;
        // int ret2 = get_first_larger_or_equal(1, 0, n - 1, tl, tr, threshold);
        // if (ret != ret2) {
        //     cerr << tl << " " << tr << " " << threshold << endl;
        //     exit(0);
        // }
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
            prop(2 * c, l, mid); // IMPORTANT!
            if (seg[2 * c].last >= threshold)
                return get_first_larger_or_equal(2 * c, l, mid, tl, tr, threshold);
            return get_first_larger_or_equal(2 * c + 1, mid + 1, r, tl, tr, threshold);
        }
        return min(get_first_larger_or_equal(2 * c, l, mid, tl, tr, threshold),
                   get_first_larger_or_equal(2 * c + 1, mid + 1, r, tl, tr, threshold));
    }
};

vector<int> get_first_ok(string s, string tar) {
    // tar'da bir harften birden fazla olabileceği ihtimalini de hesaba katarak
    // daha genel bir algoritma yazdım.
    // Normalde tar'da aynı harften birden fazla olursa soruyu çözemiyorum.
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

ll gauss(ll x) { return x * (x + 1) / 2; }

ll calc(SegTree &seg, int l, int r) {
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

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    auto start = chrono::steady_clock::now();
    string s;
    cin >> s;
    string tar = "inzva";
    for (char &c : s)
        c -= 'a';
    bool is_tar[26] = {};
    for (char &c : tar)
        c -= 'a', is_tar[c] = 1;
    int n = s.size();
    set<int> pos[26];
    for (int i = 0; i < 26; i++)
        pos[i].insert(-1), pos[i].insert(n);
    for (int i = 0; i < n; i++) {
        pos[s[i]].insert(i);
    }

    auto first_ok = get_first_ok(s, tar);
    SegTree seg(first_ok);

    int q;
    cin >> q;
    for (int qq = 1; qq <= q; qq++) {
        int t;
        cin >> t;
        if (t == 1) {
            int changed_pos;
            cin >> changed_pos;
            changed_pos--;
            char prev_char = s[changed_pos];
            s[changed_pos] = 'x' - 'a';
            if (is_tar[prev_char]) {
                auto it = pos[prev_char].find(changed_pos);
                int prev_pos = *(prev(it));
                int next_pos = *(next(it));
                next_pos = min(n - 1, next_pos);
                pos[prev_char].erase(it);
                int tl = seg.get_first_larger_or_equal(prev_pos + 1, changed_pos, changed_pos);
                int tr = seg.get_first_larger_or_equal(prev_pos + 1, changed_pos, next_pos);
                seg.upd(tl, tr - 1, next_pos);
            }

            // first_ok = get_first_ok(s, tar);
        } else {
            int l, r;
            cin >> l >> r;
            l--, r--;
            // ll ans1 = calc(seg, l, r);
            // ll ans2 = calc_brute(first_ok, l, r);
            // if (ans1 != ans2) {
            //     cerr << qq << " mismatch\nl=" << l << "; r=" << r << "; ans1=" << ans1 << "; ans2=" << ans2 << "\n";
            //     return 0;
            // }
            cout << calc(seg, l, r) << "\n";
        }
    }
    auto end = chrono::steady_clock::now();
    cerr << chrono::duration_cast<chrono::milliseconds>(end - start).count() << endl;
}