#include <bits/stdc++.h>
using namespace std;

// https://en.cppreference.com/w/cpp/container/vector

// Special case: vector<bool>
// https://en.cppreference.com/w/cpp/container/vector_bool
// Not a vector containing bools!

// size (n) is the total number of elements
// capacity is the size of the underlying array (number of elements occupied in memory)
// Whenever size == capacity, double the capacity before the next push_back, hence O(n) amortized.

void info(vector<int> &v) { cout << v.size() << " " << v.capacity() << "\n"; }

struct S {
    int a, b, c;
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int reserve, n;
    cin >> reserve >> n;

    vector<int> v(n);
    v.reserve(reserve);

    for (int i = 0; i < v.size(); i++) {
    }

    for (auto it = v.begin(); it != v.end(); it++) {
        int x = *it;
        int index = it - v.begin();
    }

    for (int x : v) {
    }

    // I don't really use reserve in practice, just to show the capacity increase.
    // There might be rare cases where reserve saves the day.

    // info(v);

    for (int i = 0; i < n; i++) {
        v.emplace_back(S{1, 2, 3});

        // info(v);
    }
    for (int i = 0; i < n; i++) {
        v.pop_back();
        // info(v);
    }
}