#include <bits/stdc++.h>
using namespace std;

int main() {
    int n = 13012023;
    int n_divisors = 0;

    // Iterate over d's
    for (int d = 1; d <= n; d++) {
        // The remainder is zero -> d is a divisor!
        if (n % d == 0) { // Do whatever you want...
            n_divisors++;
        }
    }

    // Hate endl, embrace "\n" :)
    cout << n_divisors << "\n";
}
