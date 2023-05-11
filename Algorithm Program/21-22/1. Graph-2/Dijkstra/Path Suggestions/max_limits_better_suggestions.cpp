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

vector<ll> calc_dijkstra(int n, int src, vector<vector<vector<int>>>& g){
    set<vector<ll>> st;
    vector<ll> dist(n+1, 1e18);
    st.insert({0, src});
    dist[src] = 0;
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
    return dist;
}

vector<ll> solve(int n, int s, int d, vector<vector<vector<int>>>& g, vector<vector<int>>& suggestions){
    set<vector<ll>> st;
    vector<ll> dist_s = calc_dijkstra(n, s, g);
    vector<ll> dist_d = calc_dijkstra(n, d, g);
    vector<ll> ans;
    int suggestion_worked = 0;
    for(auto& edge: suggestions){
        int& u = edge[0], v = edge[1], w = edge[2];
        int make_better_strength = 10;
        bool make_better = gen0(make_better_strength);
        if(make_better < make_better_strength){
            ll min_val = min(dist_s[u] + dist_d[v], dist_s[v] + dist_d[u]);
            if(dist_s[d] - min_val - 1 >= 0){
                w = max(0, (int)min((ll)1e9, gen0(dist_s[d] - min_val - 1)));
            }
        }
        ll cur_ans = min({dist_s[d], dist_s[u] + w + dist_d[v], dist_s[v] + w + dist_d[u]});
        ans.pb(cur_ans);
        suggestion_worked += cur_ans < dist_s[d];
    }
    cout << "number of suggestions worked: " << suggestion_worked << "\n";
    return ans;
}

int main(){
    for(int tc = 0; tc < 1; tc++){
        ofstream input("input/input" + to_string(tc) + ".txt");
        ofstream output("output/output" + to_string(tc) + ".txt");
        int n = 1e5;
        int m = 1e5;
        int s = gen1(n);
        int d = gen1(n);
        input << n << " " << m << " " << s << " " << d << "\n";
        int max_weight = 1e9;
        auto edges = create_tree(n, max_weight);
        m -= n - 1;
        while(m--){
            int u = gen1(n);
            int v = gen1(n);
            while(v == u) v = gen1(n);
            edges.pb({u, v, (int)gen0(max_weight)});
        }
        for(auto edge: edges){
            input << edge[0] << " " << edge[1] << " " << edge[2] << "\n";
        }
        auto g = create_adj(n, edges);
        int S = 1e5;
        input << S << "\n";
        vector<vector<int>> suggestions;
        FOR(i, S){
            int u = gen1(n);
            int v = gen1(n);
            while(v == u) v = gen1(n);
            suggestions.pb({u, v, (int)gen0(max_weight)});
        }
        auto ans = solve(n, s, d, g, suggestions);
        for(auto edge: suggestions)
            input << edge[0] << " " << edge[1] << " " << edge[2] << "\n";
        for(ll x: ans) output << x << "\n";
    }
}