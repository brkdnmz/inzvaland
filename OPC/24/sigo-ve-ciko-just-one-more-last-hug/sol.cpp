#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 1e6 + 5;

int seg[4 * N];
vector<bool> sigociko(N);

int n;

#define mid (l + r) / 2

void build(int c, int l, int r) {
    if (l == r) {
        seg[c] = sigociko[l];
        return;
    }
    build(2 * c, l, mid);
    build(2 * c + 1, mid + 1, r);
    seg[c] = seg[2 * c] + seg[2 * c + 1];
}

void toggle(int c, int l, int r, int t) {
    if (l == r) {
        seg[c] ^= 1;
        return;
    }
    t <= mid ? toggle(2 * c, l, mid, t) : toggle(2 * c + 1, mid + 1, r, t);
    seg[c] = seg[2 * c] + seg[2 * c + 1];
}

int get(int c, int l, int r, int tl) {
    if (l > tl)
        return 0;
    if (r <= tl)
        return seg[c];
    return get(2 * c, l, mid, tl) + get(2 * c + 1, mid + 1, r, tl);
}

int get_kth(int c, int l, int r, int k) {
    if (l == r)
        return l + !seg[c];
    return k <= seg[2 * c] ? get_kth(2 * c, l, mid, k) : get_kth(2 * c + 1, mid + 1, r, k - seg[2 * c]);
}

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    int n_sum = 0, q_sum = 0;

    while (t--) {
        int q;
        cin >> n >> q;

        assert(1 <= n && n <= 1e6);
        assert(1 <= q && q <= 2e5);

        n_sum += n, q_sum += q;

        vector<bool> buf(n);
        for (int i = 0; i < n; i++) {
            char c;
            cin >> c;
            assert(c == 'S' || c == 'C');
            buf[i] = c == 'C';
        }

        for (int i = 0; i < n; i++) {
            sigociko[i] = !i || buf[i - 1] != buf[i];
        }

        build(1, 0, n - 1);

        auto get_ans = [&](int l, int tl, int r, int tr) {
            assert(l < tl && tr < r && l < r && tl > tr);
            // l -> tl
            // tr <- r

            ll a = r - l;
            ll b = tl - tr;
            ll l_dist = tl - l;
            // l + a/(a+b) * (tl - l)
            ll p = a * l_dist;
            ll q = a + b;
            ll g = __gcd(p, q);
            p /= g, q /= g;
            return q * l + p;
        };

        auto answer_query = [&](int l, int r) -> ll {
            if (l == r) {
                return l + 1;
            }

            int n_ones_before_r = get(1, 0, n - 1, r);
            int n_ones_before_l = get(1, 0, n - 1, l); // 1 at l is ignored
            int n_ones_between = n_ones_before_r - n_ones_before_l;

            if (n_ones_between <= 1) {
                int before_r = get_kth(1, 0, n - 1, n_ones_before_r);
                int after_l = get_kth(1, 0, n - 1, n_ones_before_r + (before_r <= l));
                return get_ans(l + 1, after_l + 1, r + 1, before_r - 1 + 1);
            } else {
                int l_last = get_kth(1, 0, n - 1, n_ones_before_l + n_ones_between / 2);
                int r_last = get_kth(1, 0, n - 1, n_ones_before_r - n_ones_between / 2 + 1) - 1;

                if (l_last == r_last) {
                    return l_last + 1;
                } else {
                    int l_dest = get_kth(1, 0, n - 1, n_ones_before_l + n_ones_between / 2 + 1);
                    int r_dest = get_kth(1, 0, n - 1, n_ones_before_r - n_ones_between / 2) - 1;
                    return get_ans(l_last + 1, l_dest + 1, r_last + 1, r_dest + 1);
                }
            }
        };

        cout << answer_query(0, n - 1) << "\n";

        while (q--) {
            int t, l, r;
            cin >> t >> l >> r;

            assert(t == 1 || t == 2);
            assert(1 <= l && l <= n);
            assert(1 <= r && r <= n);

            if (l > r)
                swap(l, r);

            l--, r--;

            if (t == 1) {
                ll ans = answer_query(l, r);
                cout << ans << "\n";
            } else {
                if (l)
                    toggle(1, 0, n - 1, l);
                // int first_of_r_group = get_kth(1, 0, n - 1, get(1, 0, n - 1, r));
                // assert(l <= first_of_r_group);
                // if (first_of_r_group > l) {
                //     toggle(1, 0, n - 1, first_of_r_group);
                // }

                if (r + 1 < n)
                    toggle(1, 0, n - 1, r + 1);
            }
        }

        cout << answer_query(0, n - 1);
        if (t)
            cout << "\n";
    }
    assert(n_sum <= 1e6);
    assert(q_sum <= 2e5);
}