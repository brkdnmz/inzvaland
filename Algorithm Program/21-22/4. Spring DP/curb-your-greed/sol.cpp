#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin>>n;
    int g[n][n];
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) cin>>g[i][j];
    int M = 1<<n;
    vector<long long> dp(M, -1e18);
    dp[0] = 0;
    for(int i = 0; i < n; i++){
        for(int m = 0; m < M; m++){
            int cnt = 0;
            for(int j = 0; j < n; j++) cnt += (m & 1<<j) > 0;
            if(cnt != i-1) continue;
            for(int j = 0; j < n; j++){
                if(m & 1<<j) continue;
                dp[m | 1<<j] = max(dp[m | 1<<j], dp[m] + g[i][j]);
            }
        }
    }
    cout<<dp[M-1]<<"\n";
}