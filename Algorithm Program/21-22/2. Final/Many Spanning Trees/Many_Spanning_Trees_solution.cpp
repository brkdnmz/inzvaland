#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define pb push_back
#define FOR(i, n) for(int i = 0; i < (n); i++)

const int N = 2e5 + 5;
vector<vector<ll>> g[N];
vector<int> par(N);
vector<bool> vis(N);
vector<ll> par_edge_weight(N);
// finds an edge in the loop
vector<ll> find_loop(int cur, int prev){
    vis[cur] = true;
    bool seen_prev = false;
    for(auto edge: g[cur]){
        int nxt = edge[0];
        ll w = edge[1];
        if(nxt == prev){
            if(seen_prev){ // this detects a loop consisting of two nodes
                // example: there are 2 edges connecting the nodes 1 and 2
                return {cur, prev, w};
            }
            seen_prev = true;
            continue;
        }
        if(vis[nxt]){ // it is certainly a loop
            return {cur, nxt, w};
        }
        par[nxt] = cur;
        par_edge_weight[nxt] = w;
        auto possible_loop = find_loop(nxt, cur);
        if(possible_loop.size())
            return possible_loop; // loop is found
    }
    return {}; // return empty vector
}
int main(){
    int n; cin>>n;
    FOR(i, n){
        int u, v;
        ll w;
        cin>>u>>v>>w;
        g[u].pb({v, w});
        g[v].pb({u, w});
    }
    /*          [Try to figure out]
        Due to its order of exploring the nodes,
        find_loop will find such an edge that
        "end_node" is an ancestor of "start_node"
        with respect to "par" vector.
        That's why the solution below works.
    */
    auto edge_in_loop = find_loop(1, 0);
    int start_node = edge_in_loop[0];
    int end_node = edge_in_loop[1];
    ll w = edge_in_loop[2];
    vector<ll> weights_in_loop(1, w);
    int cur = start_node;
    do{
        weights_in_loop.pb(par_edge_weight[cur]);
        cur = par[cur];
    }while(cur != end_node);
    // Count the number of max. weights.
    // An MST appears when any of these edges
    // is removed.
    RSORT(weights_in_loop);
    weights_in_loop.pb(weights_in_loop.back()+1);
    int cnt = 1;
    for(int i = 0; weights_in_loop[i] == weights_in_loop[i+1]; i++){
        cnt++;
    }
    cout<<cnt<<"\n";
}