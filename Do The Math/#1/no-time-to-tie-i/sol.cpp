#include <bits/stdc++.h>
using namespace std;

/*
    It can be solved by brute-forcing all combinations:
    There are b buttons, x of which are to be buttoned-up.

    Parameters
    ----------
    orig_b: Initial b.
    orig_x: Initial x.
    b: Number of buttons left.
    x: Number of buttons left to button up.
    last_placed: Whether the previous button has been buttoned up.
    adj: Number of adjacent buttoned-up pairs.

    Base Cases
    ----------
    1- x < 0: More than x buttons are buttoned up.
    2- b < x: There aren't enough buttons left.
    3- b == 0: A combination is finished.
        1- The number of free buttons is greater than or equal to the number of places in between buttoned-up buttons.
           (orig_b - orig_x >= orig_x - 1)
           If this is the case, there must be no adjacent buttoned-up pairs because it is the minimum possible.
        2- Else, we should distribute the free buttons in between buttoned-up buttons.
           Each free button decrements the number of adjacent pairs.
           The minimum possible number of pairs then would be orig_x - 1 - (orig_b - orig_x).
*/
int solve(int orig_b, int orig_x, int b, int x, bool last_placed, int adj = 0)
{
    if (x < 0 || b < x)
        return 0;
    if (!b)
    {
        if (orig_b - orig_x >= orig_x - 1)
            return !adj;
        return adj == orig_x - 1 - (orig_b - orig_x);
    }
    int ans = solve(orig_b, orig_x, b - 1, x, false, adj);
    ans += solve(orig_b, orig_x, b - 1, x - 1, true, adj + last_placed);
    return ans;
}
int main()
{
    int b;
    cin >> b;
    for (int x = 1; x <= b; x++)
    {
        cout << solve(b, x, b, x, false, 0) << " ";
    }
    cout << "\n";
}