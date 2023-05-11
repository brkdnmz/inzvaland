#include <bits/stdc++.h> // Every stuff we need is under there...
using namespace std;

#define pb push_back // So convenient to use :D

int main() {
    srand(time(0));
    // int v[5] = {};
    vector<int> v;             // empty vector
    vector<int> v2(5, 2);      // vector of size 5, each element is 2
    vector<int> v3(5);         // vector of size 5, each element is 0
    vector<vector<int>> v4(6); // 2D vector, containing 6 empty vectors
    for (int i = 0; i < 6; i++) {
        int cur_size = rand() % 10;
        while (cur_size--) {
            int cur_element = rand() % 10;
            v4[i].pb(cur_element);
        }
        cout << "v4[" << i << "]: ";
        for (int x : v4[i]) {
            cout << x << " ";
        }
        // for(int j = 0; j < v4[i].size(); j++){
        //     cout << v4[i][j] << " ";
        // }
        cout << "\n";
    }
    // v2[v2.size() - 1]
    // cout << v2.back() << "\n"; // last element
    v4.pop_back(); // remove the last vector from the 2D vector
    for (auto &v : v4) {
        for (int x : v)
            cout << x << " ";
        cout << "\n";
    }

    for (int x : v)
        cin >> x;
}