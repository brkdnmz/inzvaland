#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Always keep the smaller one be y (or x) for simpler coding!

ll iterative_gcd(ll x, ll y) {
    // While both are non-zero, perform larger = larger % smaller
    while (x > 0 && y > 0) {
        if (x >= y)
            x %= y;
        else
            y %= x;
    }

    // Afterward, the non-zero one is the GCD!
    // if(x > 0){
    //     return x;
    // }
    // return y;
    return (x ? x : y);
}

ll iterative_gcd_v2(ll x, ll y) {
    // While y is non-zero, perform (x, y) = (y, x % y)
    while (y > 0) {
        ll tmp = y;
        y = x % y;
        x = tmp;
    }

    // After y becomes 0, x is the GCD!
    return x;
}

ll recursive_gcd(ll x, ll y) {
    if (y == 0)
        return x;
    return recursive_gcd(y, x % y);
}

// Observe the similarity between min and gcd

ll min_of_many(vector<ll> &integers) {
    // Assume at least one element exists, or use LLONG_MAX as the initial value
    ll overall_min = integers[0];
    for (ll &i : integers) {
        overall_min = min(overall_min, i);
    }
    return overall_min;
}

ll gcd_of_many(vector<ll> &integers) {
    ll overall_gcd = 0;
    for (ll &i : integers) {
        overall_gcd = __gcd(overall_gcd, i);
    }
    return overall_gcd;
}

// Observe the similarity between max and lcm

ll max_of_many(vector<ll> &integers) {
    // Assume at least one element exists, or use LLONG_MIN as the initial value
    ll overall_max = integers[0];
    for (ll &i : integers) {
        overall_max = max(overall_max, i);
    }
    return overall_max;
}

ll lcm_of_many(vector<ll> &integers) {
    ll overall_lcm = 1; // Notice that 1 the minimum initial value for max'ing (all exps are zero)
    for (ll &i : integers) {
        // Notice how we first divided, then multiplied
        // It's just to prevent overflow!
        overall_lcm = overall_lcm / __gcd(overall_lcm, i) * i;
    }
    return overall_lcm;
}

int main() {
    ll x = 2584;
    ll y = 8362;

    ll iterative = iterative_gcd(x, y);
    ll iterative_v2 = iterative_gcd_v2(x, y);
    ll recursive = recursive_gcd(x, y);
    ll builtin = __gcd(x, y);
    cout << iterative << " " << iterative_v2 << " " << recursive << " " << builtin << "\n";
}
