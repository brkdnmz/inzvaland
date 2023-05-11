#include <bits/stdc++.h>
using namespace std;

#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define REVERSE(v) reverse((v).begin(), (v).end())
#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))
#define pb push_back
#define FOR(i, n) for (int i = 0; i < (n); i++)
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

int mod = 1e9 + 7;
// int mod = 998244353;

inline void sum_self(int& a, int b) {
    a += b;
    if (a >= mod) a -= mod;
    if (a < 0) a += mod;
}
inline int sum(int a, int b) {
    a += b;
    if (a >= mod) a -= mod;
    if (a < 0) a += mod;
    return a;
}
inline void mul_self(int& a, int b) { a = 1ll * a * b % mod; }
inline int mul(int a, int b) {
    a = 1ll * a * b % mod;
    return a;
}
inline int exp(ll b, ll p) {
    if (p < 0) return 0;
    b %= mod;
    int res = 1;
    int mul = b;
    while (p) {
        if (p & 1) mul_self(res, mul);
        p >>= 1;
        mul_self(mul, mul);
    }
    return res;
}
inline int invexp(ll b) { return exp(b, mod - 2); }  // 1/i modulo mod
template <typename T>
inline void max_self(T& a, T b) {
    a = max(a, b);
}
template <typename T>
inline void min_self(T& a, T b) {
    a = min(a, b);
}

const int N = 1e6 + 5;
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
	int n; cin>>n;
    int a[n];
    FOR(i, n){
        cin>>a[i];
    }
    vector<vector<int>> dp(n, vector<int>(n+1, 1));
    FOR(i, n){
        int cur_sum = a[i];
        for(int j = i-1; j >= 0; j--){
            for(int cnt = 2; cnt <= i+1; cnt++){
                dp[i][cnt] = max(dp[i][cnt], __gcd(cur_sum, dp[j][cnt-1]));
            }
            cur_sum += a[j];
        }
        dp[i][1] = cur_sum;
    }
    for(int k = n; k >= 1; k--){
        if(dp[n-1][k] > 1){
            cout<<k<<"\n";
            return 0;
        }
    }
}