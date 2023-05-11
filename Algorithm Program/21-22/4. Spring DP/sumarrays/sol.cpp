#include <bits/stdc++.h>
using namespace std;

#define FOR(i, n) for (int i = 0; i < (n); i++)
typedef long long ll;

const int N = 1e5 + 5;

vector<ll> a(N);
ll solve(int l, int r, ll min_sum){
    if(l == r) return 0;
    int mid = (l+r)/2;
    ll ans = solve(l, mid, min_sum) + solve(mid+1, r, min_sum);
    int p1 = l;
    int p2 = mid+1;
    for(; p2 <= r; p2++){
        while(p1 <= mid && a[p2] - a[p1] >= min_sum){
            ans += r-p2+1;
            p1++;
        }
    }
    p1 = l;
    p2 = mid+1;
    ll new_a[r-l+1];
    int ptr = 0;
    while(p1 <= mid || p2 <= r){
        if(p1 > mid) new_a[ptr] = a[p2], p2++;
        else if(p2 > r) new_a[ptr] = a[p1], p1++;
        else if(a[p1] <= a[p2]) new_a[ptr] = a[p1], p1++;
        else new_a[ptr] = a[p2], p2++;
        ptr++;
    }
    for(int i = l; i <= r; i++) a[i] = new_a[i-l];
    return ans;
}
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    // https://leetcode.com/problems/count-of-range-sum/
    int n; ll k;
    cin>>n>>k;
    FOR(i, n) cin>> a[i+1], a[i+1] += a[i];
    ll l = -1e18, r = 1e18;
    while(l < r){
        ll mid = (l+r+1)/2;
        auto aa = a;
        if(solve(0, n, mid) >= k){
            l = mid;
        }else{
            r = mid-1;
        }
        a = aa;
    }
    cout<<l<<"\n";
}