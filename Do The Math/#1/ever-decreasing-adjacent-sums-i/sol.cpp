#include <bits/stdc++.h>

using namespace std;

int main()
{
    int l, r;
    cin >> l >> r;
    int ans[15] = {};
    for (; l <= r; l++)
    {
        for (int div = 2; div <= 16 && (l - 1) % div == 0; div++)
        {
            ans[div - 2]++;
        }
    }
    for (int i = 0; i < 15; i++)
        cout << ans[i] << " ";
}