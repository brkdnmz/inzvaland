// https://ideone.com/qH1Y3q
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll factorial(int n) {
    ll res = 1;
    for (int i = 1; i <= n; i++) {
        res *= i;
    }
    return res;
}

ll factorial_recursive(int n) {
    if (!n)
        return 1;
    return n * factorial_recursive(n - 1);
}

void print_factorials(int n) {
    for (int i = 0; i <= n; i++) {
        cout << i << "!:";
        if (i < 10)
            cout << "\t";
        cout << " ";
        cout << factorial(i) << " (iterative), ";
        cout << factorial_recursive(i) << " (recursive)\n";
    }
}

int main() {
    int n = 25;
    print_factorials(n);
}