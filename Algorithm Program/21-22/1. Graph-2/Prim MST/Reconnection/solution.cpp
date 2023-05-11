#include <bits/stdc++.h>
using namespace std;
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define REVERSE(v) reverse((v).begin(), (v).end())
#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))
#define pb push_back
#define FOR(i, n) for(int i = 0; i < (n); i++)
typedef pair<int, int> pii;
typedef long long ll;

ll mst_cost(vector<vector<vector<int>>> g){
    int n = g.size()-1;
    vector<bool> added(n+1, 0);
    set<vector<int>> edges;
    ll cost = 0;
    added[1] = true;
    for(auto edge: g[1]){
        edges.insert({edge[1], edge[0]});
    }
    while(!edges.empty()){
        auto tmp = *edges.begin();
        edges.erase(tmp);
        int cur = tmp[1];
        if(added[cur]) continue;
        added[cur] = true;
        cost += tmp[0];
        for(auto edge: g[cur]){
            int nxt = edge[0];
            int w = edge[1];
            if(added[nxt]) continue;
            edges.insert({w, nxt});
        }
    }
    return cost;
}
int main(){
    int n, p, m;
    cin>>n>>p>>m;

    map<vector<int>, int> compulsory;
    for(int i = 0; i < p; i++){
        int u, v; cin>>u>>v;
        if(u > v) swap(u, v);
        compulsory[{u, v}] = 1e9;
    }
    vector<vector<vector<int>>> g(n+1);
    vector<vector<vector<int>>> modified_g(n+1);
    for(int i = 0; i < m; i++){
        int u, v, w; cin>>u>>v>>w;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
        if(u > v) swap(u, v);
        if(compulsory.count({u, v})){
            compulsory[{u, v}] = min(compulsory[{u, v}], w);
            w = 0;
        }
        modified_g[u].push_back({v, w});
        modified_g[v].push_back({u, w});
    }
    ll compul_cost = mst_cost(modified_g);
    for(auto x: compulsory) compul_cost += x.second;
    ll cost = mst_cost(g);
    cout<<(cost == compul_cost ? "YES" : "NO");
}