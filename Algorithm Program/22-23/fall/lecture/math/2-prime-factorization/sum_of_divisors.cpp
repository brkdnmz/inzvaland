// https://ideone.com/D2aEfj
#include <iostream>
using namespace std;
using ll = long long;

ll power(ll prime, int exponent) {
    ll res = 1;
    while (exponent--)
        res *= prime;
    return res;
}

// 1 + prime + prime^2 + ... + prime^exponent
ll calc_geometric_sum(ll prime, int exponent) {
    return (power(prime, exponent + 1) - 1) / (prime - 1);
}

ll calc_divisors_sum_without_formula(ll n) {
    ll sum = 0;
    for (int i = 1; 1ll * i * i <= n; i++) {
        if (n % i)
            continue;
        sum += i;
        if (i != n / i)
            sum += n / i;
    }
    return sum;
}

int main() {
    ll n = 10512969114312ll; // Put ll or LL to the end to specify 64-bit literal
    ll initial_n = n;
    ll sum_of_divisors_with_formula = 1;
    ll sum_of_divisors_without_formula = calc_divisors_sum_without_formula(n);
    for (int i = 2; 1ll * i * i <= n; i++) {
        if (n % i)
            continue;
        // i is a prime divisor
        int exponent = 0;
        while (n % i == 0) {
            n /= i;
            exponent++;
        }
        sum_of_divisors_with_formula *= calc_geometric_sum(i, exponent);
    }
    // n became a prime itself
    if (n > 1) {
        // Factorization includes n^1
        sum_of_divisors_with_formula *= calc_geometric_sum(n, 1);
    }
    cout << "n = " << initial_n << "\n";
    cout << "Sum of divisors w/ formula\t= " << sum_of_divisors_with_formula << "\n";
    cout << "Sum of divisors w/o formula\t= " << sum_of_divisors_without_formula << "\n";
}