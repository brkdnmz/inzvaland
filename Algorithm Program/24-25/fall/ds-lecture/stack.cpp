#include <bits/stdc++.h>
using namespace std;

// https://en.cppreference.com/w/cpp/container/stack
// Pops from and pushes to the top.

/*
    Given a bracket sequence that contains "(" and ")",
    for each closing bracket, determine its opening bracket's position.

    (() -> 1
    ()) -> 0, -
    (()())())() -> 1, 3, 0, 6, -, 9
*/

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n; // Parantez sayısı
    cin >> n;
    stack<int> s; // Açık parantezler
    for (int i = 0; i < n; i++) {
        char bracket;
        cin >> bracket;

        if (bracket == '(') {
            s.push(i);
        } else {
            if (!s.size()) {
                cout << "- ";
            } else {
                cout << s.top() << " ";
                s.pop();
            }
            // cout << i << "\n";
        }
    }
}