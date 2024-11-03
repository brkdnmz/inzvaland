#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5; // Max. number of nodes
const int M = 18;      // Type "log2(2e5)" in browser's search bar, you'll see 17.6...

vector<int> g[N];
int p[N][M]; // p[u][j] = u's (2^j)-th ancestor
// Notice since it's global, all elements initialize to 0,
// so, we would access p[0][...] below, which is safe!

void dfs(int cur, int par) {
    p[cur][0] = par;

    // You could also do this in `main`
    for (int i = 1; i < M; i++)
        p[cur][i] = p[p[cur][i - 1]][i - 1];

    for (int nxt : g[cur]) {
        if (nxt == par)
            continue;
        dfs(nxt, cur);
    }
}

int kth_ancestor(int u, int k) {
    // Iterate through k's bits, jump whenever encountered 1
    for (int i = M - 1; i >= 0; i--) {
        // >= has a higher precedence than <<, hence the parentheses
        if (k >= (1 << i)) {
            k -= 1 << i;
            u = p[u][i];
        }
    }
    return u;
}

// I don't really use this
int kth_ancestor_alternative(int u, int k) {
    int bit = 0;
    while (k) {
        if (k % 2)
            u = p[u][bit];
        k /= 2, bit++;
    }
    return u;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
    }

    dfs(1, 0);

    // Do what you want
}