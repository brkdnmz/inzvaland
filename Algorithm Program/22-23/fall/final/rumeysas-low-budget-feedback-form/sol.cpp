#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<ll> dp;
vector<int> initial_exponents;

int get_index(vector<int> &exponents) {
    int index = 0;
    for (int i = 0; i < exponents.size(); i++) {
        index = index * (initial_exponents[i] + 1) + exponents[i];
    }
    return index;
}

ll solve(vector<int> &); // forward declarated for cross function calls

/*
 For a set of prime exponents [e1, e2, ..., ek],
 This iterates over all possible [e1', e2', ..., ek']
 where ei' <= ei.

 A concrete example where recursion beats the hell out of iteration :D
*/
ll solve_for_divisors(vector<int> &exponents, int index = 0, bool is_itself = true, bool is_one = true) {
    if (index == exponents.size()) {
        if (is_one)
            return 1;
        if (is_itself)
            return 0;
        return solve(exponents);
    }
    int cur_exponent = exponents[index];
    ll ans = 0;
    for (int i = 0; i <= cur_exponent; i++) {
        exponents[index] = i;
        ans += solve_for_divisors(exponents, index + 1, is_itself && i == cur_exponent, is_one && !i);
    }
    return ans;
}

ll solve(vector<int> &exponents) {
    ll &ans = dp[get_index(exponents)];
    if (ans)
        return ans;
    return ans = solve_for_divisors(exponents);
}

int main() {
    ll n;
    cin >> n;
    int n_divisors = 1;
    for (int i = 2; 1ll * i * i <= n; i++) {
        if (n % i)
            continue;
        int exp = 0;
        while (n % i == 0)
            n /= i, exp++;
        n_divisors *= exp + 1;
        initial_exponents.push_back(exp);
    }
    if (n > 1) {
        initial_exponents.push_back(1);
        n_divisors *= 2;
    }
    auto exponents = initial_exponents;
    dp.assign(n_divisors, 0);
    cout << solve(exponents) << "\n";
}