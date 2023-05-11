#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int mod = 1e9 + 7;

inline int sum(int a, int b) {a += b;if (a >= mod) a -= mod;if (a < 0) a += mod;return a;}
inline void sum_self(int& a, int b) {a += b;if (a >= mod) a -= mod;if (a < 0) a += mod;}
inline void mul_self(int& a, int b) { a = 1ll * a * b % mod; }
inline int mul(int a, int b) {a = 1ll * a * b % mod;return a;}
inline int exp(ll b, ll p) {if (p < 0) return 0;b %= mod;int res = 1;int mul = b;while (p) {if (p & 1) mul_self(res, mul);p >>= 1;mul_self(mul, mul);}return res;}
inline int invexp(ll b) { return exp(b, mod - 2); }  // 1/i modulo mod
 
const int N = 1e3 + 5;

// Checks whether given x is a prime power, i.e., can be expressed as p^e where p is prime
bool is_prime_power(int x){
    if(x <= 1) return false;
    for(int i = 2; i <= x; i++){
        // The first divisor that appears is guaranteed to be a prime
        if(x % i == 0){
            while(x % i == 0) x /= i;
            // After extracting all "i"s, x is prime power iff it does not contain any other divisor
            return x == 1;
        }
    }
    return true; // x is a prime itself
}

int C[N][N]; // C[i][j] = i CHOOSE k (binomial coefficient)

/**
 * To precalculate binomial coefficients,
 * use the formula:
 * C(n, k) = C(n-1, k-1) + C(n-1, k)
 * https://en.wikipedia.org/wiki/Binomial_coefficient
 */
void precalc_binomial_coefficients(){
    for(int i = 1; i < N; i++){
        for(int j = 0; j <= i; j++){
            if(j == 0 || j == i) C[i][j] = 1;
            else{
                C[i][j] = sum(C[i-1][j-1], C[i-1][j]);
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
    precalc_binomial_coefficients();
    int n, m; cin>>n>>m;
    int ans = 0;
    // For every odd prime power x, add C(m, x) to the answer
    for(int x = 1; x <= m; x += 2){
        if(!is_prime_power(x)) continue;
        sum_self(ans, C[m][x]);
    }
    cout<<ans<<"\n";
}