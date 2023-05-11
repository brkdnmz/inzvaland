#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef uniform_int_distribution<ll> rnd;
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define REVERSE(v) reverse((v).begin(), (v).end())
#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))
#define pb push_back
#define FOR(i, n) for(int i = 0; i < (n); i++)
typedef pair<int, int> pii;
typedef long long ll;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
ll gen(ll l, ll r){
	return rnd(l, r)(rng);
}
ll gen1(ll r){
	return rnd(1, r)(rng);
}
ll gen0(ll r){
    return rnd(0, r)(rng);
}

vector<vector<int>> create_tree(int n, int max_weight){
    vector<vector<int>> edges;
    vector<int> nodes(n);
    FOR(i, n) nodes[i] = i+1;
    shuffle(nodes.begin(), nodes.end(), rng);
    for(int i = 1; i < n; i++){
        int parent = nodes[gen0(i-1)];
        vector<int> cur_edge = {parent, nodes[i], (int)gen0(max_weight)};
        bool do_swap = gen0(1);
        if(do_swap){
            swap(cur_edge[0], cur_edge[1]);
        }
        edges.pb(cur_edge);
    }
    return edges;
}

vector<vector<vector<int>>> create_adj(int n, vector<vector<int>> edges){
    vector<vector<vector<int>>> g(n+1);
    for(auto e: edges){
        int u = e[0], v = e[1], w = e[2];
        g[u].pb({v, w});
        g[v].pb({u, w});
    }
    return g;
}

vector<vector<ll>> calc_dijkstra(int n, int src, vector<vector<vector<int>>>& g){
    set<vector<ll>> st;
    // dist[node][last route to the node is paid]
    vector<vector<ll>> dist(n+1, vector<ll>(2, 1e18));
    // {distance, current node, last route to the node is paid}
    st.insert({0, src, 0});
    dist[src][0] = 0;
    // if you also set dist[src][1] to 0, it will cause some problems (e.g., the first route may not be paid)
    while(!st.empty()){
        auto tmp = *st.begin();
        st.erase(st.begin());
        int cur = tmp[1];
        bool is_prev_paid = tmp[2];
        bool is_cur_paid = !is_prev_paid;
        for(auto edge: g[cur]){
            int nxt = edge[0], cost = edge[1];
            ll new_dist = dist[cur][is_prev_paid] + is_cur_paid * cost;
            if(dist[nxt][is_cur_paid] <= new_dist) continue;
            st.erase({dist[nxt][is_cur_paid], nxt, is_cur_paid}); // https://cp-algorithms.com/graph/dijkstra_sparse.html
            dist[nxt][is_cur_paid] = new_dist;
            st.insert({dist[nxt][is_cur_paid], nxt, is_cur_paid});
        }
    }
    return dist;
}

ll solve(int n, int s, int t, vector<vector<vector<int>>>& g){
    vector<vector<ll>> dist_s = calc_dijkstra(n, s, g);
    return min(dist_s[t][0], dist_s[t][1]);
}

int main(){
    for(int tc = 0; tc < 5; tc++){
        ofstream input("input/input" + to_string(tc) + ".txt");
        ofstream output("output/output" + to_string(tc) + ".txt");
        int n = gen(2, 1e5);
        int m = n-1;
        vector<int> node_order(n);
        FOR(i, n) node_order[i] = i+1;
        shuffle(node_order.begin(), node_order.end(), rng);
        int s = node_order[0];
        int t = node_order[n-1];
        input << n << " " << m << " " << s << " " << t << "\n";
        int max_weight = 1e9;
        vector<vector<vector<int>>> g(n+1);
        for(int i = 1; i < n; i++){
            int prev = node_order[i-1];
            int cur = node_order[i];
            int w = gen0(max_weight);
            g[prev].pb({cur, w});
            g[cur].pb({prev, w});
            bool do_swap = gen0(1);
            if(do_swap){
                swap(prev, cur);
            }
            input << prev << " " << cur << " " << w << "\n";
        }
        ll ans = solve(n, s, t, g);
        output << ans << "\n";
        cout << ans << "\n";
    }
}