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

vector<ll> solve(int n, int m, vector<vector<vector<int>>>& g){
    int n_nodes = n+m;
    set<vector<ll>> st;
    vector<ll> dist(n_nodes+1, 1e18);
    for(int i = n+1; i <= n+m; i++){
        st.insert({0, i});
        dist[i] = 0;
    }
    while(!st.empty()){
        auto tmp = *st.begin();
        st.erase(st.begin());
        int cur = tmp[1];
        for(auto edge: g[cur]){
            int nxt = edge[0], cost = edge[1];
            ll new_dist = dist[cur] + cost;
            if(dist[nxt] <= new_dist) continue;
            st.erase({dist[nxt], nxt}); // https://cp-algorithms.com/graph/dijkstra_sparse.html
            dist[nxt] = new_dist;
            st.insert({dist[nxt], nxt});
        }
    }
    vector<ll> ans(n);
    for(int i = 1; i <= n; i++) ans[i-1] = dist[i];
    for(ll dst: ans) assert(dst != 1e18);
    return ans;
}

int main(){
    for(int tc = 0; tc < 5; tc++){
        ofstream input("input/input" + to_string(tc) + ".txt");
        ofstream output("output/output" + to_string(tc) + ".txt");
        int n = gen1(1e5);
        int m = gen1(1e5);
        int n_nodes = n+m;
        int k = gen(n_nodes-1, 2e5);
        input << n << " " << m << " " << k << "\n";
        int max_weight = gen0(1e9);
        auto edges = create_tree(n_nodes, max_weight);
        k -= n_nodes - 1;
        while(k--){
            int u = gen1(n_nodes);
            int v = gen1(n_nodes);
            while(v == u) v = gen1(n_nodes);
            edges.pb({u, v, (int)gen0(max_weight)});
        }
        for(auto edge: edges){
            input << edge[0] << " " << edge[1] << " " << edge[2] << "\n";
        }
        auto g = create_adj(n_nodes, edges);
        auto ans = solve(n, m, g);
        for(auto dist: ans) output << dist << " ";
    }
}