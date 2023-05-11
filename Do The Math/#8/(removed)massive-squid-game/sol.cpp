#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << max(a, b) / __gcd(a, b) << "\n";
}