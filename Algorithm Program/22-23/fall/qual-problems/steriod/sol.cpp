#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e3 + 7, N_CHARS = 23;

int main()
{
    int n, m;
    cin >> n >> m;
    int ans = 0;
    if (n % m == 0)
    {
        ans = 1;
        while (m--)
        {
            // ans < MOD and N_CHARS = 23.
            // The operation ans * N_CHARS cannot overflow, so it's safe.
            ans = ans * N_CHARS % MOD;
        }
    }
    cout << ans << "\n";
}