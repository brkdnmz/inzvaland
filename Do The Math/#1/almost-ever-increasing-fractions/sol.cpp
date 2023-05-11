#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll a, b;
        cin >> a >> b;
        ll sum = a + b;
        int ans = 0;
        for (int i = 1; 1ll * i * i <= sum; i++)
        {
            if (sum % i)
                continue;
            ll other = sum / i;
            ans += i <= b;
            ans++; // -i
            if (other != i)
            {
                ans += other <= b;
                ans++; // -other
            }
        }
        cout << ans << "\n";
    }
}