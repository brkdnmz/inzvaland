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

vector<vector<ll>> create_tree(int n, ll l_weight, ll r_weight){
    vector<vector<ll>> edges;
    vector<int> nodes(n);
    FOR(i, n) nodes[i] = i+1;
    shuffle(nodes.begin(), nodes.end(), rng);
    for(int i = 1; i < n; i++){
        int parent = nodes[max(0, gen(i-10, i-1))];
        vector<ll> cur_edge = {parent, nodes[i], gen(l_weight, r_weight)};
        bool do_swap = gen0(1);
        if(do_swap){
            swap(cur_edge[0], cur_edge[1]);
        }
        edges.pb(cur_edge);
    }
    return edges;
}

vector<vector<vector<ll>>> create_adj(int n, vector<vector<ll>> edges){
    vector<vector<vector<ll>>> g(n+1);
    for(auto e: edges){
        ll u = e[0], v = e[1], w = e[2];
        g[u].pb({v, w});
        g[v].pb({u, w});
    }
    return g;
}

vector<ll> find_loop(int cur, int prev, vector<vector<vector<ll>>>& g, vector<int>& par, vector<bool>& vis, vector<ll>& par_edge_w){
    //cerr<<cur<<"\n";
    vis[cur] = true;
    bool prev_seen = false;
    for(auto edge: g[cur]){
        ll nxt = edge[0], w = edge[1];
        if(nxt == prev){
            assert(nxt == par[cur]);
            if(prev_seen){
                return {cur, nxt, w};
            }
            prev_seen = true;
            continue;
        }
        if(vis[nxt]){
            assert(nxt != par[cur]);
            return {cur, nxt, w};
        }
        par[nxt] = cur;
        par_edge_w[nxt] = w;
        auto tmp = find_loop(nxt, cur, g, par, vis, par_edge_w);
        if(tmp.size()) return tmp;
    }
    return {};
}

int solve(vector<vector<vector<ll>>> g){
    int n = g.size() - 1;
    vector<int> par(n+1, 0);
    vector<bool> vis(n+1, 0);
    vector<ll> par_edge_w(n+1, 0);
    vector<ll> loop = find_loop(1, 0, g, par, vis, par_edge_w);
    vector<ll> weights(1, loop[2]);
    int start = loop[0], end = loop[1];
    int cur = start;
    do{
        weights.pb(par_edge_w[cur]);
        cur = par[cur];
        assert(cur);
    }while(cur != end);
    RSORT(weights);
    int cnt = 1;
    weights.pb(weights.back()-1); // for writing a nice for loop
    for(int i = 0; weights[i] == weights[i+1]; i++){
        cnt++;
    }
    return cnt;
}

bool connected(vector<vector<vector<ll>>> g){
    int n = g.size() - 1;
    vector<bool> vis(n+1, 0);
    queue<int> q;
    q.push(1);
    vis[1] = true;
    int cnt = 1;
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        for(auto edge: g[cur]){
            if(vis[edge[0]]) continue;
            vis[edge[0]] = true;
            cnt++;
            q.push(edge[0]);
        }
    }
    return cnt == n;
}
bool check(int n, vector<vector<ll>> edges){
    multiset<ll> weights;
    for(int i = 0; i < edges.size(); i++){
        vector<vector<ll>> new_edges;
        for(int j = 0; j < edges.size(); j++){
            if(j != i) new_edges.pb(edges[j]);
        }
        auto g = create_adj(n, new_edges);
        if(connected(g)){
            weights.insert(edges[i][2]);
        }
    }
    return weights.count(*weights.rbegin()) == solve(create_adj(n, edges));
}
const int N = 2e5;
const ll W = 10;
int main(){
    for(int tc = 0; tc < 5; tc++){
        ofstream input("input/input" + to_string(tc) + ".txt");
        ofstream output("output/output" + to_string(tc) + ".txt");
        int n = N;
        auto edges = create_tree(n, -W, W);
        int u = gen(n);
        int v = gen(n);
        while(v == u) v = gen(n);
        edges.pb({u, v, gen(-W, W)});
        auto g = create_adj(n, edges);
        int cnt = solve(g);
        input << n << "\n";
        for(auto edge: edges){
            input << edge[0] << " " << edge[1] << " " << edge[2] << "\n";
        }
        output << cnt << "\n";
        //assert(check(n, edges));
    }
}