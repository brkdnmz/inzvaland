#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;
vector<int> g[N];
int first_time[N];

void dfs(int c, int time) {
    first_time[c] = time;
    for (int n : g[c]) {
        if (first_time[n])
            continue;
        dfs(n, time);
    }
}

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    first_time[1] = 1;
    for (int i = 1; i <= m; i++) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
        if (first_time[a] && first_time[b])
            continue;
        if (first_time[a] || first_time[b]) {
            dfs(first_time[a] ? b : a, i);
        }
    }
    for (int i = 1; i <= n; i++) {
        cout << (first_time[i] ? m - first_time[i] + 1 : 0);
        if (i < n)
            cout << " ";
    }
}