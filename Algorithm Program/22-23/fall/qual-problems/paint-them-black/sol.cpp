#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e3 + 7;

int main()
{
    int n, m;
    cin >> n >> m;
    int ans = 1;
    m--;
    while (m--)
        ans = ans * 2 % MOD;
    cout << ans << "\n";
}