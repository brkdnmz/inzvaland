#include <bits/stdc++.h> // Every stuff we need is under there...
using namespace std;

#define pb push_back // So convenient to use :D

void f(int x = 5) {
    if (!x)
        return;
    int a = x;
    f(x - 1);
}

int main() {
    srand(time(0));
    stack<int> stk;
    vector<int> v;
    for (int i = 0; i < 10; i++) {
        v.pb(rand() % 10);
    }
    cout << "Elements pushed:\t";
    for (int x : v) {
        cout << x << " ";
        stk.push(x);
    }
    cout << "\n";
    cout << "Is it so..?\t\t";
    while (!stk.empty()) { // or while(stk.size())
        cout << stk.top() << " ";
        stk.pop();
    }
    cout << "\n";
}