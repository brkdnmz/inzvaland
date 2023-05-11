#include <bits/stdc++.h>
using namespace std;

#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define REVERSE(v) reverse((v).begin(), (v).end())
#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))
#define pb push_back
#define FOR(i, n) for(int i = 0; i < (n); i++)
typedef long long ll;
typedef unsigned long long ull;

int mod = 1e9 + 7;
// int mod = 998244353;

inline void sum_self(int& a, int b) {a += b;if (a >= mod) a -= mod;if (a < 0) a += mod;}
inline int mul(int a, int b) {a = 1ll * a * b % mod;return a;}

const int N = 2e5 + 5;
vector<int> g[N];
int val[N];
ll dp[N][2];
void dfs(int c, int p){
    dp[c][1] = val[c];
    for(int n: g[c]){
        if(n == p) continue;
        dfs(n, c);
        dp[c][1] += dp[n][0];
        dp[c][0] += max(dp[n][0], dp[n][1]);
    }
}
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
    int n; cin>>n;
    FOR(i, n-1){
        int a, b; cin>>a>>b;
        g[a].pb(b);
        g[b].pb(a);
    }
    FOR(i, n) cin>>val[i+1];
    dfs(1, 0);
    cout<<max(dp[1][0], dp[1][1])<<"\n";
}