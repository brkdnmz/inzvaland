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
    ll sum = 0;
    FOR(i, n) cin>>a[i], sum += a[i];
    ll k = 0;
    for(int div = 2; 1ll*div*div <= sum; div++){
        if(sum%div) continue;
        while(sum%div == 0) sum /= div;
        ll ck = 0, cs = 0;
        FOR(i, n){
            cs += a[i];
            if(cs % div == 0) ck++, cs = 0;
        }
        k = max(k, ck);
    }
    if(sum > 1){
        ll ck = 0, cs = 0;
        FOR(i, n){
            cs += a[i];
            if(cs % sum == 0) ck++, cs = 0;
        }
        k = max(k, ck);
    }
    cout<<sum<<"\n";
    cout<<k<<"\n";
}