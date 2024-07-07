#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 2e5 + 5;
vector<int> g[N];
vector<int> component_no(N), max_of_component(N), min_of_component(N, 1e9);
vector<int> dist_to_max(N, 1e9), dist_to_sigo(N, 1e9), dist_to_ciko(N, 1e9);
ll pre_sum_costs[N];
int cur_component_no;

void dfs(int n) {
    component_no[n] = cur_component_no;
    min_of_component[cur_component_no] = min(min_of_component[cur_component_no], n);
    max_of_component[cur_component_no] = max(max_of_component[cur_component_no], n);
    for (int nxt : g[n]) {
        if (component_no[nxt])
            continue;
        dfs(nxt);
    }
}

void calc_dist_within_component(int source, vector<int> &dist) {
    queue<int> q;
    q.push(source);
    dist[source] = 0;
    while (q.size()) {
        int cur = q.front();
        q.pop();
        for (int nxt : g[cur]) {
            if (dist[nxt] <= dist[cur] + 1)
                continue;
            dist[nxt] = dist[cur] + 1;
            q.push(nxt);
        }
    }
}

void preprocess_components() {
    int n_components = cur_component_no;
    for (int i = 1; i <= n_components; i++) {
        calc_dist_within_component(max_of_component[i], dist_to_max);
    }
    for (int i = 1; i <= n_components; i++) {
        pre_sum_costs[i] = pre_sum_costs[i - 1] + min_of_component[i] + dist_to_max[min_of_component[i]];
    }
}

ll calc_dist(int node, int sigo_or_ciko, vector<int> &dist_to_sigo_or_ciko) {
    int o1 = component_no[node], o2 = component_no[sigo_or_ciko];
    if (o1 == o2) {
        return dist_to_sigo_or_ciko[node];
    }

    ll dist = dist_to_max[node] + min_of_component[component_no[sigo_or_ciko]] +
              dist_to_sigo_or_ciko[min_of_component[component_no[sigo_or_ciko]]];
    if (o1 < o2) {
        dist += pre_sum_costs[o1 - 1] + pre_sum_costs[o2 - 1] - pre_sum_costs[o1];
    } else {
        dist += pre_sum_costs[o2 - 1];
    }

    return dist;
}

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m, sigo, ciko;
    cin >> n >> m >> sigo >> ciko;

    assert(1 <= n && n <= 2e5);
    assert(0 <= m && m <= 2e5);
    assert(1 <= sigo && sigo <= n);
    assert(1 <= ciko && ciko <= n);

    while (m--) {
        int a, b;
        cin >> a >> b;
        assert(1 <= a && a <= n);
        assert(1 <= b && b <= n);
        g[a].push_back(b);
        g[b].push_back(a);
    }

    for (int i = 1; i <= n; i++) {
        if (component_no[i])
            continue;
        cur_component_no++;
        dfs(i);
    }

    calc_dist_within_component(sigo, dist_to_sigo);
    calc_dist_within_component(ciko, dist_to_ciko);

    preprocess_components();

    int q;
    cin >> q;
    assert(1 <= q && q <= 2e5);
    while (q--) {
        int rumeysa, elif;
        cin >> rumeysa >> elif;
        assert(1 <= rumeysa && rumeysa <= n);
        assert(1 <= elif && elif <= n);
        ll rumeysa_dist = calc_dist(rumeysa, sigo, dist_to_sigo) + calc_dist(sigo, ciko, dist_to_ciko);
        ll elif_dist = calc_dist(elif, ciko, dist_to_ciko);
        cout << rumeysa_dist << " " << elif_dist << "\n";
    }
}