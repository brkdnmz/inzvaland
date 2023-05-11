// https://ideone.com/8Obksu
#include <iostream>
#include <vector>
using namespace std;

vector<int> calc_number_of_divisors_up_to(int n) {
    vector<int> n_divisors(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        for (int multiple = i; multiple <= n; multiple += i)
            n_divisors[multiple]++;
    }

    return n_divisors;
}

int calc_number_of_divisors_single(int n) {
    int n_divisors = 0;
    for (int i = 1; i * i <= n; i++) {
        if (n % i)
            continue;
        n_divisors += 1 + (i * i != n);
    }
    return n_divisors;
}

int main() {
    int n = 1e7;
    vector<int> n_divisors = calc_number_of_divisors_up_to(n);
    int n_numbers_to_print = 10;
    for (int i = 0; i < n_numbers_to_print; i++) {
        int randint = rand() % n + 1; // [1, n]
        cout << "Number of divisors of " << randint << ",\n";
        cout << "\tusing sqrt(n) algorithm = " << calc_number_of_divisors_single(randint) << "\n";
        cout << "\tusing sieve = " << n_divisors[randint] << "\n";
    }
}