#include <bits/stdc++.h>
using namespace std;

int divs(int x)
{
    int ret = 0;
    for (int i = 1; i * i <= x; i++)
    {
        if (x % i)
            continue;
        ret++;             // i is a divisor
        ret += i * i != x; // x/i is also a divisor but check if i != x/i
    }
    return 2 * ret; // count the negatives also (not necessary but consistent)
}

int main()
{
    int n;
    cin >> n;
    int ans = n;
    for (int x = 1; x <= n; x++)
    {
        int sum = x * (x + 1) / 2;
        ans -= divs(x) == divs(sum);
    }
    cout << ans << "\n";
}