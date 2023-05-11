#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define FOR(i, n) for (int i = 0; i < (n); i++)
using ll = long long;

const int N = 2e5 + 5;

vector<int> sets[N];
int set_of[N]; // set_of[u] = u'nun bulunduğu setin index'i

// u'nun bulunduğu seti ver
vector<int> &parent(int u) {
    return sets[set_of[u]];
}

// u ve v'nin bulunduğu setleri birleştir
void union_sets(int u, int v) {
    // u'nun bulunduğu set {1, 2, 4}
    // v'nin bulunduğu {3, 5}
    // u'nun bulunduğu setin index'i u olsun
    // v'nin bulunduğu v
    // yeni hali -> {1, 2, 3, 4, 5}
    // u'nun bulunduğu yine u
    // ama artık v'nin bulunduğu da u

    // z ile v'yi birleştir
    // z'nin bulunduğu {9, 10}
    // v'nin bulunduğu {1, 2, 3, 4, 5}

    if (parent(u).size() < parent(v).size())
        swap(u, v);

    if (set_of[u] == set_of[v])
        return;

    // v'nin bulunduğu setteki tüm node'ları u'nun bulunduğu sete aktar
    vector<int> set_v = parent(v);
    for (int i = 0; i < set_v.size(); i++) {
        int node = set_v[i];
        parent(u).push_back(node);
        set_of[node] = set_of[u];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < N; i++) {
        sets[i] = {i};
        set_of[i] = i;
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
        cout << parent(u).size() << "\n";
    }
}