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

vector<vector<int>> mst(int n, vector<vector<vector<int>>> g){
    vector<bool> added(n+1, 0);
    set<vector<int>> edges;
    added[1] = true;
    for(auto edge: g[1]){
        int nxt = edge[0], w = edge[1];
        edges.insert({w, nxt, 1});
    }
    vector<vector<int>> added_edges;
    while(!edges.empty()){
        auto tmp = *edges.begin();
        edges.erase(edges.begin());
        int cur = tmp[1];
        if(added[cur]) continue;
        added[cur] = true;
        added_edges.pb(tmp);
        for(auto edge: g[cur]){
            int nxt = edge[0], w = edge[1];
            if(added[nxt]) continue;
            edges.insert({w, nxt, cur});
        }
    }
    return added_edges;
}

ll mst_cost(vector<vector<int>> mst){
    ll cost = 0;
    for(auto edge: mst) cost += edge[0];
    return cost;
}

int main(){
    for(int tc = 0; tc < 20; tc++){
        ofstream input("input/input" + to_string(tc) + ".txt");
        ofstream output("output/output" + to_string(tc) + ".txt");
        int n = gen(2, 1e5);
        int m = gen(n-1, 1e5);
        input << n << " " << m << "\n";
        int max_weight = 1e9;
        auto edges = create_tree(n, max_weight);
        m -= n-1;
        while(m--){
            int u = gen1(n);
            int v = gen1(n);
            while(v == u) v = gen1(n);
            int w = gen0(max_weight);
            edges.pb({u, v, w});
        }
        shuffle(edges.begin(), edges.end(), rng);
        for(auto edge: edges){
            input << edge[0] << " " << edge[1] << " " << edge[2] << "\n";
        }
        auto g = create_adj(n, edges);
        auto mst_edges = mst(n, g);
        ll cost = mst_cost(mst_edges);
        output << cost << "\n";
        cout << cost << "\n";
    }
}