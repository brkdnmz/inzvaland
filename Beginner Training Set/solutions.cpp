DP
1-
vector<int> dp(K+1, 0);
dp[0] = 1;
//or dp[n][K+1]
for(int i = 1; i < n; i++){
	vector<int> ndp = dp;
	for(int j = 0; j <= K; j++){
		ndp[j] = dp[j];
		if(j) ndp[j] += dp[j-1];
		if(ndp[j] >= mod) ndp[j] -= mod;
	}
	dp = ndp;
}
n*K

2-
vector<int> dp(n, 0);
dp[0] = 1;
for(int i = 1; i < n; i++){
	vector<int> ndp = dp;
	int sum = dp[0];
	for(int j = 1; j < i; j++){
		ndp[j] = dp[j] + sum;
		sum += ndp[j];
		//ndp[j] == dp[0] + dp[1] + ... + dp[j]
		if(ndp[j] >= mod) ndp[j] -= mod;
	}
}
~n^2

3-
int sum = n*(n+1)/2;
if(sum & 1){
	return 0;
}

vector<int> dp(sum/2 + 1, 0);
dp[0] = 1;
for(int i = 1; i <= n; i++){
	for(int j = sum/2-i; j >= 0; j--){
		dp[j+i] += dp[j];
		if(dp[j+i] >= mod) dp[j+i] -= mod;
	}
}
n*n*(n+1)/4 operations, good for n = 1e3

4-
vector<int> dp(n+1);
dp[0] = 1;
int ans = 0;
for(int cnt = 1; cnt <= n; cnt++){
	vector<int> ndp(n+1, 0);
	for(int i = 1; i <= n; i++){
		for(int sum = n-i; sum >= 0; sum--){
			ndp[sum+i] += dp[sum];
			if(ndp[sum+i] >= mod) ndp[sum+i] -= mod;
		}
	}
	dp = ndp;
	ans += dp[n];
	if(ans >= mod) ans -= mod;
}

OR
ans = 2**n

n* n*(n+1)/2 operations, OK for n = 1e3

5-
int cnt = n/2;
if(n & 1){
	return 0;
}
vector<vector<int>> dp(cnt+1, vector<int>(cnt+1, 0));
dp[0][0] = 1;
for(int opened = 1; opened <= cnt; opened++){
	for(int closed = 0; closed <= opened; closed++){
		dp[opened][closed] = dp[opened-1][closed];
		if(closed) dp[opened][closed] += dp[opened][closed-1];
	}
}
cout<<dp[cnt][cnt]<<"\n";
(n/2)^2

6-
int dp[N+1];
dp[0] = 0;
for(int i = 1; i <= N; i++){
	for(int ai: a){
		if(ai <= i) dp[i] = min(dp[i], dp[i-ai]+1);
		if(i%ai == 0) dp[i] = min(dp[i], dp[i/ai]+1);
	}
	dp[i] = min(dp[i], dp[i-1]+1);
}
n*N

STL
1-
multiset<int> small, big;
for(int i = 0; i < n; i++){
	small.insert(a[i]);
	while(*small.rbegin() > *big.begin()){
		big.insert(*small.rbegin());
		small.erase(small.end()-1);
	}
	while(small.size() - big.size() > 1){
		big.insert(*small.rbegin());
		small.erase(small.end()-1);
	}
	int median = *small.rbegin();
}
n * logn

2-
map<long long, bool> seen;
for(int i = 0; i < n; i++){
	a[i] %= P;
	if(a[i] < 0) a[i] += P;
	if(seen.count(P - a[i])) return true;
	seen[a[i]] = true;
}
n * logn or n for unordered_map

3-
map<string, int> cnt;

if(op == 1) cnt[s]++;
if(op == 2){
	if(!cnt.count(s)) continue;
	cnt[s]--;
	if(cnt[s] == 0) cnt.erase(s);
}
if(op == 3){
	auto target = cnt.lower_bound(s);
	if(target != cnt.end() && s == prefix(*target)){
		print(*target);
	}else print(-1);
}

/*Recursion
1-
int g[15][15];
int nums[15];
bool taken[15];
int n, m;
int N;
bool check(int r, int c){
	if(c && __gcd(g[r][c-1], g[r][c]) > 1) return false;
	if(r && __gcd(g[r-1][c], g[r][c]) > 1) return false;
	return true;
}
ll f(int r = 0, int c = 0){
	if(r == n) return 1;
	ll ret = 0;
	int nr = r, nc = c+1;
	if(nc == m) nr++, nc = 0;
	for(int i = 0; i < N; i++){
		if(taken[i]) continue;
		g[r][c] = nums[i];
		if(!check(r, c)) continue;
		taken[i] = true;
		ret += f(nr, nc);
		taken[i] = false;
	}
	return ret;
}*/

map<string, int> cnt;
for(int i = 0; i < n; i++){
	vector<pair<string, int>> to_be_added;
	for(auto& p: cnt){
		string subs = p.first;
		if(subs.size() == 4) continue;
		to_be_added.pb({subs, p.second});
	}
	for(auto& p: to_be_added){
		cnt[p.first + s[i]] += p.second;
	}
}