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
int m[100][100];
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
	ll n; cin>>n;
    int a[100];
    FOR(i, 100) cin>>a[i];
    FOR(i, 100) m[0][i] = a[i];
    FOR(i, 99){
        m[i+1][i] = 1;
    }
    int cur[100] = {};
    cur[0] = 1;
    while(n){
        if(n & 1){
            int ncur[100] = {};
            FOR(i, 100){
                FOR(j, 100){
                    sum_self(ncur[i], mul(m[i][j], cur[j]));
                }
            }
            FOR(i, 100) cur[i] = ncur[i];
        }
        n >>= 1;
        int nm[100][100] = {};
        FOR(i, 100){
            FOR(j, 100){
                FOR(k, 100){
                    sum_self(nm[i][j], mul(m[i][k], m[k][j]));
                }
            }
        }
        FOR(i, 100) FOR(j, 100) m[i][j] = nm[i][j];
    }
    cout<<cur[0]<<"\n";
}