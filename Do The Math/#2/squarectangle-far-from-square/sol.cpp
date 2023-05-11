#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int phi(int x)
{
    // Result is initially x.
    // For every prime divisor p of x, multiply the result with (p-1)/p.
    // This is what phi(x) is actually equal to.

    int res = x;
    for (int i = 2; i * i <= x; i++)
    {
        if (x % i)
            continue;
        res /= i, res *= i - 1;
        while (x % i == 0)
            x /= i;
    }

    // This is for the cases where the greatest prime divisor's exponent is 1.
    if (x > 1)
        res /= x, res *= x - 1;
    return res;
}

int main()
{
    int n;
    cin >> n;
    ll ans = 0;
    for (int i = 2; i <= n; i++)
        ans += phi(i);
    cout << ans << "\n";
}