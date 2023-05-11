#include <bits/stdc++.h> // Every stuff we need is under there...
using namespace std;

#define pb push_back // So convenient to use :D

int main() {
    srand(time(0));
    queue<int> q;
    vector<int> v;
    for (int i = 0; i < 10; i++) {
        v.pb(rand() % 10);
    }
    cout << "Elements pushed:\t";
    for (int x : v) {
        cout << x << " ";
        q.push(x);
    }
    cout << "\n";
    cout << "Is it so..?\t\t";
    while (!q.empty()) { // or while(q.size())
        cout << q.front() << " ";
        q.pop();
    }
    cout << "\n";
}