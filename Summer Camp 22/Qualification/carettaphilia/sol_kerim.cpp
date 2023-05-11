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
const int N=1e6+3;
int vis[N],good[N];
int fac[N],inv[N];
int mod(ll x){
	return (x%INF);
}
int Fe(int x,int y){
	if(!y)return 1;
	int h=Fe(x,y/2);
	h=mod(h*1LL*h);
	if(y&1)
		h=mod(h*1LL*x);
	return h;
}
int C(int x,int y){
	return mod(fac[x]*1LL*mod(inv[y]*1LL*inv[x-y]));
}
int main(){
    //~ freopen("file.in", "r", stdin);
    int n,m,ans=0;
    scanf("%d%d",&n,&m);
    inv[0]=fac[0]=1;
    for(int i=1;i<=m;i++){
		fac[i]=mod(fac[i-1]*1LL*i);
		inv[i]=Fe(fac[i],INF-2);
	}
    assert(1<=n and n<=1000000000);
    assert(1<=m and m<=1000000 and m<=n);
    for(int i=2;i<N;i++){
		if(vis[i])continue;
		if(i>2){
			ll x=i;
			while(x<N){
				good[x]=1;
				x*=i;
			}
		}
		for(int j=i;j<N;j+=i)
			vis[j]=1;
	}
	for(int i=1;i<=m;i++)
		if(good[i])
			ans=mod(ans+C(m,i));
	printf("%d\n",ans);
	return 0;
}