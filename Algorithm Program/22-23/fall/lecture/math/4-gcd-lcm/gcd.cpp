// https://ideone.com/MZLH0V
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll gcd(ll a, ll b) {
    // always assign a = a % b for convenience
    if (a < b)
        swap(a, b); // built-in function

    while (b) { // while b is non-zero, continue the process
        a %= b;
        swap(a, b);
    }
    // at the end, a will be the GCD!
    return a;
}

ll gcd_recursive(ll a, ll b) {
    if (a < b)
        swap(a, b);
    if (!b)
        return a;
    return gcd_recursive(a % b, b);
}

// You don't need to swap yourself. This is an alternative version.
ll gcd_recursive_alt(ll a, ll b) {
    if (!a) // a will eventually become zero.
        return b;
    // First, change the parameters' location,
    // then apply modulo. This is totally the same.
    return gcd_recursive_alt(b % a, a);
}

int main() {
    ll a = 152348643862835682ll;
    ll b = 4236438563286243ll;
    cout << "GCD (iterative):\t" << gcd(a, b) << "\n";
    cout << "GCD (recursive):\t" << gcd_recursive(a, b) << "\n";
    cout << "GCD (recursive v2):\t" << gcd_recursive_alt(a, b) << "\n";

    // Guess what? There is a  built-in GCD function!
    cout << "GCD (built-in):\t\t" << __gcd(a, b) << "\n";
}