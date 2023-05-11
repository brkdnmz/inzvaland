#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int coef[4] = {};
    int d;
    cin >> d;
    for (int i = 0; i < 3; i++) {
        int x;
        cin >> x;
        coef[i + 1] += x;
    }
    for (int i = 0; i < 4; i++) {
        int x;
        cin >> x;
        coef[i] += x;
    }
    double l = 0, r = d;
    for (int i = 0; i < 100; i++) {
        double mid = (l + r) / 2;
        double dist_after_m_mins = 0;
        for (int c : coef)
            dist_after_m_mins = mid * dist_after_m_mins + c;
        dist_after_m_mins *= mid;
        if (d > dist_after_m_mins)
            l = mid;
        else
            r = mid;
    }
    cout << fixed << setprecision(2) << l << "\n";
}