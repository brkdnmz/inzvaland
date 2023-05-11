#include <bits/stdc++.h> // Every stuff we need is under there...
using namespace std;

#define pb push_back // So convenient to use :D

int main() {
    srand(time(0));
    string s = "(()())()(((())()))";
    stack<int> stk;
    vector<int> v;
    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        if (c == '(') {
            stk.push(i);
        } else {
            if(stk.empty()) return 0;
            int open_paran_index = stk.top();
            v.push_back(open_paran_index);
            stk.pop();
        }
    }
    if(stk.size()) return 0;
    for (int x : v)
        cout << x << " ";
    cout << "\n";
}