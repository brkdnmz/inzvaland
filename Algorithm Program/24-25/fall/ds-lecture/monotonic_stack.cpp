#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    stack<int> s;
    int a[n];
    vector<int> smaller_left(n, -1), smaller_right(n, n);
    for (int i = 0; i < n; i++) {
        while (s.size() && a[s.top()] >= a[i]) {
            smaller_right[s.top()] = i;
            s.pop();
        }
        if (s.size())
            smaller_left[i] = s.top();
    }
    vector<int> larger_left(n, -1), larger_right(n, n);
    for (int i = 0; i < n; i++) {
        while (s.size() && a[s.top()] <= a[i]) {
            larger_right[s.top()] = i;
            s.pop();
        }
        if (s.size())
            larger_left[i] = s.top();
    }
}