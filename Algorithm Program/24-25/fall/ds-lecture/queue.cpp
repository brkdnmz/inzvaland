#include <bits/stdc++.h>
using namespace std;

// https://en.cppreference.com/w/cpp/container/queue
// Pops from the front, pushes to the back.

/*
    Process one list L.
    L initially contains n only.
    In each move:
        - Take the leftmost number from L and erase it.
        - If x is odd, write x - 1 to the end of L.
        - Else, write x / 2 and x - 2 to the end of L, in this order.
            - If x is 0, do nothing.

    In the end, print L.
*/

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    queue<int> q;
    q.push(n);
    // q.size() != 0
    while (q.size()) { // or !q.empty()
        int x = q.front();
        q.pop();
        cout << x << " ";
        if (!x)
            continue; // guard condition
        q.push(x % 2 ? x - 1 : x / 2);
        if (x % 2 == 0)
            q.push(x - 2);
    }
    cout << "\n";
}