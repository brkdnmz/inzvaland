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
	return rnd(0, r)(rng);
}
int main(){
	for(int x = 0; x < 40; x++){
		string input = "do_you_even_lift/input/input" + to_string(x) + ".txt";
		string output = "do_you_even_lift/output/output" + to_string(x) + ".txt";
		ofstream in(input);
		ofstream out(output);
		int n = gen(3, 50);
		if(x >= 10) n = gen(5, 10);
		if(x >= 20) n = gen(50, 100);
		if(x >= 30) n = gen(500, 1000);
		int sum = 1e6/n;
		int W = sum;
		assert(n*sum <= 1e6 && sum >= n);
		vector<int> a(n, 1);
		sum -= n;
		while(sum > 0){
			FOR(i, n){
				if(!sum) break;
				int cur = min(sum, 100);
				if(x >= 10) cur = min(sum, 1000);
				if(x >= 20) cur = min(sum, 70);
				if(x >= 30) cur = min(sum, 4);
				int add = gen(1, cur);
				a[i] += add;
				sum -= add;
			}
		}
		random_shuffle(a.begin(), a.end());
		in<<n<<"\r\n";
		FOR(i, n) in<<a[i]<<" ";
		in<<"\r\n";
		in.close();
		
		vector<bool> can(W+1, 0);
		can[0] = 1;
		for(int i = 0; i < n; i++){
			vector<bool> new_can = can;
			for(int w = 0; w <= W; w++){
				if(!can[w]) continue;
				if(w + a[i] <= W) new_can[w + a[i]] = true;
				new_can[abs(w - a[i])] = true;
			}
			can = new_can;
		}
		int ans = 0;
		for(int w = 1; w <= W; w++) ans += can[w];
		out<<ans<<"\r\n";
		out.close();
	}
}