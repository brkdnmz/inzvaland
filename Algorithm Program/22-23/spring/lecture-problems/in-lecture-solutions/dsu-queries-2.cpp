#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define FOR(i, n) for (int i = 0; i < (n); i++)
using ll = long long;

const int N = 2e5 + 5;

int par[N];      // par[i] = i'nin bulunduğu setin lideri/parent'ı
int set_size[N]; // set_size[i] = i'nin bulunduğu set içindeki node sayısı

// u'nun bulunduğu setin liderini bul
int find_leader(int u) {
    if (u == par[u])
        return u;
    return (par[u] = find_leader(par[u]));
}

// u ve v'nin bulunduğu setleri birleştir
void union_sets(int u, int v) {
    u = find_leader(u);
    v = find_leader(v);
    if (u == v)
        return;

    if (set_size[u] < set_size[v])
        swap(u, v);

    par[v] = u;
    set_size[u] += set_size[v];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < N; i++) {
        par[i] = i;
        set_size[i] = 1;
    }

    int n, q;
    cin >> n >> q;
    while (q--) {
        int t, u;
        cin >> t >> u;
        if (t == 1) {
            int v;
            cin >> v;
            // u ve v'nin bulunduğu setleri birleştir
            union_sets(u, v);
        }
        cout << set_size[find_leader(u)] << "\n";
    }
}