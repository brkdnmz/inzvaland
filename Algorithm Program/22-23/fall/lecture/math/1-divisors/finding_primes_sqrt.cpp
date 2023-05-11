// https://ideone.com/nolkPT
#include <iostream>
using namespace std;

bool is_prime(int n) {
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    int n = 1e6;
    int n_primes = 0;
    for (int i = 1; i <= n; i++) {
        n_primes += is_prime(i);
    }
    cout << "Number of primes up to " << n << " = " << n_primes << "!\n";
}