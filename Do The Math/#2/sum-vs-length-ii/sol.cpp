#include <bits/stdc++.h>
using namespace std;

bool p(int x)
{
    for (int i = 2; i * i <= x; i++)
    {
        if (x % i == 0)
            return false;
    }
    return true;
}

int main()
{
    int n;
    cin >> n;
    int ans = n - 1; // -1 is for x = 1
    for (int x = 2; x <= n; x += 4)
    {
        ans -= p(x + 1);
    }
    cout << ans << "\n";
}