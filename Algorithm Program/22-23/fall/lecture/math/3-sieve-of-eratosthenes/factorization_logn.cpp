// https://ideone.com/aoWvPj
#include <iostream>
#include <vector>
using namespace std;

vector<int> calc_prime_divisors(int n) {
    vector<int> prime_divisor(n + 1);
    // prime_divisor[i] is any prime divisor of i (largest for most of i's)

    for (int i = 2; i <= n; i++) {
        // if i is a prime, then prime_divisor[i] == 0
        if (prime_divisor[i])
            continue; // i is not a prime, because it has a prime divisor smaller than itself

        prime_divisor[i] = i; // assign it manually, when i is a prime

        if (1ll * i * i <= n)
            for (int multiple = i * i; multiple <= n; multiple += i) {
                prime_divisor[multiple] = i;
            }
    }
    return prime_divisor;
}

struct PrimePower {
    int prime;
    int exponent;
};

vector<PrimePower> factorize(int n, vector<int> &prime_divisor) {
    vector<PrimePower> factorization;

    while (n > 1) {
        int prime = prime_divisor[n];
        PrimePower prime_power{prime, 0};
        while (n % prime == 0) {
            n /= prime;
            prime_power.exponent++;
        }
        factorization.push_back(prime_power);
    }

    return factorization; // might be unordered!
}

void print_factorization(vector<PrimePower> &factorization) {
    int i = 0;
    for (PrimePower &prime_power : factorization) {
        i++;
        cout << prime_power.prime << "^" << prime_power.exponent;
        if (i < factorization.size())
            cout << " * ";
    }
}

int main() {
    int n = 1e8;
    vector<int> prime_divisor = calc_prime_divisors(n);
    int n_numbers_to_print = 10;
    for (int i = 0; i < n_numbers_to_print; i++) {
        int randint = rand() % n + 1; // [1, n]
        vector<PrimePower> factorization = factorize(randint, prime_divisor);
        cout << randint << " = ";
        print_factorization(factorization);
        cout << "\n";
    }
}