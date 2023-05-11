#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef uniform_int_distribution<ll> rnd;
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define REVERSE(v) reverse((v).begin(), (v).end())
#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))
#define pb push_back
#define FOR(i, n) for(int i = 0; i < (n); i++)
typedef pair<int, int> pii;
typedef long long ll;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
template<typename T>
T gen(T l, T r){
	return rnd(l, r)(rng);
}
template<typename T>
T gen(T r){
	return rnd(1, r)(rng);
}
template<typename T>
T gen0(T r){
    return rnd(0, r)(rng);
}

int main(){
    for(int tc = 0; tc < 1; tc++){
        ofstream input("input/input" + to_string(tc) + ".txt");
        ofstream output("output/output" + to_string(tc) + ".txt");
        /*
            n - i^2
            -------
            i + a

            n + ia
            ------
            i + a

            n - a^2
            -------
            i + a
        */
        
        int n = 1e6;
        int a = 1e3;
        int numerator = abs(n - a*a);
        int res = 0;
        for(int i = 1; i <= numerator; i++){
            if(numerator % i == 0) res += 2;
        }
        if(numerator == 0) res = -1;

        input << n << " " << a;
        output << res;
    }
}