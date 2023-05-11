#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define FOR(i, n) for(int i = 0; i < (n); i++)
typedef long long ll;

/**
 * To check if a*b exceeds c (a*b > c) where a and b are nonnegative integers,
 * you can check if a > floor(c/b).
 * Because if a > floor(c/b),
 * then it is also true that a > c/b (and thus a*b > c)
 * since a is an integer.
*/
bool is_ovf(ll a, ll b, ll c){
    // a == 0 or b == 0 (edge case)
    if(!a || !b) return c < 0;
    return a > c / b; // it is already floor(c/b) in C++.
}
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
    ll n; cin>>n;
    int p[11], m[11];
    vector<int> portions[11]; // Portion sequences of the people
    vector<ll> sum_till[11]; // Prefix sum array of portions[i]
    /*
        Notice that the sequence:
            p % m, p * i % m, p * i^2 % m...
        starts to repeat after a while.
    */
    int repetition_start[11]; // repeated sequence of the i-th person starts at repetition_start[i]
    FOR(i, 11){
        cin>>p[i]>>m[i];
        // 1- Fill the portions[i] sequence. Stop when it starts to repeat.
        int cur = p[i] % m[i];
        vector<bool> vis(m[i]); // vis[x] = x is visited
        vector<int> pos(m[i]);  // pos[x] = position of x in the portions[i] sequence
        /*
            Until it starts to repeat, fill portions[i].
            Whenever a value appears for the second time (some value will reappear definitely),
            the sequence starts to repeat.
            Here's why:
                In the sequence, every number is a nonnegative integer less than m[i].
                Since this sequence is infinite, some values will appear several times.
                (It can be proved by the pigeonhole principle.)
                Call the first value that appears for the second time "x".
                A part of the sequence will look like this:
                    x, a1, a2, a3, ..., y, x, (?)
                What do you think will be the rest of of the sequence?
                Since x * i % m == a1, a1 will reappear right after x,
                and since a1 * i % m == a2, a2 will reappear right after a1,
                and so on.
                Thus, the sequence will actually repeat itself starting from x:
                    x, a1, a2, a3, ..., y,
                    x, a1, a2, a3, ...., y,
                    x, ...
        */
        while(!vis[cur]){
            vis[cur] = 1;
            pos[cur] = portions[i].size(); // find the position of the value "cur"
            portions[i].pb(cur);
            cur = cur * (i+1) % m[i];
        }
        // Repetition starts at the position of the first reappearing value
        repetition_start[i] = pos[cur];
        // Calculate the prefix sum array sum_till[i]
        sum_till[i].pb(0);
        for(int x: portions[i]){
            sum_till[i].pb(sum_till[i].back() + x);
        }
    }
    // Now, binary search on the number of days
    ll lo = 0, hi = n + 1;
    while(lo < hi){
        ll mid = (lo + hi + 1) / 2;
        ll portions_left = n;
        FOR(i, 11){
            ll n_portions = portions[i].size();
            ll days_left = mid;
            /*
                First, process the whole portions[i] sequence
                to start dealing with the repeating part.
            */
            /*
                If the last value in the sequence is 0,
                only 0 continues to appear.
                So, there is no need for repeated part calculation.
            */
            if(portions[i].back() == 0 || days_left <= n_portions){
                portions_left -= sum_till[i][min(days_left, n_portions)];
                continue;
            }
            days_left -= n_portions;
            portions_left -= sum_till[i][n_portions];

            /*
                Now is the time to deal with the repeating part.
            */
            int repeat_length = n_portions - repetition_start[i];  // The length of the repeating part
            ll n_repeats = days_left / repeat_length;              // The number of times the repeating part appears in the remaining days
            int remaining_length = days_left % repeat_length;      // The number of remaining days
            ll sum_until_start = sum_till[i][repetition_start[i]]; // The sum of values until the repeating part
            ll whole_sum = sum_till[i].back();                     // Equivalent to sum_till[i][n_portions]
            ll repeating_sum = whole_sum - sum_until_start;        // The sum of the repeating part
            /*
                Think about the case where
                    repeat_length is 1
                    repeating_sum is something close to 10^5
                    n_repeats is 10^18 (N / repeat_length)
                there can be lots of similar cases.
                To prevent any overflow, this is necessary.
                
                Actually, the higher bound of binary search
                can be lowered down to not deal with this,
                but I think it might require some boring calculations.
            */
            if(is_ovf(n_repeats, repeating_sum, portions_left)){
                portions_left = -1;
                break;
            }
            // 1. Subtract the repeating part
            portions_left -= n_repeats * repeating_sum;
            // 2. Subtract the remaining part
            portions_left -= sum_till[i][repetition_start[i]  + remaining_length] - sum_until_start;
        }
        if(portions_left < 0) hi = mid-1;
        else lo = mid;
    }
    /*
        If the maximum number of days is greater than n, the answer is not finite.
        Because if at least one person will eat positive number of portions
        in the first n days, the number of portions eaten will be at least n.
        So, if the answer can be n+1, that means in the (n+1)-th day, no one will eat any Acuka.
        In later days, everyone will continue not eating, thus the trip can last infinitely.
    */
    if(lo == n + 1) lo = -1;
    cout<<lo<<"\n";
}