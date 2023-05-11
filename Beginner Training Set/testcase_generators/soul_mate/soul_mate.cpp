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
	set<int> s;
	ofstream ns("ns.txt");
	for(int x = 0; x < 1; x++){
		string input = "input/input" + to_string(100) + ".txt";
		string output = "output/output" + to_string(100) + ".txt";
		ofstream in(input);
		ofstream out(output);
		int n = 5e5, P = 1e9;
		in<<n<<" "<<P<<"\r\n";
		set<int> st;
		for(int i = 0; i < n; i++){
			int cur = gen(2e9) - 1e9;
			int soulmate = (P - (cur%P + P) % P) % P;
			while(st.count(soulmate)){
				cur = gen(2e9) - 1e9;
				soulmate = (P - (cur%P + P) % P) % P;
			}
			st.insert(cur);
			in<<cur<<" ";
		}
		out<<"No";
		/*int n, P;
		if(x < 15){
			n = gen(1e4, 5e5);
			P = gen(1e7, 1e9);
			while(s.count(n)) n = gen(1e4, 5e5);
			s.insert(n);
		}else{
			n = gen(2, 1e4);
			P = gen(1e9);
			while(s.count(n)) n = gen(2, 1e4);
			s.insert(n);
		}
		if(x == 15 && !s.count(5e5)) n = 5e5;
		in<<n<<" "<<P<<"\r\n";
		ns<<n<<" "<<P<<"\r\n";
		
		vector<int> a(n);
		FOR(i, n) a[i] = gen(P-1);
		if(gen(5) == 0){
			int mate1 = gen(n-1);
			int mate2 = gen(n-1);
			while(mate2 == mate1) mate2 = gen(n-1);
			a[mate2] = (P - a[mate1]) % P;
		}
		map<int, bool> exists;
		bool yes = false;
		FOR(i, n){
			int bound = gen(1e8, 1e9);
			int op = gen(2);
			if(op == 0){
				while(a[i] + P <= bound) a[i] += P;
			}else if(op == 1){
				while(a[i] - P >= -bound) a[i] -= P;
			}
			in<<a[i]<<" ";
			int md = (a[i]%P + P) % P;
			if(exists.count((P - md) % P)) yes = true;
			exists[md] = true;
		}
		out<<(yes ? "Yes" : "No");*/
		in.close(), out.close();
	}
	ns.close();
}