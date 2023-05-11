// https://ideone.com/k2WMUG
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n = 123456;
    vector<int> positive_divisors;
    for (int i = 1; i <= n; i++) {
        if (n % i)
            continue; // r > 0
        // i is a divisor, do whatever you want!
        positive_divisors.push_back(i);
    }
    int n_positive_divisors = positive_divisors.size();
    cout << "n: " << n << "\n";
    cout << "Number of positive divisors: " << n_positive_divisors << "\n";
    cout << "Number of all divisors: " << 2 * n_positive_divisors << "\n";
    cout << "Positive divisors:\n";
    for (int d : positive_divisors) {
        cout << d << " ";
    }
    cout << "\n";
}