#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
    ll n; cin>>n;
    int r[11];
    /*
        sum_till[i][d] = a_i1 + a_i2 + ... + a_id
        a.k.a. prefix sum array
        int is enough, no need for long long

        Actually, prefix sum array is not needed but
        we can use it anyway
    */
    vector<int> sum_till[11];
    for(int i = 0; i < 11; i++){
        cin>>r[i];
        // Allocate r[i] ints and initialize to 0
        sum_till[i].resize(r[i]+1);
        // Equivalently: sum_till[i] = vector<int>(r[i]+1, 0);
        for(int j = 1; j <= r[i]; j++){
            int portion; cin>>portion;
            sum_till[i][j] = sum_till[i][j-1] + portion;
        }
    }
    // Binary search over the number of days
    /*
        The minimum possible number of days is 0,
        and the maximum is definitely less than n.
    */
    ll lo = 0, hi = n;
    while(lo < hi){
        /*
            (Call d "mid")
            The type of binary search is:
                Assign mid-1 to hi when failure,
                assign mid to lo when success.

            This is why when finding mid,
            we add 1 to the numerator.
            (Think about what happens when lo = hi - 1)
        */
        ll d = (lo + hi + 1) / 2;
        ll p_left = n; // portions left
        for(int i = 0; i < 11; i++){
            ll n_repetitions = d / r[i];
            int n_remaining = d % r[i];
            p_left -= n_repetitions * sum_till[i][r[i]] + sum_till[i][n_remaining];
        }
        if(p_left < 0){
            hi = d - 1;
        }else{
            lo = d;
        }
    }
    cout<<lo<<"\n";
}