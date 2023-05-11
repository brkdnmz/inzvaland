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
	for(int x = 0; x < 100; x++){
		string input = "input/input" + to_string(x) + ".txt";
		string output = "output/output" + to_string(x) + ".txt";
		ofstream in(input);
		ofstream out(output);
		int n;
		if(x < 80){
			n = gen(50, 100);
		}else{
			n = gen(4, 50);
		}
		string s;
		FOR(i, n){
			s += gen(0, 25) + 'a';
		}
		in<<n<<"\r\n"<<s<<"\r\n";
		in.close();
		map<string, int> cnt;
		cnt[""] = 1;
		for(int i = 0; i < n; i++){
			vector<pair<string, int>> update;
			for(auto& x: cnt){
				string ss = x.first;
				if(ss.size() == 4) continue;
				ss += s[i];
				update.pb({ss, x.second});
			}
			for(auto& x: update){
				cnt[x.first] += x.second;
			}
		}
		int ans = 0;
		for(auto& x: cnt) if(x.first.size() == 4) ans = max(ans, x.second);
		out<<ans<<"\r\n";
		out.close();
	}
}