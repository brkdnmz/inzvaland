#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int p[n];
    for (int i = 0; i < n; i++)
        cin >> p[i];
    auto fac = [](int x)
    {
        long long res = 1;
        for (int i = 2; i <= x; i++)
            res *= i;
        return res;
    };

    // This is not the most efficient implementation, of course :D
    // But, n is small, so who cares?
    long long num = 1;
    int coef[n - 1];
    for (int i = 0; i + 1 < n; i++)
    {
        int cnt = 0;
        for (int j = i + 1; j < n; j++)
        {
            cnt += p[i] > p[j];
        }
        num += cnt * fac(n - i - 1);
        coef[i] = cnt;
    }
    cout << num << "\n";
    for (int x : coef)
        cout << x << " ";
    cout << "\n";
}