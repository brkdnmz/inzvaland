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
template<typename T>
T gen(T l, T r){
	return rnd(l, r)(rng);
}
template<typename T>
T gen(T r){
	return rnd(1, r)(rng);
}
template<typename T>
T gen0(T r){
    return rnd(0, r)(rng);
}

vector<vector<int>> create_tree(int n){
    vector<vector<int>> edges;
    vector<int> nodes(n);
    FOR(i, n) nodes[i] = i+1;
    shuffle(nodes.begin(), nodes.end(), rng);
    for(int i = 1; i < n; i++){
        int parent = nodes[gen0(i-1)];
        vector<int> cur_edge = {parent, nodes[i]};
        bool do_swap = gen0(1);
        if(do_swap){
            swap(cur_edge[0], cur_edge[1]);
        }
        edges.pb(cur_edge);
    }
    return edges;
}

vector<vector<int>> create_adj(int n, vector<vector<int>> edges){
    vector<vector<int>> g(n+1);
    for(auto e: edges){
        int u = e[0], v = e[1];
        g[u].pb(v);
        g[v].pb(u);
    }
    return g;
}

vector<vector<ll>> dijkstra(vector<vector<int>> g, vector<int>& weight, int s){
    int n = g.size() - 1;
    g[0].pb(1);
    vector<vector<ll>> dist(n+1, vector<ll>(s+1, 1e18));
    dist[0][0] = 0;
    set<vector<ll>> st;
    // {dist, node, skips}
    st.insert({0, 0, 0});
    while(!st.empty()){
        auto tmp = *st.begin();
        st.erase(tmp);
        int cur = tmp[1];
        int skips = tmp[2];
        for(int nxt: g[cur]){
            // do not skip
            if(dist[nxt][skips] > dist[cur][skips] + weight[nxt]){
                st.erase({dist[nxt][skips], nxt, skips});
                dist[nxt][skips] = dist[cur][skips] + weight[nxt];
                st.insert({dist[nxt][skips], nxt, skips});
            }

            // skip
            if(skips == s) continue;
            if(dist[nxt][skips+1] > dist[cur][skips]){
                st.erase({dist[nxt][skips+1], nxt, skips+1});
                dist[nxt][skips+1] = dist[cur][skips];
                st.insert({dist[nxt][skips+1], nxt, skips+1});
            }
        }
    }
    return dist;
}

const int N = 1e5;
const int W = 1e9;
int main(){
    for(int tc = 0; tc < 3; tc++){
        ofstream input("input/input" + to_string(tc) + ".txt");
        ofstream output("output/output" + to_string(tc) + ".txt");
        int n, m, k, s;

        n = gen(N);
        m = gen(n-1, N);
        k = gen(n);
        s = gen(20);
        input << n << " " << m << " " << k << " " << s << "\n";

        vector<int> len(n+1);
        for(int i = 1; i <= n; i++){
            len[i] = gen(W);
        }
        for(int i = 1; i <= n; i++){
            input << len[i] << " ";
        }
        input << "\n";

        auto edges = create_tree(n);
        m -= n-1;
        while(m--){
            int u = gen(n);
            int v = gen(n);
            while(v == u) v = gen(n);
            edges.pb({u, v});
        }

        for(auto edge: edges){
            input << edge[0] << " " << edge[1] << "\n";
        }

        vector<int> nodes(n);
        FOR(i, n) nodes[i] = i+1;
        shuffle(nodes.begin(), nodes.end(), rng);
        vector<int> final_nodes(nodes.begin(), nodes.begin() + k);
        for(int node: final_nodes){
            input << node << " ";
        }
        input << "\n";

        auto g = create_adj(n, edges);
        auto dist = dijkstra(g, len, s);
        ll min_dist = 1e18;
        for(int node: final_nodes){
            min_dist = min(min_dist, dist[node][s]);
        }
        output << min_dist;
    }
}