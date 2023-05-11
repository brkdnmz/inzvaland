#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int a, b;
        cin >> a >> b;
        /*
            Solution 1
            ----------
            After a+k < 2*(b+k), there will definitely be no integers, because every element will be in the range (1, 2).

            a+k < 2b + 2k -> k > a - 2b
            a - 2b < 10**6
            We can iterate over k's.

            Solution 2
            ----------
            Notice that (a+k) / (b+k) == (a - b) / (b + k) + 1,
            where a-b is constant for every element.

            Just iterate over integers from b to abs(a-b), and check if the current integer divides a - b.

            Edge Case
            ---------
            If a == b, then every element is an integer.
        */
        a -= b;
        int cnt = 0;
        for (int i = b; i <= abs(a); i++)
        {
            cnt += a % i == 0;
        }
        if (!a)
            cnt = -1;
        cout << cnt << "\n";
    }
}