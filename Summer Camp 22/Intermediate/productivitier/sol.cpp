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

const int N = 1e6 + 5;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
    int n; cin>>n;
    vector<int> sm(N);
    for(int i = 2; i < N; i++){
        if(sm[i]) continue;
        for(int k = i; k < N; k += i) sm[k] = i;
    }
    vector<vector<int>> exps(N);
    FOR(i, n){
        int x; cin>>x;
        while(x > 1){
            int cnt = 0;
            int p = sm[x];
            for(; x % p == 0; x /= p, cnt++){};
            exps[p].pb(cnt);
        }
    }
    int ans = 1;
    FOR(i, N){
        auto& v = exps[i];
        if(n - v.size() > 1) continue;
        SORT(v);
        if(n - v.size() == 1){
            FOR(_, v[0])
                ans *= i;
        }
        else{
            FOR(_, v[1])
                ans *= i;
        }
    }
    cout<<ans<<"\n";
}