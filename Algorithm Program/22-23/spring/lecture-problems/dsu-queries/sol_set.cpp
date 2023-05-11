#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;
vector<int> sets[N];
int set_of[N];

vector<int> &get(int u) {
    return sets[set_of[u]];
}

void combine(int u, int v) {
    if (get(u).size() < get(v).size()) {
        swap(u, v);
    }

    if (set_of[u] == set_of[v])
        return;

    auto &u_set = get(u);
    auto &v_set = get(v);
    while (v_set.size()) {
        u_set.push_back(v_set.back());
        set_of[u_set.back()] = set_of[u];
        v_set.pop_back();
    }
    vector<int>().swap(v_set); // capacity won't reset without this, not required anyway
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    for (int i = 1; i < N; i++)
        sets[i] = {i}, set_of[i] = i;
    int n, q;
    cin >> n >> q;
    while (q--) {
        int t, u;
        cin >> t >> u;
        if (t == 1) {
            int v;
            cin >> v;
            assert(u != v);
            combine(u, v);
        }
        cout << get(u).size() << "\n";
    }
}