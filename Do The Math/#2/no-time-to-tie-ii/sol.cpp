#include <bits/stdc++.h>
using namespace std;

const int M = 1e9 + 7; // Our modulo value.
const int N = 2505;    // A value large enough to cover all test cases in general.

// A modulo sum function that is faster than (a + b) % M when both 0 < a, b < M.
// (A single % operation is unfortunately slower than all these lines combined.)
int sum(int a, int b)
{
    a += b;
    if (a >= M)
        a -= M;
    return a;
}

int main()
{
    // Fill in the binomial coefficient table (modulo M) beforehand.
    int C[N][N];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            // Base case(s): C(i, 0) = 0
            if (j == 0)
                C[i][j] = 1;
            else if (i == 0)
                C[i][j] = 0;
            else
                C[i][j] = sum(C[i - 1][j - 1], C[i - 1][j]);
        }
    }

    int b;
    cin >> b;
    for (int x = 1; x <= b; x++)
    {
        if (b - x >= x - 1)
        {
            cout << C[b - x + 1][x] << " ";
        }
        else
        {
            cout << C[x - 1][b - x] << " ";
        }
    }
    cout << "\n";
}