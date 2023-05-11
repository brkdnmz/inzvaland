#include <bits/stdc++.h> // Every stuff we need is under there...
using namespace std;

#define pb push_back // So convenient to use :D

int main() {
    int n, p;
    cin >> n >> p;
    set<int> s;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        int mate = (p - x + p) % p;
        if (s.count(mate)) {
            cout << "Yes";
            return 0;
        }
        s.insert(x);
    }
}