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
	ofstream write_n("n.txt");
	for(int x = 0; x < 100; x++){
		string input = "input/input" + to_string(x) + ".txt";
		string output = "output/output" + to_string(x) + ".txt";
		ofstream in(input);
		ofstream out(output);
		
		int n;
		if(x < 80){
			n = gen(1000);
			while(s.count(n)) n = gen(1000);
		}else{
			n = gen(40);
			while(s.count(n)) n = gen(40);
		}
		write_n<<n<<"\r\n";
		s.insert(n);
		in<<n<<"\r\n";
		in.close();
		
		int sum = n*(n+1)/2;
		const int mod = 1e9+7;
		if(sum&1){
			out<<0<<"\r\n";
		}else{
			int target = sum/2;
			vector<int> ways(target+1, 0);
			ways[0] = 1;
			for(int i = 1; i <= n; i++){
				for(int w = target-i; w >= 0; w--){
					ways[w+i] += ways[w];
					if(ways[w+i] >= mod) ways[w+i] -= mod;
				}
			}
			out<<ways[target]<<"\r\n";
		}
		out.close();
	}
	write_n<<"\r\n";
	write_n.close();
}