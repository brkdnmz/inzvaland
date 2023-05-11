#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        /*
            Solution
            --------
            Instead of corners, think about the edges of the sticker to be extracted:
            - There must not be any indicated pixel on the left of the left edge.
            - There must not be any indicated pixel above the top edge.
            - There must not be any indicated pixel on the right of the right edge.
            - There must not be any indicated pixel below the bottom edge.

            With these constraints, the answer can be found by maintaining the following:
            - Column number of the leftmost indicated pixel: lmost
            - Row number of the topmost indicated pixel: umost
            - Column number of the rightmost indicated pixel: rmost
            - Row number of the bottommost indicated pixel: dmost
        */
        int n, m;
        cin >> n >> m;
        int lmost = m, rmost = 0, umost = n, dmost = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                char c;
                cin >> c;
                if (c == '.')
                    continue;
                lmost = min(lmost, j);
                rmost = max(rmost, j);
                umost = min(umost, i);
                dmost = max(dmost, i);
            }
        }
        long long ans = 0;
        if (lmost < m)
        {
            ans = 1ll * (lmost + 1) * (m - rmost) * (umost + 1) * (n - dmost);
        }
        cout << ans << "\n";
    }
}