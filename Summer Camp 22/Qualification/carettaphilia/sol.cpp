#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
 
int mod = 1e9 + 7;
 
inline void sum_self(int& a, int b) {a += b;if (a >= mod) a -= mod;if (a < 0) a += mod;}
inline void mul_self(int& a, int b) { a = 1ll * a * b % mod; }
inline int mul(int a, int b) {a = 1ll * a * b % mod;return a;}
inline int exp(ll b, ll p) {if (p < 0) return 0;b %= mod;int res = 1;int mul = b;while (p) {if (p & 1) mul_self(res, mul);p >>= 1;mul_self(mul, mul);}return res;}
inline int invexp(ll b) { return exp(b, mod - 2); }  // 1/i modulo mod
 
const int N = 2e5 + 5;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
    int n, m; cin>>n>>m;
    vector<bool> is_prime(m+1, 1);          //  self-explanatory
    vector<bool> is_prime_power(m+1, 0);    // is i a prime power (p ^ e where p is a prime)?
    is_prime[0] = is_prime[1] = 0;          // these two aren't primes
    // Eratosthenes' Sieve for marking primes and prime powers
    for(int i = 2; i <= m; i++){
        // if i is not a prime, skip it
        if(!is_prime[i]) continue;

        // mark i^2, i^2 + i, i^2 + 2i... as non-prime
        for(ll k = 1ll*i*i; k <= m; k += i){
            is_prime[k] = 0;
        }

        // mark i, i^2, i^3... as prime power
        for(ll k = i; k <= m; k *= i){
            is_prime_power[k] = 1;
        }
    }
    int factorial[m+1];         //          factorial[i] = i!       modulo 10^9 + 7
    int inverse_factorial[m+1]; //  inverse_factorial[i] = (1 / i!) modulo 10^9 + 7
    factorial[0] = 1; // 0! = 1
    for(int i = 1; i <= m; i++){
        // mul is my function for calculating product modulo 10^9 + 7
        factorial[i] = mul(factorial[i-1], i);
    }
    // invexp(a) calculates 1/a modulo 10^9 + 7 (equivalent to a^(10^9 + 5))
    inverse_factorial[m] = invexp(factorial[m]);
    /**
     * Here, we compute the inverse factorials in O(n)
     * instead of using invexp everytime (leading to O(n * logn) in total).
     * We use the fact that 1 / i! = (i+1) / (i+1)! (mod 10^9 + 7)
     * 
     * You can also compute each inverse factorial with invexp!
     */
    for(int i = m-1; i >= 0; i--){
        inverse_factorial[i] = mul(inverse_factorial[i+1], i+1);
    }

    // Calculates C(n, k) a.k.a. n CHOOSE k
    // This is a lambda function
    auto C = [&](int n, int k){
        return mul(factorial[n], mul(inverse_factorial[k], inverse_factorial[n-k]));
    };
    int ans = 0;
    for(int i = 1; i <= m; i++){
        // For each odd prime power p^e, add C(m, p^e) to the answer.
        if(!is_prime_power[i] || i % 2 == 0) continue;
        sum_self(ans, C(m, i));
    }
    cout<<ans<<"\n";
}