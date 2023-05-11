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
ll gen(ll l, ll r){
	return rnd(l, r)(rng);
}
ll gen(ll r){
	return rnd(1, r)(rng);
}
int main(){
	set<int> s;
	const int N = 1e6;
	vector<ll> dp(N+1, 0);
	dp[1] = 1;
	for(int p = 1; p <= N; p++){
		for(int np = 2*p; np <= N; np += p){
			dp[np] += dp[p];
		}
	}
	cout<<dp[N]<<"\n";
	return 0;
	ofstream ns("ns.txt");
	for(int x = 0; x < 100; x++){
		string input = "input/input" + to_string(x) + ".txt";
		string output = "output/output" + to_string(x) + ".txt";
		ofstream in(input);
		ofstream out(output);
		int n;
		if(x < 80){
			n = gen(1e3+1, 1e6);
			while(s.count(n)) n = gen(1e3+1, 1e6);
			s.insert(n);
		}else{
			n = gen(1e3);
			while(s.count(n)) n = gen(1e3);
			s.insert(n);
		}
		if(x == 80 && !s.count(967680)) n = 967680;
		in<<n<<"\r\n";
		ns<<n<<"\r\n";
		out<<dp[n]<<"\r\n";
		in.close(), out.close();
	}
	ns.close();
}