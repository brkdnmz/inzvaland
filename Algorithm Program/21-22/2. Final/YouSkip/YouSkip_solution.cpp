#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define FOR(i, n) for(int i = 0; i < (n); i++)
typedef long long ll;

struct Q{
    ll dist;
    int node;
    int skips;
    bool operator<(const Q& o) const{
        // for priority_queue, define < operator as > operator
        return dist > o.dist;
    }
};
const int N = 1e5 + 5;
int main(){
    int n, m, k, s; cin>>n>>m>>k>>s;
    vector<vector<int>> g(N);
    vector<int> w(N);
    FOR(i, n){
        cin>>w[i+1];
    }
    while(m--){
        int u, v; cin>>u>>v;
        g[u].pb(v);
        g[v].pb(u);
    }
    // instead of edges, we have weighted nodes
    // consider every edge a combination of 2 edges with reverse directions
    // for every edge u -> v, define w(u -> v) = w(v)
    // besides, define two additional nodes: 0 and n+1
    // connected 0 to 1 with 0-weighted edge
    // connect every final node to n+1 with 0-weighted edges
    // you will obtain an equivalent graph with weighted edges instead
    // you actually need not apply these above, it just eases the understanding
    // apply dijkstra's algorithm with dp
    while(k--){
        int final_node; cin>>final_node;
        g[final_node].pb(n+1);
    }
    g[0].pb(1);
    vector<vector<ll>> dist(N, vector<ll>(s+1, 1e18));
    dist[0][0] = 0;
    priority_queue<Q> q;
    // dist, node, skips
    q.push(Q{0, 0, 0});
    while(!q.empty()){
        Q top = q.top();
        q.pop();
        int cur = top.node;
        int skips = top.skips;
        if(top.dist != dist[cur][skips])
            continue;
        for(int nxt: g[cur]){
            // do not skip
            if(dist[nxt][skips] > dist[cur][skips] + w[nxt]){
                dist[nxt][skips] = dist[cur][skips] + w[nxt];
                q.push(Q{dist[nxt][skips], nxt, skips});
            }
            // skip
            if(skips == s)
                continue;
            if(dist[nxt][skips+1] > dist[cur][skips]){
                dist[nxt][skips+1] = dist[cur][skips];
                q.push(Q{dist[nxt][skips+1], nxt, skips+1});
            }
        }
    }
    cout<<dist[n+1][s]<<"\n";
}