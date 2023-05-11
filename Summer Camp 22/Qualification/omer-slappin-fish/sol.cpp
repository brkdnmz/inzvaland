#include "bits/stdc++.h"
#define MAXN 100009
#define INF 1000000007
#define mp(x,y) make_pair(x,y)
#define all(v) v.begin(),v.end()
#define pb(x) push_back(x)
#define wr cout<<"----------------"<<endl;
#define ppb() pop_back()
#define tr(ii,c) for(__typeof((c).begin()) ii=(c).begin();ii!=(c).end();ii++)
#define ff first
#define ss second
#define my_little_dodge 46
#define debug(x)  cerr<< #x <<" = "<< x<<endl;
using namespace std;
 
typedef long long ll;
typedef pair<int,int> PII;
template<class T>bool umin(T& a,T b){if(a>b){a=b;return 1;}return 0;}
template<class T>bool umax(T& a,T b){if(a<b){a=b;return 1;}return 0;}
int dx[]={+1,-1,0,0};
int dy[]={0,0,+1,-1};
int main(){
    //~ freopen("file.in", "r", stdin);
    int n,m;
    scanf("%d%d",&n,&m);
    assert(1<=n and 1<=m and n*1LL*m<=1000000);
    vector<vector<char> >s(n+1, vector<char>(m+1));
    vector<vector<int> >F(n+1, vector<int>(m+1));
    vector<vector<int> >O(n+1, vector<int>(m+1));
    vector<vector<int> >dp(n+1, vector<int>(m+1));
    for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			scanf(" %c",&s[i][j]), assert(s[i][j]=='~' or s[i][j]=='F');
	queue<PII>q;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++){
			F[i][j]=O[i][j]=INF;
			if(s[i][j]=='F')
				q.push(mp(i,j)),F[i][j]=0;
		}
	while(!q.empty()){
		int nx=q.front().ff;
		int ny=q.front().ss;
		q.pop();
		for(int i=0;i<4;i++){
			int tox=nx+dx[i];
			int toy=ny+dy[i];
			if(tox>=1 and toy>=1 and tox<=n and toy<=m and umin(F[tox][toy],F[nx][ny]+1))
				q.push(mp(tox,toy));
		}
	}
	q.push(mp(1,1));
	O[1][1]=0;
	while(!q.empty()){
		int nx=q.front().ff;
		int ny=q.front().ss;
		q.pop();
		for(int i=0;i<4;i++){
			int tox=nx+dx[i];
			int toy=ny+dy[i];
			if(tox>=1 and toy>=1 and tox<=n and toy<=m and umin(O[tox][toy],O[nx][ny]+1))
				q.push(mp(tox,toy));
		}
	}
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++){
			int cost=(F[i][j]<=O[i][j]);
			if(i==1 and j==1)
				dp[i][j]=cost;
			else if(i==1)
				dp[i][j]=dp[i][j-1]+cost;
			else if(j==1)
				dp[i][j]=dp[i-1][j]+cost;
			else
				dp[i][j]=min(dp[i][j-1],dp[i-1][j])+cost;
		}
	printf("%d\n",dp[n][m]);
	return 0;
}