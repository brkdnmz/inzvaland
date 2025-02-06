#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int LOG = 18;

int main(int argc, char **argv) {
    // freopen(argv[1], "r", stdin);
    // freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    int n_sum = 0, s_sum = 0;
    while (t--) {
        int n;
        cin >> n;
        n_sum += n;
        string sigociko;
        cin >> sigociko;

        for (char c : sigociko) {
            assert(c == 'S' || c == 'C');
        }

        sigociko = "$" + sigociko + "$";

        int forward_jump[n + 2][LOG] = {}, backward_jump[n + 2][LOG] = {};
        // 0 for Sigo, 1 for Ciko
        int nxt[n + 2][2], prv[n + 2][2];
        int nearest[2] = {n + 1, n + 1};
        for (int i = n + 1; i >= 0; i--) {
            for (int j : {0, 1})
                nxt[i][j] = nearest[j];
            bool is_ciko = sigociko[i] == 'C';
            forward_jump[i][0] = nearest[!is_ciko];
            nearest[is_ciko] = i;
        }

        nearest[0] = nearest[1] = 0;
        for (int i = 0; i <= n + 1; i++) {
            for (int j : {0, 1})
                prv[i][j] = nearest[j];
            bool is_ciko = sigociko[i] == 'C';
            backward_jump[i][0] = nearest[!is_ciko];
            nearest[is_ciko] = i;
        }

        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i <= n + 1; i++) {
                forward_jump[i][j] = forward_jump[forward_jump[i][j - 1]][j - 1];
                backward_jump[i][j] = backward_jump[backward_jump[i][j - 1]][j - 1];
            }
        }

        auto find_meeting_point = [&](int rumeysa, int rumeysa_target, int elif, int elif_target) {
            ll a = abs(elif - rumeysa);
            ll b = abs(rumeysa_target - elif_target);
            ll rumeysa_dist = rumeysa_target - rumeysa;
            // rumeysa + a/(a+b) * rumeysa_dist
            ll p = a * rumeysa_dist;
            ll q = a + b;
            ll g = __gcd(abs(p), abs(q));
            p /= g, q /= g;
            return q * rumeysa + p;
        };

        int s;
        cin >> s;
        s_sum += s;

        while (s--) {
            int r, e;
            cin >> r >> e;

            assert(0 <= r && r <= n + 1);
            assert(0 <= e && e <= n + 1);

            int rumeysa = r, elif = e;

            ll meeting_point = 0;

            if (r == e) {
                meeting_point = r;
                goto print_ans;
            }

            if (r < e) {
                // Rumeysa goes right, Elif goes left

                // Edge case: First jump
                if (nxt[rumeysa][0] >= prv[elif][1]) {
                    meeting_point = find_meeting_point(rumeysa, min(nxt[rumeysa][0], e), elif, max(prv[elif][1], r));
                    goto print_ans;
                }

                rumeysa = nxt[rumeysa][0], elif = prv[elif][1];

                for (int j = LOG - 1; j >= 0; j--) {
                    if (forward_jump[rumeysa][j] < backward_jump[elif][j]) {
                        rumeysa = forward_jump[rumeysa][j];
                        elif = backward_jump[elif][j];
                    }
                }

                meeting_point =
                    find_meeting_point(rumeysa, min(forward_jump[rumeysa][0], e), elif, max(backward_jump[elif][0], r));
            } else {
                // Rumeysa goes left, Elif goes right

                // Edge case: First jump
                if (prv[rumeysa][0] <= nxt[elif][1]) {
                    meeting_point = find_meeting_point(rumeysa, max(prv[rumeysa][0], e), elif, min(nxt[elif][1], r));
                    goto print_ans;
                }

                rumeysa = prv[rumeysa][0], elif = nxt[elif][1];

                for (int j = LOG - 1; j >= 0; j--) {
                    if (backward_jump[rumeysa][j] > forward_jump[elif][j]) {
                        rumeysa = backward_jump[rumeysa][j];
                        elif = forward_jump[elif][j];
                    }
                }

                meeting_point =
                    find_meeting_point(rumeysa, max(backward_jump[rumeysa][0], e), elif, min(forward_jump[elif][0], r));
            }

        print_ans:
            cout << meeting_point;
            if (s)
                cout << "\n";
        }

        if (t)
            cout << "\n";
    }
    assert(1 <= n_sum && n_sum <= 5e5);
    assert(1 <= s_sum && s_sum <= 5e5);
}